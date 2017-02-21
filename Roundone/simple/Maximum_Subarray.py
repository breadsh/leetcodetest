import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        res=-sys.maxint-1
        for n in nums:
            sum+=n
            if sum<0:
                sum=n
            res=max(sum,res)
        return res