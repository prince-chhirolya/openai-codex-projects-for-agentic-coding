# Building a Flask Pixel Art Canvas App using Codex

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

**https://github.com/prince-chhirolya/building-a-flask-pixel-art-canvas-app-using-codex** (Complete Project Source Code on GitHub)

Let’s see what Codex did. It created six new files and updated two existing ones:

- app.py (updated): Refactored into an app factory with a create_app() function. This keeps the route handlers and configuration separate and makes the app easier to test.
- routes/canvas.py: A new routes file with two endpoints. One serves the drawing page and one handles saving a canvas to the database.
- services/canvas_service.py: A new service file that handles all the business logic: defining the colour palette, validating the pixel grid, and writing to the database.
- templates/index.html (updated): Replaced with a two-panel layout showing the colour palette and Save form on the left and the drawing grid on the right.
- static/app.js: A new JavaScript file that handles drawing on the grid, colour selection, and sending the saved canvas to the API.
- static/styles.css: A new stylesheet for the two-panel layout.

The drawing interface is now live. We can paint on the grid, pick a colour, enter a name, and save our canvas to the database.

Both tasks followed the same pattern: a short, outcome-focused prompt produced a complete, well-structured implementation. The prompts described what to build and AGENTS.md handled the conventions behind the scenes. Codex applied the project structure, kept business logic in service functions, and even wrote and ran tests without being asked. Writing good prompts and a well-defined AGENTS.md is what makes this possible.

XXXXXX Completed XXXXXX
