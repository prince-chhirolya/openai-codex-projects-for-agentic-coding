from flask import Blueprint, jsonify, render_template, request

from services.canvas_service import (
    COLOR_PALETTE,
    DEFAULT_COLOR,
    GRID_SIZE,
    ValidationError,
    create_canvas,
)


canvas_bp = Blueprint("canvas", __name__)


@canvas_bp.route("/")
def index():
    return render_template(
        "index.html",
        color_palette=COLOR_PALETTE,
        default_color=DEFAULT_COLOR,
        grid_size=GRID_SIZE,
    )


@canvas_bp.route("/canvases", methods=["POST"])
def save_canvas():
    payload = request.get_json(silent=True) or {}

    try:
        canvas = create_canvas(
            name=payload.get("name"),
            pixel_data=payload.get("pixel_data"),
        )
    except ValidationError as exc:
        return jsonify({"message": str(exc)}), 400

    return (
        jsonify(
            {
                "id": canvas.id,
                "message": f'"{canvas.name}" saved successfully.',
            }
        ),
        201,
    )
