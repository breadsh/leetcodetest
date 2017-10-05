#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        mem = defaultdict(list)
        mem[0] = [root, ]
        res = []
        lev = 0
        while 1:
            node = mem[lev]
            lev += 1
            flag = False
            maxnum = -2147483648

            for x in node:
                if x and x.val > maxnum:
                    maxnum = x.val
                if x.left:
                    flag = True
                    mem[lev].append(x.left)
                if x.right:
                    flag = True
                    mem[lev].append(x.right)
            res.append(maxnum)
            if not flag:
                break
        return res


