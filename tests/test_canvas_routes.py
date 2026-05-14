import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import create_app
from models import Canvas, db
from services.canvas_service import build_blank_pixel_data


@pytest.fixture()
def app(tmp_path):
    database_path = tmp_path / "test.db"
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{database_path}",
        }
    )

    with app.app_context():
        db.drop_all()
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index_route_renders_editor(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Draw your first 32x32 canvas" in response.data
    assert b"pixel-canvas" in response.data


def test_save_canvas_success(client, app):
    response = client.post(
        "/canvases",
        json={"name": "Sunset", "pixel_data": build_blank_pixel_data("#ffffff")},
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == '"Sunset" saved successfully.'

    with app.app_context():
        canvas = Canvas.query.one()
        assert canvas.name == "Sunset"
        assert len(canvas.pixel_data) == 32
        assert len(canvas.pixel_data[0]) == 32


def test_save_canvas_requires_name(client):
    response = client.post(
        "/canvases",
        json={"name": "   ", "pixel_data": build_blank_pixel_data("#000000")},
    )

    assert response.status_code == 400
    assert response.get_json()["message"] == "Please give your canvas a name before saving."
