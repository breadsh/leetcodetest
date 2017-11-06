# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1=[]
        stack2=[]
        while l1:
            stack1.append(str(l1.val))
            l1=l1.next
        x=''.join(stack1)
        while l2:
            stack2.append(str(l2.val))
            l2=l2.next
        y=''.join(stack2)
        res=int(x)+int(y)
        node=ListNode(int(str(res)[0]))
        head=node
        for i in range(1,len(str(res))):
            nod=ListNode(int(str(res)[i]))
            node.next=nod
            node=nod
        return head


