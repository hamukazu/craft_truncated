import craftmath
import craftdraw
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import numpy as np

EDGE_LENGTH = 2 * cm
WITH_MERGIN = True
MARGIN_SIZE1 = 0.5 * cm
MARGIN_SIZE2 = 0.8 * cm
MARGIN_SIZE3 = 0.8 * cm
MARGIN_ANGLE1 = np.pi * 40 / 180
MARGIN_ANGLE2 = np.pi * 60 / 180
MARGIN_ANGLE3 = np.pi * 50 / 180


def part1(pdf, v1, v2, v3, partnum, pagenum):
    vs = craftmath.regular_polygon(3, v1, v2)
    vs = np.concatenate((vs, vs[0].reshape(1, 2)))
    craftdraw.polyline(pdf, vs)
    mvs = craftmath.margin(MARGIN_ANGLE1, MARGIN_SIZE1, vs[0], vs[2])
    craftdraw.polyline(pdf, mvs)
    vs2 = craftmath.regular_polygon(10, vs[2], vs[1])
    vs2 = np.concatenate((vs2, vs2[0].reshape(1, 2)))
    craftdraw.polyline(pdf, vs2)
    pdf.line(vs2[2, 0], vs2[2, 1], v3[0], v3[1])
    vs3 = craftmath.regular_polygon(3, vs2[5], vs2[4])
    vs3 = np.concatenate((vs3, vs3[0].reshape(1, 2)))
    craftdraw.polyline(pdf, vs3)
    if partnum % 2 == 0:
        mvs = craftmath.margin(MARGIN_ANGLE2, MARGIN_SIZE2, vs2[4], vs2[3])
        craftdraw.polyline(pdf, mvs)
        mvs = craftmath.margin(MARGIN_ANGLE2, MARGIN_SIZE2, vs3[2], vs3[1])
        craftdraw.polyline(pdf, mvs)
    if partnum in [0, 2]:
        mvs = craftmath.margin(MARGIN_ANGLE2, MARGIN_SIZE2, vs2[10], vs2[9])
        craftdraw.polyline(pdf, mvs)
        mvs = craftmath.margin(MARGIN_ANGLE3, MARGIN_SIZE3, vs2[9], vs2[8])
        craftdraw.polyline(pdf, mvs)
    if pagenum == 1:
        for i in range(3):
            if i == 1:
                ang = MARGIN_ANGLE3
                size = MARGIN_SIZE3
            else:
                ang = MARGIN_ANGLE2
                size = MARGIN_SIZE2
            mvs = craftmath.margin(ang, size, vs2[6 + i], vs2[5 + i])
            craftdraw.polyline(pdf, mvs)
        mvs = craftmath.margin(MARGIN_ANGLE2, MARGIN_SIZE2, vs3[0], vs3[2])
        craftdraw.polyline(pdf, mvs)


def page(pdf, width, height, pagenum):
    v1 = np.array([width / 2 - EDGE_LENGTH / 2, height / 2])
    v2 = np.array([width / 2 + EDGE_LENGTH / 2, height / 2])
    vs = craftmath.regular_polygon(10, v1, v2)
    vs = np.concatenate((vs, vs[0].reshape(1, 2)))
    craftdraw.polyline(pdf, vs)
    for i in range(5):
        part1(pdf, vs[i * 2 + 1], vs[i * 2], vs[(i * 2 - 1) % 10], i, pagenum)


def main():
    # Paper size (A4)
    width = 21.0 * cm
    height = 29.7 * cm

    pdf = canvas.Canvas("./trunc_dodecahedron.pdf")
    pdf.saveState()

    pdf.setAuthor("Kimikazu Kato")
    pdf.setTitle("Truncated Regular Icosahedron")

    page(pdf, width, height, 1)
    pdf.showPage()
    page(pdf, width, height, 2)

    pdf.saveState()
    pdf.save()


if __name__ == '__main__':
    main()
