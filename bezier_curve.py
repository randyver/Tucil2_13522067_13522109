from point import midpoint, times
from draw_utils import draw_point, draw_line, draw_lines, draw_points
import turtle


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

def quadratic_with_animation(t: turtle.Turtle, control_points: list[tuple[float, float]], iteration):
    current_points: list[tuple[float, float]] = control_points
    t.color("green")
    for point in current_points:
        draw_point(t, *point)

    t.color("black")
    draw_lines(t, current_points)
    
    for _ in range(iteration):
        t.color("green")
        midpoints: list[tuple[float, float]] = []
        midpoints.append(current_points[0])

        for i in range(1, len(current_points)):
            midpoints.append(midpoint(current_points[i], current_points[i - 1]))
        midpoints.append(current_points[-1])
        draw_points(t, midpoints)

        current_points: list[tuple[float, float]] = []
        result: list[tuple[float, float]] = []
        current_points.append(midpoints[0])
        current_points.append(midpoints[1])
        result.append(midpoints[0])

        t.color("black")
        for i in range(2, len(midpoints) - 1):
            result.append(midpoint(midpoints[i], midpoints[i - 1]))
            current_points.append(midpoint(midpoints[i], midpoints[i - 1]))
            draw_line(t, midpoints[i], midpoints[i - 1])
            current_points.append(midpoints[i])
        
        current_points.append(midpoints[-1])
        result.append(midpoints[-1])

        t.color("green")
        draw_points(t, current_points)


    t.color("blue")
    for point in result:
        draw_point(t, *point)
    return result

def bruteforce_quadratic(control_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    result: list[tuple[float, float]] = []
    density = 300
    t = 0
    for _ in range(density + 1):
        # B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2
        first = times(control_points[0], (1 - t) ** 2)
        second = times(control_points[1], 2 * (1-t) * t)
        third = times(control_points[2], t * t)
        result.append((first[0] + second[0] + third[0], first[1] + second[1] + third[1]))
        t += 1 / density

    return result

def bruteforce_general(order, control_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if order == 2:
        return bruteforce_quadratic(control_points)
    print("Order selain 2 belum diimplementasi")
    return [(0.0, 0.0)]

def general(order: int, control_points: list[tuple[float, float]], iteration) -> list[tuple[float, float]]:
    if order == 2:
        return quadratic(control_points, iteration)
    print("Order selain 2 belum diimplementasi")
    return [(0.0, 0.0)]

def general_with_animation(t, order: int, control_points: list[tuple[float, float]], iteration) -> list[tuple[float, float]]:
    if order == 2:
        return quadratic_with_animation(t, control_points, iteration)
    print("Order selain 2 belum diimplementasi")
    return [(0.0, 0.0)]
