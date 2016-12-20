from PIL import Image, ImageDraw
from random import randint
import os


TOTAL = 100
WIDTH = 28
HEIGHT = 28
LINE_WIDTH = 1
RECTANGLES_PER_IMAGE = 1
OUTPUT_BASE_PATH = "output"


def draw_rectangle(img, x0, y0, x1, y1, line_width):
    fill_color = "black"
    draw = ImageDraw.Draw(im)
    draw.line([x0, y0, x1, y0], fill=fill_color, width=line_width)
    draw.line([x1, y0, x1, y1], fill=fill_color, width=line_width)
    draw.line([x1, y1, x0, y1], fill=fill_color, width=line_width)
    draw.line([x0, y1, x0, y0], fill=fill_color, width=line_width)

for i in range(TOTAL):
    im = Image.new("RGB", (WIDTH, HEIGHT), "white")
    for r in range(RECTANGLES_PER_IMAGE):
        x0 = randint(0, WIDTH-15)
        y0 = randint(0, HEIGHT-15)
        x1 = randint(x0+5, WIDTH-5)
        y1 = randint(y0+5, HEIGHT-5)
        draw_rectangle(im, x0, y0, x1, y1, LINE_WIDTH)

    im.save(os.path.join(OUTPUT_BASE_PATH, str(i) + ".png"), "PNG")
