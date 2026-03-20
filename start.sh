#!/usr/bin/env bash
# Starts a local static file server and opens the browser at the webapp.

PORT=${PORT:-8080}
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Find a suitable static server ────────────────────────────────────────────
if command -v python3 &>/dev/null; then
  SERVER_CMD="python3 -m http.server $PORT --directory \"$DIR\""
elif command -v python &>/dev/null; then
  SERVER_CMD="python -m SimpleHTTPServer $PORT"
elif command -v npx &>/dev/null; then
  SERVER_CMD="npx --yes serve -l $PORT \"$DIR\""
else
  echo "Error: no suitable static server found (python3, python, or npx required)." >&2
  exit 1
fi

# ── Start server in background ───────────────────────────────────────────────
echo "Starting server on http://localhost:$PORT …"
eval "$SERVER_CMD" &
SERVER_PID=$!

# Give the server a moment to bind.
sleep 0.5

# ── Open browser ─────────────────────────────────────────────────────────────
URL="http://localhost:$PORT"
if command -v xdg-open &>/dev/null; then
  xdg-open "$URL"
elif command -v open &>/dev/null; then       # macOS
  open "$URL"
elif command -v start &>/dev/null; then      # Windows / Git Bash
  start "$URL"
else
  echo "Could not detect a browser opener. Please open $URL manually."
fi

echo "Server running (PID $SERVER_PID). Press Ctrl+C to stop."

# ── Wait and clean up ────────────────────────────────────────────────────────
trap "kill $SERVER_PID 2>/dev/null; echo 'Server stopped.'" EXIT INT TERM
wait $SERVER_PID
