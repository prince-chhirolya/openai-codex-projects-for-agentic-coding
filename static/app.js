const editor = document.getElementById("canvas-editor");
const canvas = document.getElementById("pixel-canvas");
const palette = document.getElementById("palette");
const saveForm = document.getElementById("save-form");
const saveButton = document.getElementById("save-button");
const saveStatus = document.getElementById("save-status");
const selectedColorValue = document.getElementById("selected-color-value");
const nameInput = document.getElementById("canvas-name");

const gridSize = Number(editor.dataset.gridSize);
const defaultColor = editor.dataset.defaultColor;
const colorPalette = JSON.parse(editor.dataset.palette);
const context = canvas.getContext("2d");
const cellSize = canvas.width / gridSize;

let selectedColor = defaultColor;
let isDrawing = false;
const pixelData = Array.from({ length: gridSize }, () =>
  Array.from({ length: gridSize }, () => defaultColor)
);

function setStatus(message, type = "") {
  saveStatus.textContent = message;
  saveStatus.className = `save-status ${type}`.trim();
}

function drawGrid() {
  context.clearRect(0, 0, canvas.width, canvas.height);

  for (let row = 0; row < gridSize; row += 1) {
    for (let column = 0; column < gridSize; column += 1) {
      context.fillStyle = pixelData[row][column];
      context.fillRect(column * cellSize, row * cellSize, cellSize, cellSize);
    }
  }

  context.strokeStyle = "rgba(44, 36, 27, 0.12)";
  context.lineWidth = 1;

  for (let index = 0; index <= gridSize; index += 1) {
    const offset = index * cellSize;

    context.beginPath();
    context.moveTo(offset, 0);
    context.lineTo(offset, canvas.height);
    context.stroke();

    context.beginPath();
    context.moveTo(0, offset);
    context.lineTo(canvas.width, offset);
    context.stroke();
  }
}

function getGridPosition(event) {
  const rect = canvas.getBoundingClientRect();
  const x = Math.floor(((event.clientX - rect.left) / rect.width) * gridSize);
  const y = Math.floor(((event.clientY - rect.top) / rect.height) * gridSize);

  if (x < 0 || x >= gridSize || y < 0 || y >= gridSize) {
    return null;
  }

  return { x, y };
}

function paintPixel(event) {
  const position = getGridPosition(event);
  if (!position) {
    return;
  }

  const { x, y } = position;
  if (pixelData[y][x] === selectedColor) {
    return;
  }

  pixelData[y][x] = selectedColor;
  drawGrid();
}

palette.addEventListener("click", (event) => {
  const swatch = event.target.closest("[data-color]");
  if (!swatch) {
    return;
  }

  selectedColor = swatch.dataset.color;
  selectedColorValue.textContent = selectedColor;

  for (const button of palette.querySelectorAll("[data-color]")) {
    button.classList.toggle("active", button === swatch);
  }
});

canvas.addEventListener("pointerdown", (event) => {
  isDrawing = true;
  canvas.setPointerCapture(event.pointerId);
  paintPixel(event);
});

canvas.addEventListener("pointermove", (event) => {
  if (!isDrawing) {
    return;
  }

  paintPixel(event);
});

canvas.addEventListener("pointerup", () => {
  isDrawing = false;
});

canvas.addEventListener("pointerleave", () => {
  isDrawing = false;
});

saveForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  setStatus("");
  saveButton.disabled = true;

  try {
    const response = await fetch("/canvases", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: nameInput.value,
        pixel_data: pixelData,
      }),
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.message || "Unable to save canvas.");
    }

    setStatus(data.message, "success");
  } catch (error) {
    setStatus(error.message, "error");
  } finally {
    saveButton.disabled = false;
  }
});

context.imageSmoothingEnabled = false;
selectedColorValue.textContent = selectedColor;
drawGrid();
