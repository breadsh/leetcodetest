__author__ = 'jiangxiaowei-006'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self._leftsum=0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        else:
            if root.left and root.left.left==None and root.left.right==None:
                self._leftsum+=root.left.val
            else:
                self.sumOfLeftLeaves(root.left)
                self.sumOfLeftLeaves(root.right)
        return self._leftsum