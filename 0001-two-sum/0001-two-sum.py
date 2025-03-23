class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}

        for index, value in enumerate(nums):

            diff = target - nums[index]
            if diff in nums_map:
                return [nums_map[diff],index]
            else:
                nums_map[value] = index