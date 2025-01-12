class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}

        def isSpecial(st):
            if st in dic:
                return dic[st]

            count = 0 
            for ch in st:
                if ch == '1':
                    count += 1
                else:
                    count -= 1

                if count < 0:
                    dic[st] = False
                    return False

            dic[st] = (count == 0)
            return dic[st]

        def backtrack(s):
            if not s:  
                return ""

            count = 0
            start = 0
            substrings = []

            for i, ch in enumerate(s):
                count += 1 if ch == '1' else -1
                if count == 0: 
                    inner = backtrack(s[start + 1:i])
                    substrings.append('1' + inner + '0')
                    start = i + 1

            substrings.sort(reverse=True)

            return ''.join(substrings)

        return backtrack(s)