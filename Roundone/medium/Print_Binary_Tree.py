# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        res=[]
        memlst=[]

        def getheight(root):
            height=0
            memlst.append(root)
            while memlst:
                height+=1
                node=memlst.pop()
                if node:
                    memlst.append(node.right)
                    memlst.append(node.left)
            return height
        height=getheight(root)
        if root:
            while root.left!=None:
                memlst.append(root)
                root=root.left
            res.append([root.val,"",])
            while memlst:

            if root.left!=None:
