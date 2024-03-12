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

pen_size = 2 if iteration > 5 else 5 

t = turtle.Turtle()

print("Perhitungan dengan divide and conquer menggunakan warna merah")

for point in points:
    t.penup()
    t.goto(*point)
    t.dot(pen_size, "red")

print("Perhitungan dengan bruteforce menggunakan warna biru")

points = bezier_curve.bruteforce_quadratic(control_points)
for point in points:
    t.penup()
    t.goto(*point)
    t.dot(pen_size, "black")

turtle.done()