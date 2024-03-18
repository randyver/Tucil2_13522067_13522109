from line import Line
from math import comb
import copy

def divide_and_conquer_from_lines(control_lines: list[Line], iteration: int, weight: float) -> list[tuple[float, float]]:
    original_control_lines = copy.deepcopy(control_lines)

    while len(control_lines) > 1:
        new_lines: list[Line] = []
        for i in range(len(control_lines) - 1):
            new_lines.append(Line(control_lines[i].weight(weight), control_lines[i + 1].weight(weight)))
        control_lines = new_lines
    
    current_result = [control_lines[0].weight(weight)]
    
    if iteration == 1:
        return current_result
    else:
        first_result: list[tuple[float, float]] = divide_and_conquer_from_lines(original_control_lines, iteration - 1, weight / 2)
        second_result: list[tuple[float, float]] = divide_and_conquer_from_lines(original_control_lines, iteration - 1, 1 - weight / 2)
        return first_result + current_result + second_result

def divide_and_conquer(order: int, control_points: list[tuple[float, float]], iteration: int) -> list[tuple[float, float]]:
    # if order == 2:
        # return quadratic_divide_and_conquer(control_points, iteration)
    
    control_lines: list[Line] = []
    for i in range(len(control_points) - 1):
        control_lines.append(Line(control_points[i], control_points[i + 1]))
    return divide_and_conquer_from_lines(control_lines, iteration, 0.5)


def quadratic_divide_and_conquer(control_points: list[tuple[float, float]], iteration) -> list[tuple[float, float]]:
    def midpoint(first: tuple[float, float], second: tuple[float, float]):
        return (first[0] + second[0]) / 2, (first[1] + second[1]) / 2

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

def bruteforce_general(order: int, control_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    result: list[tuple[float, float]] = []
    density = 300
    n = len(control_points)
    
    for d in range(density + 1):
        t = d / density
        x, y = 0, 0
        
        # basis
        basis_pow = (1 - t) ** (n - 1)
        
        for i, (px, py) in enumerate(control_points):
            
            # bernstein poly
            if i == 0:
                b = basis_pow
            elif t == 1:
                if i < (n-1):
                    b = 0
                else:
                    b = 1
            else:
                b *= t / (1 - t) * (n - i) / i
            
            x += px * b
            y += py * b
            
            if t != 1:
                basis_pow /= (1 - t)
            
        result.append((x, y))

    return result

def bruteforce_quadratic(control_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    result: list[tuple[float, float]] = []
    density = 300
    t = 0
    for _ in range(density + 1):
        # B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2
        first = control_points[0][0] * (1 - t) ** 2, control_points[0][1] * (1 - t) ** 2
        second = control_points[1][0] * 2 * (1-t) * t, control_points[1][1] * 2 * (1-t) * t
        third = control_points[2][0] * t * t, control_points[2][1] * t * t
        result.append((first[0] + second[0] + third[0], first[1] + second[1] + third[1]))
        t += 1 / density

    return result

