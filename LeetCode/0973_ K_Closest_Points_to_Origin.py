from heapq import heappop, heappush
from typing import List, Tuple


class Solution:
    def closest_points(self, points: List[Tuple[float, float]], k: int) -> List[Tuple[float, float]]:
        """
        Finds the K points closest to the origin.

        The implementation pushes the points on a Heap with their key being the distance to the origin, then removes K elements from the heap.
        I chose to go with a more verbose implementation to show how it can be done, but alternatively one could do:

        >>> from heapq import nsmallest
        ... nsmallest(k, points, key=self.distance)
        """
        
        heap = []
        for point in points:
            heappush(heap, (self.distance(point), point))

        return [heappop(heap)[1] for _ in range(k)]

    def distance(self, point: Tuple[float, float]) -> float:
        """
        Pythagorean formula to get the distance to the origin.
        """
        
        return (point[0] ** 2 + point[1] ** 2) ** 0.5
