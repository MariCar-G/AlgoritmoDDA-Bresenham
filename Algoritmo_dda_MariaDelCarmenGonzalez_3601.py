def dda_algrithm(x,y,x2,y2):
    dx = abs(x2-x)
    dy = abs(y2-y)
    steps = 0
    if dx>dy:
        steps = dx
    else:
        steps = dy

    increment_x = dx / steps     
    increment_y = dy / steps

    p1 = x
    p2 = y
    x_vars=[p1]
    y_vars=[p2]
    for i in range(steps):
        if x2 < x:
            p1 -= increment_x
        else:
            p1 += increment_x
        n = round(p1)
        x_vars.append(n)
        if y2>y:
            p2 += increment_y
        else:
            p2 -= increment_y 
        n = round(p2)
        y_vars.append(n)
    return x_vars,y_vars
