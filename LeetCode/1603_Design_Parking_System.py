class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._limits = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        self._limits[carType - 1] -= 1
        if self._limits[carType - 1] < 0:
            return False
        return True
