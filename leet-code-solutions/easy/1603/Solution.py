class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._big = big
        self._medium = medium
        self._small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self._big > 0:
            self._big -= 1
            return True
        elif carType == 2 and self._medium > 0:
            self._medium -= 1
            return True
        elif carType == 3 and self._small > 0:
            self._small -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)