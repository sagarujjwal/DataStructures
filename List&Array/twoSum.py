class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


nums = [3, 2, 3, 5, 6, 7]
target = 9
obj=Solution()
print(obj.twoSum(nums, target))

