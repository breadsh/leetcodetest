# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def __init__(self):
        self._root=TreeNode(None)
    def _solu(self,root,nums):
        if not nums:
            return
        root.val=max(nums)
        n = nums.index(max(nums))
        if nums[:n]:
            root.left=TreeNode(None)
            self._solu(root.left,nums[:n])
        if nums[n + 1:]:
            root.right=TreeNode(None)
            self._solu(root.right, nums[n + 1:])

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self._solu(self._root,nums)
        return self._root