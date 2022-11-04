int searchInsert(int* nums, int numsSize, int target){
    
    if(target < nums[0]) {
            return 0;
    }

    if(target > nums[numsSize - 1]) {
        return numsSize;
    }


    for(int i = 0; i < numsSize; i++) {
        if(target <= nums[i]) {
            return i;
        }
    }
    
    return 0;

}