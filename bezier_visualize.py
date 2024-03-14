from line import Line
import copy
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.animation import FuncAnimation
from itertools import cycle
import bezier_curve
# import bezier_animation


def visualize(order: int, control_points: list[tuple[float, float]], iteration: int):   

    # Static visualization

    for point in control_points:
        plt.scatter(point[0], point[1], s=100, color="orange")

    result = bezier_curve.approximate(order, control_points, iteration)
    for point in result:
        plt.scatter(point[0], point[1], s=30, color="red")

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Hasil titik-titik Divide and Conquer')
    plt.grid(True)
    plt.show()

    # Moving animation (Belum Selesai)

    # animation = FuncAnimation(fig[1], bezier_animation.update_lines)


def visualize_bruteforce(order: int, control_points: list[tuple[float, float]]):
    for point in control_points:
        plt.scatter(point[0], point[1], s=100, color="orange")

    result = bezier_curve.bruteforce_general(order, control_points)
    for point in result:
        plt.scatter(point[0], point[1], s=5, color="red")
    
    plt.grid(True)
    plt.show()

