import turtle
import bezier_curve
from draw_utils import draw_lines

order = int(input("Masukkan order kurva n (1 untuk linier, 2 untuk quadratic, dst) "))

control_points: list[tuple[float, float]] = []
print(f"Masukkan {order + 1} titik: P_0, ..., P_{order}")
for i in range(order + 1):
    point = map(float, input().split())
    control_points.append(tuple(point))

print("Control points:", control_points)

iteration = int(input("Masukkan jumlah iterasi "))

with_animation = input("Apakah mau dengan animasi? (y/n) ").strip().lower()
with_bruteforce = input("Apakah mau dengan bruteforce? (y/n) ").strip().lower()

with_animation = True if with_animation == 'y' else False if with_animation == 'n' else None
with_bruteforce = True if with_bruteforce == 'y' else False if with_bruteforce == 'n' else None

if with_animation == None or with_bruteforce == None:
    print("Input tidak valid", with_animation, with_bruteforce)
    exit(0)

t = turtle.Turtle()

print("Perhitungan dengan Divide and Conquer menggunakan warna ungu")
if with_animation:
    t.speed(1)
    points = bezier_curve.general_with_animation(t, order, control_points, iteration)
    t.color("purple")
    draw_lines(t, points)
else:
    t.speed(0)
    points = bezier_curve.general(order, control_points, iteration)
    t.color("purple")
    draw_lines(t, points)

t.speed(0)

if with_bruteforce:
    print("Perhitungan dengan bruteforce menggunakan warna oranye")
    t.color("orange")
    points = bezier_curve.bruteforce_general(order, control_points)
    draw_lines(t, points)


turtle.done()