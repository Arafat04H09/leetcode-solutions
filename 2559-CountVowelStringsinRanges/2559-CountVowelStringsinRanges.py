class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        pre = [0] * (len(words) + 1)
        for i in range(len(words)):
            pre[i + 1] = pre[i] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)
        
        ans = []
        for start, end in queries:
            ans.append(pre[end + 1] - pre[start])
        
        return ans
