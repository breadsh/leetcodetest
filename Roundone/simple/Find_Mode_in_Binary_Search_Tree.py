# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.mem={}
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self._findMode(root)
        res=[]
        for key in self.mem:
            n=self.mem[key]
            if len(res)==0:
                res.append(key)
            else:
                if n>self.mem[res[0]]:
                    res=[]
                    res.append(key)
                    continue
                if n==self.mem[res[0]]:
                    res.append(key)
        return res
    def _findMode(self,root):
        if root==None:
            return None
        else:
            self.mem[root.val]=self.mem.get(root.val,0)+1
        self._findMode(root.left)
        self._findMode(root.right)

if __name__=='__main__':
    a=TreeNode(2)
    a.left=None
    b=TreeNode(3)
    a.right=b
    b.left=None
    c=TreeNode(4)
    b.right=c
    c.left=None
    d=TreeNode(5)
    c.right=d
    d.left=None
    e=TreeNode(6)
    d.right=e
    s=Solution()
    print s.findMode(a)
