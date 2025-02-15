class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for i in range(1, n + 1):
            sq_str = str(i * i)
            if self.canPartition(sq_str, i, 0, {}):
                total += i * i
        return total

    def canPartition(self, s, target, idx, memo):
        if idx == len(s):
            return target == 0
        
        key = (idx, target)
        if key in memo:
            return memo[key]
       
        for j in range(idx + 1, len(s) + 1):
            num = int(s[idx:j])
            if num > target:
                if s[idx] != '0':
                    break
            if self.canPartition(s, target - num, j, memo):
                memo[key] = True
                return True
        
        memo[key] = False
        return False


