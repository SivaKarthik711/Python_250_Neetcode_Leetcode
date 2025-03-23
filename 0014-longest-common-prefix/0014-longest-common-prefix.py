class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Sort the array
        strs.sort()

        first, last = strs[0], strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]
