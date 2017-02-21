__author__ = 'jiangxiaowei-006'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        else:
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)