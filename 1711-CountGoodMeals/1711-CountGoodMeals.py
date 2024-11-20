class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        # keep track of powers of 2
        # have count 
        # defaultdict()

        powOf2 = [2 ** i for i in range(22)]
        count = 0 
        d = defaultdict(int)

        for value in deliciousness:
            
            for p in powOf2:
                if p - value in d:
                    count += d[p - value]
                    count %= ((10**9 + 7))
            
            d[value] += 1
        
        return count