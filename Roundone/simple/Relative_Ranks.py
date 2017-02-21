__author__ = 'jiangxiaowei-006'
import copy
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        awarded=[]
        #sortnums=copy.deepcopy(nums)
        sortnums=copy.deepcopy(nums)
        sortnums.sort(reverse=True)

        for i in range(len(nums)):
            index=sortnums.index(nums[i])
            if index<3:
                if index==0:
                    awarded.append('Gold Medal')
                if index==1:
                    awarded.append('Silver Medal')
                if index==2:
                    awarded.append('Bronze Medal')
            else:
                awarded.append(str(index+1))
        return awarded



if __name__=="__main__":
    nums=[10,3,8,9,4]
    s=Solution()
    print s.findRelativeRanks(nums)
