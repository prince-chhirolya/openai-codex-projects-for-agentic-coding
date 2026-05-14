# Building a Flask Pixel Art Canvas App using Codex


Prompt: We are building a Flask pixel art canvas app. The app will let users draw on a 32×32 grid, save their artwork with a name, browse a gallery of saved canvases, and export any canvas as a PNG file. The stack is Flask, SQLite, Flask-SQLAlchemy, HTML5 Canvas, vanilla JavaScript, and Pillow.

For this first task, scaffold the base app:

app.py: Flask app with SQLAlchemy configured and the database initialised on startup

models.py: A Canvas model with fields: id (integer, primary key), name (string, required), pixel_data (JSON, stores the 32×32 grid as a 2D array of hex colour strings), created_at (timestamp, auto-set)

templates/index.html: A minimal base HTML page that the index route serves

An index route in app.py that returns the index template

The app should start without errors when we run python3 app.py.
