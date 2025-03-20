class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}  # Dictionary to store counts
        
        # Count occurrences
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1  # ✅ Corrected
        
        # Find the majority element
        for i in hash_map:
            if hash_map[i] > len(nums) // 2:  # ✅ Integer division
                return i  # ✅ Return instead of print

        