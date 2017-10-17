class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bg=nums[0]
        res=[0,0]
        for x in nums[1:]:
            bg=bg ^ x
        bg&=-bg
        for x in nums:
            if bg&x==0:
                res[0]^=x
            else:
                res[1]^=x
        return res





if __name__=='__main__':
    nums=[1,1,2,2,3,3,4,5,4,5,6,7,8,9,6,7,8,10]
    s=Solution()
    print s.singleNumber(nums)
