class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merges two sorted arrays (nums1 and nums2) into nums1 in-place.
        
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        # Pointers for nums1, nums2, and the last position in nums1
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Merge from the end to avoid overwriting elements in nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 has remaining elements, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        