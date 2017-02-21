__author__ = 'jiangxiaowei-006'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self._mem=set()
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        if head in self._mem:
            return True
        self._mem.add(head)
        return self.hasCycle(head.next)
