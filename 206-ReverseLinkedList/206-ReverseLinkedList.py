# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        newHead = None
        while head:
            nxt = head.next
            head.next = newHead
            newHead = head
            head = nxt
        
        return newHead

            
        