class Solution(object):
    def lengthOfLongestSubstring(self, s):
        holder = set()
        start = 0 
        maxL = 0

        for end in range(len(s)):
            while s[end] in holder:
                holder.remove(s[start])
                start += 1
            
            holder.add(s[end])
            maxL = max(maxL, end - start + 1)
        
        return maxL
