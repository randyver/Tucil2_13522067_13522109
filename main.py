import turtle
import bezier_curve

order = int(input("Masukkan order kurva n (1 untuk linier, 2 untuk quadratic, dst) "))

control_points: list[tuple[float, float]] = []
print(f"Masukkan {order + 1} titik: P_0, ..., P_{order}")
for i in range(order + 1):
    point = map(float, input().split())
    control_points.append(tuple(point))

print("Control points:", control_points)

iteration = int(input("Masukkan jumlah iterasi "))

points = bezier_curve.general(order, control_points, iteration)

def draw_point(x, y):
    t.penup()
    t.goto(x, y)
    t.dot(5)

t = turtle.Turtle()

for point in points:
    draw_point(*point)

turtle.done()