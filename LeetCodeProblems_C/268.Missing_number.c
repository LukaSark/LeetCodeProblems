int missingNumber(int* nums, int numsSize) {
    int* count = (int*)calloc(numsSize + 1, sizeof(int));

    for(int i=0;i<numsSize;i++){
        count[nums[i]]++;
    }
    int missing;

    for(int i=0;i<=numsSize;i++){
        if(count[i] == 0){
            free(count);
            missing = i;
            break;
        }
    }
    return missing;
}