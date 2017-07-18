# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret=[float(root.val)]
        def _averageOfLevels(root):
            if root.left!=None and root.right!=None:
                ret.append((float(root.left.val)+float(root.right.val))/2)
            if root.left!=None and root.right==None:
                ret.append(float(root.left.val))
            if root.left == None and root.right != None:
                ret.append(float(root.right.val))
            _averageOfLevels(root.left)
            _averageOfLevels(root.right)
        _averageOfLevels(root)
        return ret

