import re

from models import Canvas, db


GRID_SIZE = 32
DEFAULT_COLOR = "#ffffff"
COLOR_PALETTE = [
    "#ffffff",
    "#000000",
    "#ff595e",
    "#ffca3a",
    "#8ac926",
    "#1982c4",
    "#6a4c93",
    "#ff924c",
]
HEX_COLOR_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}$")


class ValidationError(ValueError):
    pass


def build_blank_pixel_data(fill_color=DEFAULT_COLOR):
    return [[fill_color for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def validate_pixel_data(pixel_data):
    if not isinstance(pixel_data, list) or len(pixel_data) != GRID_SIZE:
        raise ValidationError("Canvas data must contain exactly 32 rows.")

    normalized_rows = []
    for row in pixel_data:
        if not isinstance(row, list) or len(row) != GRID_SIZE:
            raise ValidationError("Each canvas row must contain exactly 32 pixels.")

        normalized_row = []
        for color in row:
            if not isinstance(color, str) or not HEX_COLOR_PATTERN.fullmatch(color):
                raise ValidationError("Each pixel must be a hex color string like #ff0000.")
            normalized_row.append(color.lower())
        normalized_rows.append(normalized_row)

    return normalized_rows


def create_canvas(name, pixel_data):
    cleaned_name = (name or "").strip()
    if not cleaned_name:
        raise ValidationError("Please give your canvas a name before saving.")
    if len(cleaned_name) > 255:
        raise ValidationError("Canvas name must be 255 characters or fewer.")

    normalized_pixels = validate_pixel_data(pixel_data)

    canvas = Canvas(name=cleaned_name, pixel_data=normalized_pixels)
    db.session.add(canvas)
    db.session.commit()
    return canvas
