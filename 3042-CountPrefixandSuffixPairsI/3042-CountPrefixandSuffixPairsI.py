class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                prefix = words[i]
                suffix = words[i]
                word = words[j]

                if len(suffix) > word or len(prefix) > word:
                    continue
                
                if word.startswith(prefix) and word.endswith(suffix):
                    count += 1

        return count
