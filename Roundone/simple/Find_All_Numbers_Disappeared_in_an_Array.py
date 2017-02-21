__author__ = 'jiangxiaowei-006'
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            print index
            nums[index] = - abs(nums[index])
            print nums
        print '-----------------------'
        print nums
        #return [i + 1 for i in range(len(nums)) if nums[i] > 0]
if __name__=="__main__":
    a=[4,3,2,7,8,2,3,1]
    s=Solution()
    s.findDisappearedNumbers(a)
