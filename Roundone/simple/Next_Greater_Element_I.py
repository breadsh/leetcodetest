__author__ = 'jiangxiaowei-006'
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        retlst=[]
        for i in findNums:
            found=False
            for j in range(nums.index(i)+1,len(nums)):
                if nums[j]>i:
                    retlst.append(nums[j])
                    found=True
                    break
                else:
                    continue
            if found==False:
                retlst.append(-1)
        return retlst

if __name__=="__main__":
    nums1 = [4,1,2]
    nums2 = [1,2,3,4]
    s=Solution()
    print s.nextGreaterElement(nums1,nums2)
