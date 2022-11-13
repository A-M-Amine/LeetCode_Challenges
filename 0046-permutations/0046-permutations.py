class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            
            return perm(nums)

        
def perm(nums):

    
    res = []

    if len(nums) == 1:
        return [nums]
    if len(nums) == 2:
        return [nums,nums[::-1]]

    for val in nums:
        temp = [i for i in nums if i != val]
        temp = perm(temp)
        for j in temp:      
            res.append([val,*j])

    
    return res