class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {')': '(', '}': '{', ']': '['}  

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or (ch in matching and stack[-1] != matching[ch]):
                    return False
                stack.pop() 

        return len(stack) == 0 