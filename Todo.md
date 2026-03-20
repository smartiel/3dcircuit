# Todo

## Pending

- [ ] Implement a small full client-side webapp that utilizes Three.js to display a .ply file
  - [ ] Set up `index.html` with a Three.js scene (camera, renderer, lights)
  - [ ] Add a PLYLoader to load and parse a `.ply` file
  - [ ] Display the loaded geometry as a mesh in the scene
  - [ ] Add basic orbit controls so the user can rotate/zoom the model
  - [ ] Allow the user to pick the `.ply` file via a file input or a hardcoded default path
- [ ] Implement a small script that starts the webapp locally and opens a browser connecting to the webapp
  - [ ] Choose a minimal static file server (e.g. Python `http.server` or `npx serve`)
  - [ ] Write the script (`start.sh` or `start.py`) to start the server on a fixed port
  - [ ] Open the browser automatically (using `xdg-open`, `open`, or `start` depending on OS)

## In Progress



## Completed

- [x] Create Todo.md
