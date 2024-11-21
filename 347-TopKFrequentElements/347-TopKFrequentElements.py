class Solution:
    def topKFrequent(self, nums, k):
        bucket, res = [[] for _ in range(len(nums) + 1)], []
        for a, b in collections.Counter(nums).items():
            bucket[b].append(a)
        for l in bucket[::-1]:
            if len(l): res += l
            if len(res) >= k: return res[ : k]