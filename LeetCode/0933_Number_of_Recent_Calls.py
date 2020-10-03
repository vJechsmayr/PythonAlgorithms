class RecentCounter:

    def __init__(self):
        self.p = []

    def ping(self, t: int) -> int:
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.pop(0)
        return len(self.p)