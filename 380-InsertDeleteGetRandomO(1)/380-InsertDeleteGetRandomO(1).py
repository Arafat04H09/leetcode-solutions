class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_idx = {}  
        self.values = [] 
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_idx:
            return False
        
        idx_to_remove = self.val_to_idx[val]
        
        last_val = self.values[-1]
        self.values[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove
        
        self.values.pop()
        del self.val_to_idx[val]
        
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.values)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()