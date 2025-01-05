class Solution(object):
    def shiftingLetters(self, s, shifts):
        s = list(s)
        cum_shift = [0]*(len(s)+1)
        cum = 0
        for start, end, direc in shifts:
            if direc == 0:
                cum_shift[start] -= 1
                cum_shift[end+1] += 1
            else:
                cum_shift[start] += 1
                cum_shift[end+1] -= 1
        for i in range(len(s)):
            cum += cum_shift[i]
            s[i] = chr((ord(s[i]) - 97 + cum) % 26 + 97)
        return "".join(s)