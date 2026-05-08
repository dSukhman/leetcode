// Original solution from 2023, solved using a linear scan in C.
// Included to showcase my growth as a programmer, as I later implemented a more efficient binary search solution in Python.

int searchInsert(int* nums, int numsSize, int target){
    for(int i = 0; i < numsSize; i++){
        if (nums[i] == target){
            return i;
        }
        else{
            if (nums[i] > target){
                return i;
            }        
        } 
    }
    return numsSize;
}