const previewCanvases = document.querySelectorAll(".gallery-preview");

function drawPreview(previewCanvas) {
  const pixels = JSON.parse(previewCanvas.dataset.pixelData || "[]");
  const gridSize = pixels.length;
  if (!gridSize) {
    return;
  }

  const context = previewCanvas.getContext("2d");
  const cellSize = previewCanvas.width / gridSize;

  context.imageSmoothingEnabled = false;
  context.clearRect(0, 0, previewCanvas.width, previewCanvas.height);

  for (let row = 0; row < gridSize; row += 1) {
    for (let column = 0; column < gridSize; column += 1) {
      context.fillStyle = pixels[row][column];
      context.fillRect(column * cellSize, row * cellSize, cellSize, cellSize);
    }
  }
}

for (const previewCanvas of previewCanvases) {
  drawPreview(previewCanvas);
}
