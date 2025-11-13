import math
from random import Random, random

import matplotlib.pyplot as plt
random = Random()
# for x in range(0, sizeX):
#     for y in range(0, sizeY):
#         gridX = x / 10
#         gridY = y / 10
#         minGradientX = math.floor(gridX)
#         minGradientY = math.floor(gridY)
#         maxGradientX = minGradientX + 1
#         maxGradientY = minGradientY + 1
#
#         upperGradVec1, upperGradVec2 = (
#             dirs[int((maxGradientY * (sizeX / 10))) + minGradientX],
#             dirs[int((maxGradientY * (sizeX / 10))) + maxGradientX],
#         )
#         lowerGradVec1, lowerGradVec2 = (
#             dirs[int((minGradientY * (sizeX / 10))) + minGradientX],
#             dirs[int((minGradientY * (sizeX / 10))) + maxGradientX],
#         )
#
#         upperSampleVec1, upperSampleVec2 = (
#             gridX - minGradientX,
#             gridY - maxGradientY,
#         ), (gridX - maxGradientX, gridY - maxGradientY)
#         lowerSampleVec1, lowerSampleVec2 = (
#             gridX - minGradientX,
#             gridY - minGradientY,
#         ), (gridX - maxGradientX, gridY - minGradientY)
#
#         upperDot1, upperDot2 = (
#             upperGradVec1[0] * upperSampleVec1[0]
#             + upperGradVec1[1] * upperSampleVec1[1],
#             upperGradVec2[0] * upperSampleVec2[0]
#             + upperGradVec2[1] * upperSampleVec2[1],
#         )
#
#         lowerDot1, lowerDot2 = (
#             lowerGradVec1[0] * lowerSampleVec1[0]
#             + lowerGradVec1[1] * lowerSampleVec1[1],
#             lowerGradVec2[0] * lowerSampleVec2[0]
#             + lowerGradVec2[1] * lowerSampleVec2[1],
#         )
#
#         upperLerp = upperDot1 + (gridX - minGradientX) * (upperDot2 - upperDot1)
#         lowerLerp = lowerDot1 + (gridX - minGradientX) * (lowerDot2 - lowerDot1)
#
#         noiseValue = upperLerp + (gridY - minGradientY) * (lowerLerp - upperLerp)
#         print(noiseValue)
#         img.putpixel(xy=(x, y), value=int((noiseValue + 1) * 0.5 * 255))


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
