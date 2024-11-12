class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = deque([])
        reverse = list(s)
        for i, ch in enumerate(s):
            if ch in 'aieouAIEOU':
                vowels.append(i)
        
        while len(vowels) > 1:
            leftIndex = vowels.popleft()
            rightIndex = vowels.pop()

            reverse[leftIndex], reverse[rightIndex] = reverse[rightIndex], reverse[leftIndex]
        
        return ''.join(reverse)