import turtle

avi = turtle.Turtle()
avi.getscreen().bgcolor("#494b52")
avi.color("yellow")
avi.speed(10)
def star(turtle, size):
    if size <=2:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)


star(avi, 270)
turtle.done()
