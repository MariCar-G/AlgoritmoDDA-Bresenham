def bresenham_algrithm(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xvars = []
    yvars = []

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        xvars.append(x0 + x*xx + y*yx)
        yvars.append(y0 + x*xy + y*yy)
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return xvars,yvars


if __name__ == '__main__':
    lista = bresenham_algrithm(0,0,0,10)
    print(lista)