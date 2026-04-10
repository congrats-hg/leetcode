class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 or n == 0:
            if m == 0:
                nums1.clear()
            if n == 0:
                nums2.clear()
        else:
            del nums1[m:]
            del nums2[n:]
        
        nums1.extend(nums2)
        nums1.sort()