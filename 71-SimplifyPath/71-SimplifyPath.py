# Last updated: 8/19/2025, 12:57:23 AM
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for token in path.split('/'):
            if token in ['', '.']:
                continue
            elif token == '..':
                if stack: stack.pop()
            else:
                stack.append(token)
        
        return '/' + '/'.join(stack)