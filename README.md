# OpenAI Codex Projects For Agentic Coding

1. [Building a Flask Pixel Art Canvas App using Codex](#1st-project-building-a-flask-pixel-art-canvas-app-using-codex)
2. [Building a Gallery and PNG Export App using Codex](#2nd-project-building-a-gallery-and-png-export-app-using-codex)
   <br/>

## (1st Project) Building a Flask Pixel Art Canvas App using Codex

## Scaffolding the base app

We will begin by giving Codex the full picture of the app we are building and then asking it to implement the foundation. Providing the full context upfront means Codex understands the shape of the project before writing a single file, which leads to better structural decisions from the start. Here is the prompt we give to Codex:

> Prompt: We are building a Flask pixel art canvas app. The app will let users draw on a 32×32 grid, > > > save their artwork with a name, browse a gallery of saved canvases, and export any canvas as a PNG > > > file. The stack is Flask, SQLite, Flask-SQLAlchemy, HTML5 Canvas, vanilla JavaScript, and Pillow.
>
> For this first task, scaffold the base app:
>
> - app.py: Flask app with SQLAlchemy configured and the database initialised on startup
> - models.py: A Canvas model with fields: id (integer, primary key), name (string, required), pixel_data > (JSON, stores the 32×32 grid as a 2D array of hex colour strings), created_at (timestamp, auto-set)
> - templates/index.html: A minimal base HTML page that the index route serves
>   An index route in app.py that returns the index template
>
> The app should start without errors when we run python3 app.py.

Codex reads the prompt, explores the project folder, and generates the basic structure.

Let’s see what Codex did. It created three files:

- app.py: Sets up the Flask app with a SQLite database, adds the index route, and creates the database tables automatically on startup.
- models.py: Defines the Canvas model with fields for the canvas name, the pixel grid stored as JSON, and a timestamp that is set automatically on every save.
- templates/index.html: A minimal HTML page that the index route serves, confirming the app is running.

Our base foundation is ready. Now, let’s implement the drawing and saving feature.

## Implementing the drawing and saving feature

Now we will ask Codex to add the drawing and saving feature. We describe what the user should be able to do and let Codex figure out how to build it. Here is the prompt:

> Prompt: The base app is running. Now add the drawing and saving feature. The user should be able to draw on a 32×32 pixel grid, pick a colour from a palette, give their canvas a name, and save it. Saving should store the canvas in the database and confirm success on screen.

Codex reads the prompt, reviews the existing files, and implements the full feature. Here is the code:

**https://github.com/prince-chhirolya/openai-codex-projects-for-agentic-coding** (Complete Project Source Code on GitHub)

Let’s see what Codex did. It created six new files and updated two existing ones:

- app.py (updated): Refactored into an app factory with a create_app() function. This keeps the route handlers and configuration separate and makes the app easier to test.
- routes/canvas.py: A new routes file with two endpoints. One serves the drawing page and one handles saving a canvas to the database.
- services/canvas_service.py: A new service file that handles all the business logic: defining the colour palette, validating the pixel grid, and writing to the database.
- templates/index.html (updated): Replaced with a two-panel layout showing the colour palette and Save form on the left and the drawing grid on the right.
- static/app.js: A new JavaScript file that handles drawing on the grid, colour selection, and sending the saved canvas to the API.
- static/styles.css: A new stylesheet for the two-panel layout.

The drawing interface is now live. We can paint on the grid, pick a colour, enter a name, and save our canvas to the database.

Both tasks followed the same pattern: a short, outcome-focused prompt produced a complete, well-structured implementation. The prompts described what to build and AGENTS.md handled the conventions behind the scenes. Codex applied the project structure, kept business logic in service functions, and even wrote and ran tests without being asked. Writing good prompts and a well-defined AGENTS.md is what makes this possible.

---

---

## (2nd Project) Building a Gallery and PNG Export App using Codex

## Adding a gallery page

Now we will ask Codex to add the gallery page. The drawing page already has a way to save canvases, so this task is about giving us somewhere to browse them. We describe the page from the user’s perspective and let Codex handle the structure. Here is the prompt:

> Prompt: Add a gallery page that shows all saved canvases. Each canvas should display its name, the date it was saved, and a visual preview of the pixel art. The gallery should be accessible from the main drawing page and link back to it.

Codex reads the prompt, checks the existing routes and templates, and builds the full gallery feature.

Let’s see what Codex did. It created two new files and updated four existing ones:

- templates/gallery.html: A new page with a navigation bar at the top, a hero section with a heading and description, and a responsive grid of canvas cards. Each card shows a pixel preview of the artwork, the canvas name, and the formatted save date. An empty state message is shown when no canvases have been saved yet.
- static/gallery.js: A new JavaScript file that reads the pixel data stored in each card and renders it onto a small canvas element as a pixel preview.
- routes/canvas.py (updated): A new GET /gallery route was added that fetches all saved canvases and passes them to the gallery template.
- services/canvas_service.py (updated): A new list_canvases() function was added that queries all canvas rows from the database ordered by save date, newest first.
- templates/index.html (updated): A navigation bar was added to the drawing page so we can switch between the editor and the gallery.
- static/styles.css (updated): New styles were added for the gallery layout, canvas cards, pixel previews, and the shared navigation bar.

> Note: Codex updated the tests again
>
> Looking at the project code, we can see that tests/test_canvas_routes.py now has a fourth test: test_gallery_route_shows_saved_canvases. Codex added it without being asked, inserting a canvas directly into the test database and asserting that it appears on the gallery page.

The gallery page is live. We can navigate from the drawing page to the gallery and see all our saved canvases with their previews.

## Adding download button for PNG export

The gallery shows our saved canvases, but we have no way to get them out of the app yet. Now we will ask Codex to add a download feature. We want each gallery card to have a button that generates a PNG file of the canvas artwork. We specify Pillow here because it is already in our requirements.txt and it is the library we chose for this task.

> Prompt: Add a download feature. Each canvas in the gallery should have a Download button that exports the pixel art as a PNG file. Use Pillow to generate the image.

Codex reads the prompt, locates the existing gallery template and service layer, and adds the export feature. Here is the code:

**https://github.com/prince-chhirolya/openai-codex-projects-for-agentic-coding** (Complete Project Source Code on GitHub)

Let’s see what Codex did. It updated four existing files:

- services/canvas_service.py (updated): Three new functions were added. get_canvas() fetches a single canvas by id and returns a 404 if it does not exist. build_canvas_png() creates a 32x32 Pillow image, sets each pixel using the stored hex colour values, scales it up to 512x512 using nearest-neighbour resizing to keep the pixels sharp, and returns the image as a byte buffer ready to send. build_download_filename() generates a clean filename from the canvas name, for example ocean-breeze.png.

- routes/canvas.py (updated): A new GET /canvases/<id>/download route was added. It fetches the canvas, calls build_canvas_png(), and returns the buffer as a file attachment using Flask’s send_file().

- templates/gallery.html (updated): A Download PNG link was added to each canvas card pointing to the download route for that canvas.

- static/styles.css (updated): Styling was added for the download link button.

The app is now complete. We can draw pixel art, save it, browse the gallery, and download any canvas as a PNG file.
