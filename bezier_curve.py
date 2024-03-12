def quadratic(control_points: list[tuple[float, float]], iteration) -> list[tuple[float, float]]:
    pass


def general(order: int, control_points: list[tuple[float, float]], iteration) -> list[tuple[float, float]]:
    if order == 2:
        return quadratic(control_points, iteration)
    print("Order selain 2 belum diimplementasi")
    return [(0.0, 0.0)]
