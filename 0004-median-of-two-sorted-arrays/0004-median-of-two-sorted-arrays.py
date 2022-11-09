class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        nums1.extend(nums2)
        nums1.sort()
        length1 = len(nums1)
        
        if length1 % 2 == 0:
            if length1 != 0:
                median1 = (nums1[length1//2 - 1] + nums1[length1//2]) / 2
        else:
            median1 = nums1[length1//2]
        
            
        if length1 == 0:
            return 0.0
        
        
        
        return median1

        