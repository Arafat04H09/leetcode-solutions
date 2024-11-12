class Solution(object):
    def maximumBeauty(self, items, queries):
        queriesPair = [(query, i) for i, query in enumerate(queries)]

        queriesPair.sort(key=lambda x: x[0])
        items.sort(key=lambda x: x[0])

        ans = [0] * len(queries)
        maxBeauty = 0
        itemIndex = 0

        for queryPrice, originalIndex in queriesPair:
            while itemIndex < len(items) and items[itemIndex][0] <= queryPrice:
                maxBeauty = max(maxBeauty, items[itemIndex][1])
                itemIndex += 1
            ans[originalIndex] = maxBeauty

        return ans