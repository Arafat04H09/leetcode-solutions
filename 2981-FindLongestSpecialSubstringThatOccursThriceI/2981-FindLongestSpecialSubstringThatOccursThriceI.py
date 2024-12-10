class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = defaultdict(int)  
        max_len = 0 
        start = 0  

        for end in range(len(s)):
            if s[start] != s[end]:
                start = end
            
            for length in range(1, end - start + 2): 
                substring = s[end - length + 1:end + 1]
                m[substring] += 1

        for k, v in m.items():
            if v >= 3:
                max_len = max(max_len, len(k))
        
        return max_len if max_len > 0 else -1
