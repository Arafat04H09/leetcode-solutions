class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        l1 = len(a) - 1
        l2 = len(b) - 1
        ans = ''    
        s = 0

        while l1 > -1 or l2 > -1 or carry:
            digita = int(a[l1]) if l1 > -1 else 0
            digitb = int(b[l2]) if l2 > -1 else 0
            total = digita + digitb + carry

            ans = str(total % 2) + ans
            carry = total//2

            l1-= 1
            l2-= 1
        
        return ans


            
