class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        m = defaultdict(int)

        for ch in sentence:
            m[ch] += 1

        return len(m) == 26