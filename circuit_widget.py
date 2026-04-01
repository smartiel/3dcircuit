"""
Jupyter notebook widget for the 3D quantum circuit viewer.

Usage:
    from circuit_widget import show_circuit

    from qiskit import QuantumCircuit
    qc = QuantumCircuit(3)
    qc.h(0); qc.cx(0, 1); qc.cx(1, 2)

    # Auto circular layout
    show_circuit(qc)

    # Explicit layout: {qubit_index: (x, y)}
    show_circuit(qc, layout={0: (0, 0), 1: (1, 0), 2: (2, 0)})
"""

import os
import json
import base64


def show_circuit(circuit, layout=None, width=900, height=600):
    """Display a Qiskit QuantumCircuit in the 3D viewer inside a Jupyter notebook.

    Parameters
    ----------
    circuit : qiskit.QuantumCircuit
        The circuit to visualise.
    layout : dict[int, tuple[float, float]] | None
        Optional mapping from qubit index to (x, y) position.
        If None, a circular layout is computed automatically.
    width : int
        Width of the embedded iframe in pixels.
    height : int
        Height of the embedded iframe in pixels.
    """
    from qiskit import qasm2
    from IPython.display import display, HTML

    # Convert circuit to QASM 2.0 string
    qasm_str = qasm2.dumps(circuit)

    # Convert layout dict {qubit_index: (x, y)} to viewer text format
    layout_str = None
    if layout is not None:
        lines = []
        for bit_idx, (x, y) in layout.items():
            qubit = circuit.qubits[bit_idx]
            reg = qubit._register
            idx = qubit._index
            lines.append(f"{reg.name}[{idx}] {float(x)} {float(y)}")
        layout_str = "\n".join(lines)

    # Load index.html template
    here = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(here, "index.html")
    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    # Build injection data
    data = {"qasm": qasm_str}
    if layout_str:
        data["layout"] = layout_str

    inject = f"<script>window.__CIRCUIT_DATA__={json.dumps(data)};</script>"
    html = template.replace("</head>", f"{inject}\n</head>", 1)

    # Encode as base64 blob URL via JS to avoid data-URI size limits
    b64 = base64.b64encode(html.encode("utf-8")).decode("ascii")
    uid = abs(hash((qasm_str, layout_str, width, height)))

    iframe_js = f"""
(function() {{
  var b64 = "{b64}";
  var binary = atob(b64);
  var bytes = new Uint8Array(binary.length);
  for (var i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
  var blob = new Blob([bytes], {{type: "text/html"}});
  var url  = URL.createObjectURL(blob);
  var iframe = document.createElement("iframe");
  iframe.src = url;
  iframe.width  = "{width}";
  iframe.height = "{height}";
  iframe.style.border = "none";
  document.getElementById("cw-{uid}").appendChild(iframe);
}})();
"""

    display(HTML(f'<div id="cw-{uid}"></div><script>{iframe_js}</script>'))
