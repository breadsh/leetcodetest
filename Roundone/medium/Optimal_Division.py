class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(reverse=True)
        nums=map(str,nums)
        if len(nums) <= 2: return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))




if __name__=='__main__':
    nums=[3,4,5,2]
    s=Solution()
    print s.optimalDivision(nums)
