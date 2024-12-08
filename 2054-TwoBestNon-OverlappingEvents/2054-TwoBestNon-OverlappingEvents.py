class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        max_sum = -inf
        min_heap, prev_max = [], 0
        for s, e, v in events:
            while min_heap and min_heap[0][0] < s:
                prev_max = max(prev_max, heapq.heappop(min_heap)[1])
            max_sum = max(max_sum, v + prev_max)
            heapq.heappush(min_heap, (e, v))
        return max_sum