# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.mem=defaultdict()
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.subtree(root)
        frequent = max(self.mem.values())
        return [s for s in self.mem.keys() if self.mem[s] == frequent]


    def subtree(self,node):
        if node == None: return 0
        s = node.val + self.subtree(node.left) + self.subtree(node.right)
        if self.mem.has_key(s):
            self.mem[s]+=1
        else:
            self.mem[s]=1
        return s


