class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
            
        ans = []

        m = {"2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        }

        def backtrack(index, combination):
            if index == len(digits):
                ans.append(combination)
                return
            
            for nextLetter in m[digits[index]]:
                backtrack(index + 1, combination + nextLetter)
        
        backtrack(0, "")
        return ans