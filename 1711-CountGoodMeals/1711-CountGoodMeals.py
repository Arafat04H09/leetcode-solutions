class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        m = defaultdict(int)
        c = 0
        pwOf2 = [2**i for i in range(22)]

        for d in deliciousness:
            for pw in pwOf2:
                c += m[pw - d]
            m[d] += 1

        return c % ((10**9) + 7)