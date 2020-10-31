class Solution(object):
    def destCity(self, paths):
        origin, destination = [], []
        for p in paths:
            origin.append(p[0])
            destination.append(p[1])
            
        for d in destination:
            if d not in origin :
                return d