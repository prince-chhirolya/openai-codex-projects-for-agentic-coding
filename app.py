from pathlib import Path
from flask import Flask, render_template
from models import db

BASE_DIR = Path(__file__).resolve().parent


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BASE_DIR / 'pixel_art.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


with app.app_context():
    from models import Canvas

    db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)