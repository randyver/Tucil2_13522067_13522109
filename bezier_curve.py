from line import Line
import copy

def approximate_from_lines(control_lines: list[Line], iteration: int, weight: float) -> list[tuple[float, float]]:
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
        left_result: list[tuple[float, float]] = approximate_from_lines(original_control_lines, iteration - 1, weight / 2)
        right_result: list[tuple[float, float]] = approximate_from_lines(original_control_lines, iteration - 1, 1 - weight / 2)
        return left_result + current_result + right_result


def approximate(order: int, control_points: list[tuple[float, float]], iteration: int) -> list[tuple[float, float]]:
    control_lines: list[Line] = []
    for i in range(len(control_points) - 1):
        control_lines.append(Line(control_points[i], control_points[i + 1]))
    return approximate_from_lines(control_lines, iteration, 0.5)


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

def bruteforce_general(order: int, control_points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if order == 2:
        return bruteforce_quadratic(control_points)
    print("Order selain 2 belum diimplementasi")
    return [(0.0, 0.0)]
