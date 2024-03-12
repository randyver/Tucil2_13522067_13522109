def midpoint(first: tuple[float, float], second: tuple[float, float]):
    return (first[0] + second[0]) / 2, (first[1] + second[1]) / 2


def quadratic(control_points: list[tuple[float, float]], iteration) -> list[tuple[float, float]]:
    current_points: list[tuple[float, float]] = control_points

    for _ in range(iteration):
        midpoints: list[tuple[float, float]] = []
        midpoints.append(current_points[0])

        for i in range(1, len(current_points)):
            midpoints.append(midpoint(current_points[i], current_points[i - 1]))
        midpoints.append(current_points[-1])

        current_points: list[tuple[float, float]] = []
        result: list[tuple[float, float]] = []
        current_points.append(midpoints[0])
        current_points.append(midpoints[1])
        result.append(midpoints[0])

        for i in range(2, len(midpoints) - 1):
            result.append(midpoint(midpoints[i], midpoints[i - 1]))
            current_points.append(midpoint(midpoints[i], midpoints[i - 1]))
            current_points.append(midpoints[i])
        
        current_points.append(midpoints[-1])
        result.append(midpoints[-1])
        
    return result

def general(order: int, control_points: list[tuple[float, float]], iteration) -> list[tuple[float, float]]:
    if order == 2:
        return quadratic(control_points, iteration)
    print("Order selain 2 belum diimplementasi")
    return [(0.0, 0.0)]
