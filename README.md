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
