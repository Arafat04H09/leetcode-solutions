class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        maxFreq = 0
        start = 0

        for end, ch in enumerate(s): #unpack the index, value pairs as tuples with an iterator 
            freq[ch] += 1
            maxFreq = max(maxFreq, freq[ch]) #updating the max frequency

            if end - start + 1 - k > maxFreq:
                if s[start] == maxFreq:
                    maxFreq -= 1
                freq[s[start]] -= 1
                start += 1
            
        return end - start + 1
            

        
        