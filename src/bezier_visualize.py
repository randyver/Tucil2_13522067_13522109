import matplotlib.pyplot as plt
import bezier_curve
import time


def visualize(order: int, control_points: list[tuple[float, float]], iteration: int):   

    # Static visualization

    for point in control_points:
        plt.scatter(point[0], point[1], s=100, color="orange")

    start_time = time.time()

    result = bezier_curve.divide_and_conquer(order, control_points, iteration)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Waktu eksekusi Divide and Conquer: {execution_time} detik")

    for point in result:
        plt.scatter(point[0], point[1], s=30, color="red")

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Hasil titik-titik Divide and Conquer')
    plt.grid(True)
    plt.show()


def visualize_bruteforce(order: int, control_points: list[tuple[float, float]]):
    for point in control_points:
        plt.scatter(point[0], point[1], s=100, color="orange")

    start_time = time.time()

    result = bezier_curve.bruteforce_general(order, control_points)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Waktu eksekusi Bruteforce: {execution_time} detik")

    for point in result:
        plt.scatter(point[0], point[1], s=5, color="red")
    
    plt.grid(True)
    plt.show()

