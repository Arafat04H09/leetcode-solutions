class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        nums.sort()
        n = len(nums)

        if nums.count(0) >= 3:
            sol.add((0, 0, 0))

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    sol.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        
        return list(sol)
