# Program ini hanya untuk animasi saja

from line import Line
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Draw:

    # t= 0
    def __init__(self, control_points: list[tuple[float, float]]):
        self.order = len(control_points) - 1
        self.line_tree: list[list[Line]] = []
        self.cur_t = 0
        
        lines: list[Line] = []
        for i in range(1, len(control_points)):
            lines.append(Line(control_points[i - 1], control_points[i]))
        self.line_tree.append(lines)

        for i in range(self.order - 1):
            lines: list[Line] = []
            for j in range(self.order - i - 1):
                start_point = self.line_tree[i][j].weight(0)
                end_point = self.line_tree[i][j + 1].weight(0)
                lines.append(Line(start_point, end_point))
            self.line_tree.append(lines)
        
        
    def update(self, t: float) -> tuple[float, float]:
        if t >= 1:
            return None
        for i in range(1, self.order):
            for j in range(self.order - i):
                start_point = self.line_tree[i - 1][j].weight(t)
                end_point = self.line_tree[i - 1][j + 1].weight(t)

                self.line_tree[i][j].start = start_point
                self.line_tree[i][j].end = end_point
        return self.line_tree[self.order - 1][0].weight(t)



print("---------------------------------------------------------------------------------------")
title = """
██████╗░███████╗███████╗██╗███████╗██████╗░  ░█████╗░██╗░░░██╗██████╗░██╗░░░██╗███████╗
██╔══██╗██╔════╝╚════██║██║██╔════╝██╔══██╗  ██╔══██╗██║░░░██║██╔══██╗██║░░░██║██╔════╝
██████╦╝█████╗░░░░███╔═╝██║█████╗░░██████╔╝  ██║░░╚═╝██║░░░██║██████╔╝╚██╗░██╔╝█████╗░░
██╔══██╗██╔══╝░░██╔══╝░░██║██╔══╝░░██╔══██╗  ██║░░██╗██║░░░██║██╔══██╗░╚████╔╝░██╔══╝░░
██████╦╝███████╗███████╗██║███████╗██║░░██║  ╚█████╔╝╚██████╔╝██║░░██║░░╚██╔╝░░███████╗
╚═════╝░╚══════╝╚══════╝╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
"""
print(title)
print("---------------------------------------------------------------------------------------")


order = int(input("Masukkan order kurva n (1 untuk linier, 2 untuk quadratic, dst): "))

control_points: list[tuple[float, float]] = []
print(f"Masukkan {order + 1} titik kontrol (P_0, ..., P_{order}):")
for i in range(order + 1):
    point = map(float, input().split())
    control_points.append(tuple(point))

control_points_str = ', '.join([f'({x}, {y})' for x, y in control_points])
print("Titik kontrol:", control_points_str)


d = Draw(control_points)


def update_lines(frame):
    try:
        lines: list[Line] = []
        for i in d.line_tree:
            for j in i:
                lines.append(j)
        points.append( d.update(d.cur_t))
        d.cur_t += 0.01

        ax.clear()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        

        for point in points:
            ax.scatter(*point, color="black")

        for line in lines:
            x_values = [line.start[0], line.end[0]]
            y_values = [line.start[1], line.end[1]]
            ax.plot(x_values, y_values)
    except:
        pass

points: list[tuple[float, float]] = []

fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of Lines')
plt.grid(True)

ani = FuncAnimation(fig, update_lines)

plt.show()
