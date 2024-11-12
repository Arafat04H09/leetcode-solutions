class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        curIndex = 0
        length = len(s) 

        while curIndex < length:
            #skip over until you reach a letter
            while curIndex < length and not s[curIndex].isalnum():
                curIndex += 1
            
            #you have reached a letter or index > length
            word = ''
            while curIndex < length and s[curIndex].isalnum():
                word += s[curIndex]
                curIndex += 1
            
            #insert word to beginning of sentence
            ans = ' '+ word + ans
        
        return ans.strip()