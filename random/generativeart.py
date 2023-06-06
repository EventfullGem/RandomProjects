import turtle

CANVAS_SIZE = 500
DENSITY = 12

t = turtle.Turtle()
s = turtle.Screen()
s.setup(CANVAS_SIZE, CANVAS_SIZE)

t.penup()

def draw_line(row, col):
        lower_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
        upper_right = (
            ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
            ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
        )

        t.goto(lower_left)
        t.pendown()
        t.goto(upper_right)
        t.penup()


for row in range(DENSITY):
    for col in range(DENSITY):
        draw_line(row, col)

