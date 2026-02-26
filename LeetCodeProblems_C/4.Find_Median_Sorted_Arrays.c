int cmp(const void *a, const void *b){
    return (*(int*)a - *(int*)b);
}
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int *nums = malloc((nums1Size + nums2Size)* sizeof(int));
    int numsLength = nums1Size + nums2Size;
    
    for(int i = 0; i < nums1Size;i++){
        nums[i] = nums1[i];
    }

    for(int i = 0;i < nums2Size;i++){
        nums[nums1Size + i] = nums2[i];
    }

    qsort(nums, numsLength, sizeof(int), cmp);

    float median = 0;

    if(numsLength % 2 == 0){
        median = (nums[numsLength/2 - 1] + nums[(numsLength/2)]) / 2.0;
    }
    else{
        median = (nums[(numsLength/2)]);
    }
    return median;
}