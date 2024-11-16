class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        b = 10 ** ((intLength - 1) /2)
        ans = [q - 1 + b for q in queries]

        for i, a in enumerate(ans):
            a = str(a) + str(a)[- 1 -intLength%2:: -1]
            ans[i] = int(a) if len(a) == intLength else -1
        
        return ans