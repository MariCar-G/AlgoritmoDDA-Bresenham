import matplotlib.pyplot as plt

def dda_algrithm(x,y,x2,y2,cl):
    dx = abs(x2-x)
    dy = abs(y2-y)
    steps = 0
    if dx > dy:
        steps = dx
    else:
        steps = dy

    increment_x =float(dx / steps)
    increment_y =float(dy / steps)

    increment_x = round(increment_x,1)
    increment_y = round(increment_y,1)

    for i in range(0, int(steps + 1)):
        plt.plot(round(x),round(y),cl)
        x+= increment_x
        y+=increment_y
        print(x)
        print(y)

    plt.show()

def main():
    x=int(input("x1: "))
    y=int(input("y1: "))
    x2=int(input("x2: "))
    y2=int(input("y2: "))


    dda_algrithm(x,y, x2, y2,".g")

if __name__ == '__main__':
    main()
    


    