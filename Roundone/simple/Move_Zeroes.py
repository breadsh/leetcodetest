__author__ = 'jiangxiaowei-006'
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums