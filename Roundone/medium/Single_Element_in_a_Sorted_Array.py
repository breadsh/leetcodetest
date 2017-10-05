class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=0
        mark=0
        for x in nums:
            if flag==0:
                mark=x
                flag=1
            else:
                if x!=mark:
                    return mark
                else:
                    flag=0
        return x

if __name__=='__main__':
    nums=[1,1,2]
    s=Solution()
    print s.singleNonDuplicate(nums)

