__author__ = 'jiangxiaowei-006'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha=headA
        hb=headB
        if ha==None or hb==None:return None
        while ha!=None and hb!=None and ha!=hb:
            ha=ha.next
            hb=hb.next
            if ha==hb:
                return ha
            if ha==None: ha=headB
            if hb==None: hb=headA
        return ha