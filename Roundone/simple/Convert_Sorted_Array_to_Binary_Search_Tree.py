# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        lenth=len(nums)
        if lenth%2==0:
            i=lenth/2-1
        else:
            i=lenth/2
        root=TreeNode(nums[i])
        root.left=self.sortedArrayToBST(nums[0:i])
        root.right=self.sortedArrayToBST(nums[i+1:])
        return root

if __name__=='__main__':
    a=[1,3]
    s=Solution()
    print s.sortedArrayToBST(a).val
    print s.sortedArrayToBST(a).left
    print s.sortedArrayToBST(a).right