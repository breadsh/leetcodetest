__author__ = 'jiangxiaowei-006'
class Solution(object):
    def __init__(self):
        self.movecount=0
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #not good enough to pass --time limited
        while 1:
            ma=max(nums)
            mi=min(nums)
            if ma==mi:
                return self.movecount
            diff = ma - mi
            self.movecount+=diff
            idx=nums.index(ma)
            for i in range(len(nums)):
                if i!=idx:
                    nums[i]+=diff


if __name__=='__main__':
    ts=[1,2,3]
    s=Solution()
    print s.minMoves(ts)



