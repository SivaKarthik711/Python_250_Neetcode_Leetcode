class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        else :
             return True
