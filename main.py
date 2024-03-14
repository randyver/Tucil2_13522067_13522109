import bezier_visualize
from draw_utils import draw_lines, draw_points
from line import Line

order = int(input("Masukkan order kurva n (1 untuk linier, 2 untuk quadratic, dst): "))

control_points: list[tuple[float, float]] = []
print(f"Masukkan {order + 1} titik: P_0, ..., P_{order}:")
for i in range(order + 1):
    point = map(float, input().split())
    control_points.append(tuple(point))

print("Control points:", control_points)

iteration = int(input("Masukkan jumlah iterasi: "))

print(
"""Pilihan pembuatan kurva Bezier
1. Divide and Conquer
2. Bruteforce""")

option = int(input())
if option not in [1, 2]:
    print("Opsi tidak valid")
    exit(0)

if option == 1:
    bezier_visualize.visualize(order, control_points, iteration)
else:
    bezier_visualize.visualize_bruteforce(order, control_points)
