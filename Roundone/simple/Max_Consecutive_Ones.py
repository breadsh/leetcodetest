__author__ = 'jiangxiaowei-006'
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        retnum=0
        maxnum=0
        for num in nums:
            if num==1:
                retnum+=1
            else:
                maxnum = max(maxnum, retnum)
                retnum=0
        return max(maxnum, retnum)
