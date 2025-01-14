class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        seen = set()
        common = 0
        C = [0] * len(A)

        for i in range(len(A)):
            if A[i] in seen:
                common += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                common += 1
            else:
                seen.add(B[i])
            
            C[i] = common
        
        return C
