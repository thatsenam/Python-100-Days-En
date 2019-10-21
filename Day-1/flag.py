import turtle

pen = turtle.Turtle()
width = 100 * 2
height = 60 * 2


def draw_rect():
    pen.color('green')
    pen.penup()
    pen.setx(-200)
    pen.sety(200)
    pen.pendown()
    pen.begin_fill()
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.end_fill()


def draw_circle():
    pen.forward(width / 2)
    pen.right(90)
    pen.forward(height / 2)
    pen.right(90)
    pen.dot(60, 'red')
    pen.end_fill()


def done():
    turtle.penup()
    pen.penup()
    pen.home()
    turtle.done()
    turtle.mainloop()


def main():
    print(pen.pos())
    draw_rect()
    draw_circle()
    done()


if __name__ == '__main__':
    main()
