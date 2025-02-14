class ProductOfNumbers(object):

    def __init__(self):
        self.nums = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.nums = []
        else:
            self.nums.append(num * self.nums[-1] if len(self.nums) > 0 else num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > len(self.nums):
            return 0
        if k == len(self.nums):
            return self.nums[-1]
        return self.nums[-1] // self.nums[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)