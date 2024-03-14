class Line:
    def __init__(self, start: tuple[float, float], end: tuple[float, float]):
        self.start = start
        self.end = end
    def midpoint(self) -> tuple[float, float]:
        return (self.start[0] + self.end[0]) / 2, (self.start[1] + self.end[1]) / 2
    
    def weight(self, weight: float) -> tuple[float, float]:
        return (1 - weight) * self.start[0] + weight * self.end[0], (1 - weight) * self.start[1] + weight * self.end[1]
    def __str__(self) -> str:
        return self.start.__str__() + "," + self.end.__str__()