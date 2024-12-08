class Solution(object):
    def romanToInt(self, numeral):
        roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }

        prev  = 0
        s = 0
        cur = 0
        for i,n in enumerate(numeral):
            if i == 0:
                prev = roman.get(n)
                s += roman.get(n)
                continue
            cur = roman.get(n)
            s+= cur
            if prev < cur:
                s -= (2*prev)
            prev = cur
        
        return s