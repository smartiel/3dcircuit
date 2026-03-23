# 3D Circuit Viewer

An interactive, browser-based 3D visualiser for quantum circuits. Open `index.html` directly in any modern browser — no server or install required.

---

## Quick start

1. Open `index.html` in your browser.
2. Click **Load example** to instantly see a 4-qubit circuit rendered in 3D.
3. Rotate, zoom and pan the circuit with your mouse (see controls below).

---

## Loading your own circuit

A circuit requires two files: a **QASM file** describing the gates and a **layout file** placing the qubits in 2D space.

### 1 — QASM file (`.qasm`)

Standard OpenQASM 2.0. Supported gate names: `h`, `x`, `y`, `z`, `s`, `sdg`, `t`, `tdg`, `rx`, `ry`, `rz`, `u` / `u1` / `u2` / `u3`, `cx`, `cy`, `cz`, `swap`, `ccx`. Unknown gate names are rendered in grey ("Other").

`measure`, `barrier`, `reset` and classical control (`if`) statements are silently ignored.

```openqasm
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
h q[0];
cx q[0], q[1];
```

### 2 — Layout file (`.txt` or `.csv`)

One qubit per line: `name  x  y` (whitespace-separated). Lines starting with `#` are treated as comments.
The X and Y coordinates are the qubit positions in the cross-section plane; the time (circuit depth) axis runs along Z.

```
# qubit layout: name x y
q[0] 0 0
q[1] 1 0
q[2] 0 1
q[3] 1 1
```

Qubit names must match exactly the register names used in the QASM file (e.g. `q[0]`).

### 3 — Building the circuit

1. Click **Open .qasm** and select your QASM file.
2. Click **Open layout** and select your layout file.
3. The **Build 3D circuit** button becomes active — click it to render.

The status bar shows the total gate count and circuit depth after a successful build. Changing settings (geometry, colors, …) automatically rebuilds the circuit.

---

## Loading a PLY mesh

Click **Open .ply file** to load any PLY geometry (with or without vertex colours). The mesh is automatically centred and scaled to fit the viewport. Useful for overlaying a chip floorplan or any custom 3D model.

---

## Navigation

| Action | Control |
|---|---|
| Rotate | Left-drag |
| Zoom | Right-drag or scroll wheel |
| Pan | Middle-drag |

The camera always orbits around the centre of the loaded object.

---

## Settings panel

Click **⚙ Settings** in the toolbar to open the settings panel.

### Geometry

| Slider | Effect |
|---|---|
| **Time step** | Spacing between successive gate layers along Z |
| **Gate depth** | Thickness of each gate block along Z |
| **Margin** | Padding added around each gate block in X and Y |

### Wires

| Control | Effect |
|---|---|
| **Color** | Colour of the qubit wire cylinders |
| **Thickness** | Radius of the wire cylinders |

### Labels

| Control | Effect |
|---|---|
| **Show labels** | Toggle gate-name text sprites on/off |

### Gate Colors

Each gate type has:
- A **colour picker** to change its display colour. Aliases (S / S†, Rx/Ry/Rz, …) share the same colour swatch.
- A **checkbox** to instantly show or hide all gates of that type (and their labels). Hidden gates are remembered across rebuilds.

---

## File format reference

### Layout file

```
# comment
<qubit_name>  <x>  <y>
```

- `qubit_name` — must match the QASM register name exactly, e.g. `q[0]`
- `x`, `y` — floating-point 2D coordinates (any unit; the viewer normalises to fit the viewport)

### QASM file

Standard OpenQASM 2.0 (`OPENQASM 2.0;`). Gate parameters (rotation angles) are parsed but not displayed. Multi-qubit gates spanning non-adjacent qubits are fully supported and rendered as a single block stretching between the involved qubits.

---

## Examples

The `examples/` folder contains ready-to-use files:

| File | Description |
|---|---|
| `bell.qasm` | 4-qubit circuit with H, CX, T, S gates |
| `grid2x2.layout` | 2 × 2 qubit grid (matches `bell.qasm`) |
| `cube.ply` | Simple PLY mesh for testing the PLY loader |
