__author__ = 'jiangxiaowei-006'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)/2+1):
            if nums.count(nums[i])==1:
                return i

