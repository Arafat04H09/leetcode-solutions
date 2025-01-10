class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        ans = []
        totalB = Counter()

        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                totalB[char] = max(totalB[char], count)  
        
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= totalB[char] for char in totalB):
                ans.append(word)  

        return ans
