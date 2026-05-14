from flask import Blueprint, jsonify, render_template, request, send_file

from services.canvas_service import (
    COLOR_PALETTE,
    DEFAULT_COLOR,
    GRID_SIZE,
    ValidationError,
    build_canvas_png,
    build_download_filename,
    create_canvas,
    get_canvas,
    list_canvases,
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


@canvas_bp.route("/gallery")
def gallery():
    return render_template("gallery.html", canvases=list_canvases())


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


@canvas_bp.route("/canvases/<int:canvas_id>/download")
def download_canvas(canvas_id):
    canvas = get_canvas(canvas_id)
    png_file = build_canvas_png(canvas)

    return send_file(
        png_file,
        mimetype="image/png",
        as_attachment=True,
        download_name=build_download_filename(canvas),
    )
