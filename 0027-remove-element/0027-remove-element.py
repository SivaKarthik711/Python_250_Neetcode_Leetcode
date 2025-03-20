class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Position for non-val elements
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val elements forward
                k += 1
        
        return k  # New length of the modified array
