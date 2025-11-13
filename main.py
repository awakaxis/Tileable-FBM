import math
from random import Random, random

import matplotlib.pyplot as plt
from PIL import Image

random = Random()
img = Image.new(mode="L", size=(1920, 1080))

sizeX, sizeY = img.size


def randGradVector(random: Random):
    theta = math.acos(2.0 * random.random() - 1)
    phi = 2.0 * random.random() * math.pi

    return (math.cos(phi) * math.sin(theta), math.sin(phi) * math.sin(theta))


dirs = []
gridSizeX = 10
gridSizeY = 10
for i in range(0, int((gridSizeX + 1) * (gridSizeY + 1))):
    dirs.append(randGradVector(random))


def plotGradientVectors(dirs: list):
    fig, ax = plt.subplots()
    ax.set_xlim(0, gridSizeX)
    ax.set_ylim(0, gridSizeY)
    ax.set_aspect("equal")

    ax.set_xticks(range(0, gridSizeX + 1))
    ax.set_yticks(range(0, gridSizeY + 1))

    ax.grid(True)

    for i, dir in enumerate(dirs):
        ax.quiver(
            i % gridSizeY,
            i / gridSizeX,
            dir[0],
            dir[1],
            angles="xy",
            scale_units="xy",
            scale=1,
            width=0.005,
            headwidth=0.005,
            headlength=0.01,
        )

    plt.show()


# plotGradientVectors(dirs)


def lerp(left, right, factor):
    return left + factor * (right - left)


def smoothstep(x):
    return (3 * (x**2)) - (2 * (x**3))


def bettersmoothstep(x):
    return (6 * x**5) - (15 * x**4) + (10 * x**3)


def perlin(x: int, y: int, dirs: list):
    gridX = x * (gridSizeX / sizeX)
    gridY = y * (gridSizeY / sizeY)

    floorGridX = math.floor(gridX)
    floorGridY = math.floor(gridY)

    fracX = gridX - floorGridX
    fracY = gridY - floorGridY

    # print(f"x: {x}")
    # print(f"y: {y}")
    # print(f"gridX: {gridX}")
    # print(f"gridY: {gridY}")

    # unit gradient vectors for the corners (vertices) of the grid space the sampled pixel falls within
    grad1, grad2, grad3, grad4 = (
        dirs[(floorGridY * gridSizeX) + floorGridX],
        dirs[(floorGridY * gridSizeX) + floorGridX + 1],
        dirs[((floorGridY + 1) * gridSizeX) + floorGridX],
        dirs[((floorGridY + 1) * gridSizeX) + floorGridX + 1],
    )

    # distance vectors pointing from each grid vertex to the position of the sampled pixel
    dist1, dist2, dist3, dist4 = (
        (gridX - floorGridX, gridY - floorGridY),
        (gridX - (floorGridX + 1), gridY - floorGridY),
        (gridX - floorGridX, gridY - (floorGridY + 1)),
        (gridX - (floorGridX + 1), gridY - (floorGridY + 1)),
    )

    # dot products of each gradient vector and it's respective distance vector to the sampled pixel
    dot1, dot2, dot3, dot4 = (
        (grad1[0] * dist1[0]) + (grad1[1] * dist1[1]),
        (grad2[0] * dist2[0]) + (grad2[1] * dist2[1]),
        (grad3[0] * dist3[0]) + (grad3[1] * dist3[1]),
        (grad4[0] * dist4[0]) + (grad4[1] * dist4[1]),
    )
    lowLerp = lerp(dot1, dot2, bettersmoothstep(fracX))
    highLerp = lerp(dot3, dot4, bettersmoothstep(fracX))
    noiseValue = lerp(lowLerp, highLerp, bettersmoothstep(fracY))
    return noiseValue


for x in range(0, sizeX):
    for y in range(0, sizeY):
        octaves = 10
        fbm = 0
        for octave in range(0, octaves + 1):
            fbm += perlin(
                x * (2**octave), y * (2**octave), dirs * (2**octave)
            ) * (0.5**octave)

        img.putpixel(xy=(x, y), value=int((fbm + 1) * 0.5 * 255))

img.show()
