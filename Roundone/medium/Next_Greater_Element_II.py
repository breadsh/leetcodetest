class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res=[-1 for i in range(n)]
        stack=[]
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
if __name__=='__main__':
    s=Solution()
    nums=[1,2,1]
    print s.nextGreaterElements(nums)