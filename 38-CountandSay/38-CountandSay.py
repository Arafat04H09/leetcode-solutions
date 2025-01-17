class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"

        for i in range(1, n):
            nextS = ''

            cnt = 1
            cur = s[0]
            for idx in range(1, len(s)):
                if s[idx] == cur:
                    cnt += 1
                else:
                    nextS+= str(cnt) + cur
                    cur = s[idx]
                    cnt = 1
            nextS += str(cnt) + cur
            s = nextS

        return s