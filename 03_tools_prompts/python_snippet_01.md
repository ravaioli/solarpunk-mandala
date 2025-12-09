# Example: Python Snippet 01

Purpose
- Small reproducible script to generate a simple mandala-like radial pattern using PIL (Pillow).

Example
```python
from PIL import Image, ImageDraw
import math

W = H = 800
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
cx, cy = W // 2, H // 2

for i in range(36):
    angle = i * (2 * math.pi / 36)
    x = cx + math.cos(angle) * 260
    y = cy + math.sin(angle) * 260
    r = 40
    draw.ellipse((x-r, y-r, x+r, y+r), outline="darkgreen", width=3)

img.save("mandala_example.png")
```

Notes
- This is a tiny starting point — experiment with gradients, blending, and per-element color rules.
