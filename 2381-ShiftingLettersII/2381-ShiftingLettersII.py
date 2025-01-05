class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shiftEffects = [0] * (n + 1)  

        for start, end, direction in shifts:
            if direction == 1: 
                shiftEffects[start] += 1
                shiftEffects[end + 1] -= 1
            else:  
                shiftEffects[start] -= 1
                shiftEffects[end + 1] += 1

        cumulativeShift = 0
        for i in range(n):
            cumulativeShift += shiftEffects[i]
            shiftEffects[i] = cumulativeShift

        s = list(s)  
        for i in range(n):
            shift = shiftEffects[i] % 26  
            s[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))

        return ''.join(s) 