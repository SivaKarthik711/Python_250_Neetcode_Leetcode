class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums) # set elminates duplicates
        if len(nums) == len(nums_set): #compared the lengths of list and set
            return False
        else :
             return True
