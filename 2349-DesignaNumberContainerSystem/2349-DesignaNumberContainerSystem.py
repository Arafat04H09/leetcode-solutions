class NumberContainers(object):

    def __init__(self):
        self.indexForNums = defaultdict(list)  # Min-heaps storing indices for each number
        self.nums = {}  # Maps index -> number
        self.valid = {}  # Validity tracking for lazy deletion

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.nums:
            old_number = self.nums[index]
            if old_number == number:
                return  # No change needed
            self.valid[(old_number, index)] = False  # Mark old (num, index) as invalid

        # Store new number at the index
        self.nums[index] = number
        heapq.heappush(self.indexForNums[number], index)
        self.valid[(number, index)] = True  # Mark as valid

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.indexForNums or not self.indexForNums[number]:
            return -1

        # Ensure we return the smallest valid index
        while self.indexForNums[number]:
            smallest_index = self.indexForNums[number][0]
            if self.valid.get((number, smallest_index), False):
                return smallest_index
            heapq.heappop(self.indexForNums[number])  # Remove invalid elements

        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)