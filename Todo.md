# Todo

## Pending

## In Progress

## Completed

- [x] Create Todo.md
- [x] Implement a small full client-side webapp that utilizes Three.js to display a .ply file
  - [x] Set up `index.html` with a Three.js scene (camera, renderer, lights)
  - [x] Add a PLYLoader to load and parse a `.ply` file
  - [x] Display the loaded geometry as a mesh in the scene
  - [x] Add basic orbit controls so the user can rotate/zoom the model
  - [x] Allow the user to pick the `.ply` file via a file input or a hardcoded default path
- [x] Implement a small script that starts the webapp locally and opens a browser connecting to the webapp
  - [x] Choose a minimal static file server (e.g. Python `http.server` or `npx serve`)
  - [x] Write the script (`start.sh`) to start the server on a fixed port
  - [x] Open the browser automatically (using `xdg-open`, `open`, or `start` depending on OS)
