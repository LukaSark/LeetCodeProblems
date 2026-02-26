#include <stdio.h>
#include <stdlib.h>

// Comparison function for qsort
int cmp(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    int capacity = 100; // initial capacity (can grow later if needed)

    int** result = (int**)malloc(capacity * sizeof(int*));
    *returnColumnSizes = (int*)malloc(capacity * sizeof(int));

    if (numsSize < 3) return result;

    qsort(nums, numsSize, sizeof(int), cmp);

    for (int i = 0; i < numsSize - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicates for i

        int left = i + 1;
        int right = numsSize - 1;

        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];

            if (sum == 0) {
                int* triplet = (int*)malloc(3 * sizeof(int));
                triplet[0] = nums[i];
                triplet[1] = nums[left];
                triplet[2] = nums[right];

                // Store the triplet
                result[*returnSize] = triplet;
                (*returnColumnSizes)[*returnSize] = 3;
                (*returnSize)++;

                // Resize if needed
                if (*returnSize >= capacity) {
                    capacity *= 2;
                    result = (int**)realloc(result, capacity * sizeof(int*));
                    *returnColumnSizes = (int*)realloc(*returnColumnSizes, capacity * sizeof(int));
                }

                // Skip duplicates for left and right
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;

                left++;
                right--;
            } 
            else if (sum < 0) {
                left++;
            } 
            else {
                right--;
            }
        }
    }

    return result;
}
