__author__ = 'jiangxiaowei-006'
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        if len(numset)<3:
            return max(numset)
        numset.remove(max(numset))
        numset.remove(max(numset))
        return max(numset)


if __name__=='__main__':
    s=Solution()
    nums=[1,2,2,5,3,5]
    print s.thirdMax(nums)