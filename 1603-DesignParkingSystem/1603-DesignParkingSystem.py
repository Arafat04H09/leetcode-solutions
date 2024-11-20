class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.m = defaultdict(int)
        self.m[1] += big
        self.m[2] += medium
        self.m[3] += small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.m[carType] > 0:
            self.m[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)