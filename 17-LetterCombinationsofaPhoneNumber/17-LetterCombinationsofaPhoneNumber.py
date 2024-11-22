class Solution(object):
    def letterCombinations(self, digits):
        ans = []

        if not digits:
            return ans

        m = { '2' : "abc", '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(s, index):
            if index == len(digits):
                ans.append(s)
                return

            for ch in m[digits[index]]:
                backtrack(s + ch, index + 1)
        
        backtrack('', 0)

        return ans