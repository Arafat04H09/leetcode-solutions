class Solution(object):
    def lengthOfLongestSubstring(self, s):
        currentCharacters = set()
        longest = 0
        start = 0

        for end , ch in enumerate(s):
            while ch in currentCharacters:
                currentCharacters.remove(s[start])
                start += 1
            
            currentCharacters.add(ch)
            longest = max(longest, end - start + 1)
        
        return longest

