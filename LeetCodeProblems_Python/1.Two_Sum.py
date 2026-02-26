class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        Hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Hashmap:
                return [Hashmap[diff], i]
            Hashmap[n] = i