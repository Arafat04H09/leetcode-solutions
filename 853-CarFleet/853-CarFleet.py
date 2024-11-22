class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for pos, vel in cars:
            time = float(target - pos)/vel
            
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
