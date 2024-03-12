def midpoint(first: tuple[float, float], second: tuple[float, float]) -> tuple[float, float]:
    return (first[0] + second[0]) / 2, (first[1] + second[1]) / 2

def times(point: tuple[float, float], factor: float) -> tuple[float, float]:
    return point[0] * factor, point[1] * factor