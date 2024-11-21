class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = defaultdict(list)
        
        for s in strs:
            m[tuple(sorted(s))].append(s)
        
        return [list(s) for s in m.values()]