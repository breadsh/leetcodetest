# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            node=TreeNode(v)
            node.left=root
            return node
        mem=[root]
        for i in range(d-2):
            n=len(mem)
            for j in range(n):
                node=mem.pop(0)
                if node.left:
                    mem.append(node.left)
                if node.right:
                    mem.append(node.right)
        while mem:
            node=mem.pop(0)
            orilnode=node.left
            node.left=TreeNode(v)
            node.left.left=orilnode
            orirnode = node.right
            node.right=TreeNode(v)
            node.right=orirnode
        return root

