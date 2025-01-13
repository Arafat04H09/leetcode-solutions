# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = head
        while dummy and dummy.next:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        return head

