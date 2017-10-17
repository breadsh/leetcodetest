class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None

def bst_search_recursion(root,x):
    if root or root.val==x:
        return root
    else:
        if x<root.val:
            bst_search_recursion(root.left,x)
        else:
            bst_search_recursion(root.right,x)