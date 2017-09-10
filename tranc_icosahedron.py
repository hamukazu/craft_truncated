import craftmath
import craftdraw
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import numpy as np

EDGE_LENGTH = 2 * cm
WITH_MERGIN = True
MARGIN_SIZE = 0.6 * cm
MARGIN_ANGLE = np.pi * 50 / 180


def part1(pdf, v1, v2, pagenum):
    vs = craftmath.regular_polygon(5, v1, v2)
    vs = np.c_[vs[1:].T, vs[0]].T
    craftdraw.polyline(pdf, vs)
    mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[1], vs[0])
    craftdraw.polyline(pdf, mvs)
    mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[2], vs[1])
    craftdraw.polyline(pdf, mvs)
    mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[4], vs[3])
    craftdraw.polyline(pdf, mvs)
    vs = craftmath.regular_polygon(6, vs[3], vs[2])
    vs = np.c_[vs[1:].T, vs[0]].T
    craftdraw.polyline(pdf, vs)
    for i in range(3):
        if pagenum != 2 or i != 2:
            mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[1 + i], vs[i])
            craftdraw.polyline(pdf, mvs)
    vs2 = craftmath.regular_polygon(5, vs[4], vs[3])
    vs2 = np.c_[vs2[1:].T, vs2[0]].T
    craftdraw.polyline(pdf, vs2)
    vs3 = craftmath.regular_polygon(6, vs2[3], vs2[2])
    vs3 = np.c_[vs3[1:].T, vs3[0]].T
    craftdraw.polyline(pdf, vs3)
    for i in range(2):
        if pagenum != 1 or i != 0:
            mvs = craftmath.margin(
                MARGIN_ANGLE, MARGIN_SIZE, vs3[1 + i], vs3[i])
            craftdraw.polyline(pdf, mvs)
    vs4 = craftmath.regular_polygon(6, vs3[5], vs3[4])
    vs4 = np.c_[vs4[1:].T, vs4[0]].T
    craftdraw.polyline(pdf, vs4)
    mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[5], vs[4])
    mvs[1, :] = vs4[4, :]
    craftdraw.polyline(pdf, mvs)
    v = 0.8 * vs4[4] + 0.2 * vs4[5]
    pdf.line(vs[4, 0], vs[4, 1], v[0], v[1])


def page(pdf, width, height, pagenum):
    v1 = np.array([width / 2 - EDGE_LENGTH / 2, height / 2])
    v2 = np.array([width / 2 + EDGE_LENGTH / 2, height / 2])

    vs = craftmath.regular_polygon(6, v1, v2)
    vs = np.c_[vs.T, vs[0, :]].T
    craftdraw.polyline(pdf, vs)
    mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[2], vs[1])
    craftdraw.polyline(pdf, mvs)
    mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[4], vs[3])
    craftdraw.polyline(pdf, mvs)
    mvs = craftmath.margin(MARGIN_ANGLE, MARGIN_SIZE, vs[0], vs[5])
    craftdraw.polyline(pdf, mvs)
    part1(pdf, vs[1], vs[0], pagenum)
    part1(pdf, vs[3], vs[2], pagenum)
    part1(pdf, vs[5], vs[4], pagenum)


def main():
    # Paper size (A4)
    width = 21.0 * cm
    height = 29.7 * cm

    pdf = canvas.Canvas("./trunc_icosahedron.pdf")
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
