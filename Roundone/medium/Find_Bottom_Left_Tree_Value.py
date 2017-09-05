# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        que=[root]
        for node in que:
            if node.right!=None:
                que.append(node.right)
            if node.left!=None:
                que.append(node.left)
        return que[-1].val
