__author__ = 'jiangxiaowei-006'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        retnode=head
        while retnode!=None and retnode.val==val:
            retnode=retnode.next
        tnode=retnode
        while tnode!=None:
            if tnode.next!=None:
                if tnode.next.val==val:
                    tnode.next=tnode.next.next
                else:
                    tnode=tnode.next
            else:
                break
        return retnode
