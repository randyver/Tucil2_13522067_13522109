import turtle

def draw_point(t: turtle.Turtle, x, y, size=8):
    t.penup()
    t.goto(x, y)
    t.dot(size)

def draw_points(t: turtle.Turtle, points: list[tuple[float, float]], size=8):
    t.penup()
    for point in points:
        t.goto(point)
        t.dot(size)

def draw_line(t: turtle.Turtle, start_point, end_point):
    t.penup()
    t.goto(start_point)
    t.pendown()
    t.goto(end_point)

def draw_lines(t: turtle.Turtle, points: list[tuple[float, float]]):
    t.penup()
    t.goto(points[0])
    t.pendown()
    for point in points[1:]:
        t.goto(point)
        