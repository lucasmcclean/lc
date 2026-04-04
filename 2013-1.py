class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point):
        self.points[tuple(point)] += 1

    def count(self, point):
        count = 0

        x, y = point
        for (px, py), freq in self.points.items():
            if abs(px - x) == abs(py - y) and px != x:
                count += (
                    freq *
                    self.points.get((x, py), 0) *
                    self.points.get((px, y), 0)
                )

        return count
