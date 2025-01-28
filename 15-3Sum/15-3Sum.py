class Solution:
    def threeSum(self, nums):
        sol = set()
        nums.sort()

        if nums.count(0) >= 3:
            sol.add((0, 0, 0))

        splitIdx = bisect_left(nums, 0)
        negatives = nums[:splitIdx]
        positives = nums[splitIdx:]

        positiveSet = set(positives)
        negativeSet = set(negatives)

        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                target = -(negatives[i] + negatives[j])
                if target in positiveSet:
                    sol.add((negatives[i], negatives[j], target))

        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                target = -(positives[i] + positives[j])
                if target in negativeSet:
                    sol.add((positives[i], positives[j], target))

        return list(sol)
