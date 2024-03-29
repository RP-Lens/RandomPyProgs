import numpy as np
from PIL import Image
from scipy.interpolate import interp1d

from mandy import MandelbrotSet
from viewport import Viewport


def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]


def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color) for color in palette
    ]


def makeGrad(colors, interpolation="linear"):
    X = [i / (len(colors) - 1) for i in range(len(colors))]
    Y = [[color[i] for color in colors] for i in range(3)]
    channels = [interp1d(X, y, kind=interpolation) for y in Y]
    return lambda x: [np.clip(channel(x), 0, 1) for channel in channels]


if __name__ == "__main__":
    print("grab a coffee...")

    black = (0, 0, 0)
    blue = (0, 0, 1)
    maroon = (0.5, 0, 0)
    navy = (0, 0, 0.5)
    red = (1, 0, 0)

    colors = [black, navy, blue, maroon, red, black]
    gradient = makeGrad(colors, interpolation="cubic")

    num_colors = 256
    palette = denormalize(
        [gradient(i / num_colors) for i in range(num_colors)]
    )

    mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=1000)
    image = Image.new(mode="RGB", size=(1024, 1024))
    viewport = Viewport(image, center=-0.75, width=3.5)
    paint(mandelbrot_set, viewport, palette, smooth=True)
    image.show()
