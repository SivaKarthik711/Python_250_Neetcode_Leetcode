class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in nums:
            ans.append(i)
        ans = ans + nums
        return ans        