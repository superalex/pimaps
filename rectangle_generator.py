import numpy
import struct
from PIL import Image, ImageDraw
from random import randint

TOTAL = 500
WIDTH = 28
HEIGHT = 28
LINE_WIDTH = 1
OUTPUT_IMAGES = "rectangles_images_idx3_ubyte"
OUTPUT_LABELS = "rectangles_labels_idx3_ubyte"

def draw_rectangle(img, x0, y0, x1, y1, line_width):
    fill_color = "white"
    draw = ImageDraw.Draw(img)
    draw.line([x0, y0, x1, y0], fill=fill_color, width=line_width)
    draw.line([x1, y0, x1, y1], fill=fill_color, width=line_width)
    draw.line([x1, y1, x0, y1], fill=fill_color, width=line_width)
    draw.line([x0, y1, x0, y0], fill=fill_color, width=line_width)

with open(OUTPUT_IMAGES, "wb") as rectangles_bs, open(OUTPUT_LABELS, "wb") as labels_bs:
    magic_images = 2051
    magic_labels = 2049

    rectangles_bs.write(magic_images.to_bytes(4, byteorder = 'big'))
    rectangles_bs.write(TOTAL.to_bytes(4, byteorder = 'big'))
    rectangles_bs.write(WIDTH.to_bytes(4, byteorder = 'big'))
    rectangles_bs.write(HEIGHT.to_bytes(4, byteorder = 'big'))

    labels_bs.write(magic_labels.to_bytes(4, byteorder = 'big'))
    labels_bs.write(TOTAL.to_bytes(4, byteorder = 'big'))

    img = Image.new("L", (28, 28), "black")

    for n in range(TOTAL):
        print(n+1, "/", TOTAL)
        rectangles = randint(1, 3)
        for r in range(rectangles):
            x0 = randint(0, WIDTH-15)
            y0 = randint(0, HEIGHT-15)
            x1 = randint(x0+5, WIDTH-5)
            y1 = randint(y0+5, HEIGHT-5)
            draw_rectangle(img, x0, y0, x1, y1, LINE_WIDTH)

        pixels = img.load()
        pixels_array = numpy.empty([28, 28], dtype=numpy.uint8)

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixel = pixels[i, j]
                rectangles_bs.write(pixel.to_bytes(1, byteorder = 'big'))
                labels_bs.write(rectangles.to_bytes(1, byteorder = 'big'))


"""
def extract():
    def _read32(bytestream):
        dt = numpy.dtype(numpy.uint32).newbyteorder('>')
        return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]

    with open("kk", "rb") as bytestream:
        magic = _read32(bytestream)
        if magic != 2051:
          raise ValueError(
              'Invalid magic number %d in MNIST image file:' % (magic))
        num_images = _read32(bytestream)
        rows = _read32(bytestream)
        cols = _read32(bytestream)
        buf = bytestream.read(rows * cols * num_images)
        data = numpy.frombuffer(buf, dtype=numpy.uint8)
        data = data.reshape(num_images, rows, cols, 1)

        print(num_images, rows, cols)

        img = Image.new( 'L', (28, 28), "black") # create a new black image
        pixels = img.load() # create the pixel map

        for i in range(img.size[0]):    # for every pixel:
            for j in range(img.size[1]):
                pixels[i , j] = int(data[0][i][j][0]) #(i, j, data[100][i][j][0]) # set the colour accordingly

        img.save("2.bmp")
"""
