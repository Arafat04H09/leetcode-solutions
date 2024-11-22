class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temperature:
                oldIndex, _  = stack.pop()
                ans[oldIndex] = (index - oldIndex)
            
            stack.append((index, temperature))
        
        return ans