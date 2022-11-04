class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        for ind, val in enumerate(nums):

            if target <= val:
                return ind

            