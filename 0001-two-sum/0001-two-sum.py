class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {} # to check, we need index as return. So, index is the value for the dictionary

        for index, i in enumerate(nums): # as we need both index to return and value to check, enumerate functions is helpful for this case which iterates over the list.

            diff = target - nums[index] # we need a variable to check previous values in the dictionary
            if diff in dict_nums:
                return [dict_nums[diff],index]
            else:
                dict_nums[i] = index
        