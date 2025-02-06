class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product[nums[i] * nums[j]] += 1
        
        res = 0 

        for v in product.values():
            res += (v * (v - 1))//2 * 8
        
        return res
        