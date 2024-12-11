# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less = lessPtr = ListNode(0)
        more = morePtr = ListNode(0)
        cur = head

        while cur:
            if cur.val < x:
                lessPtr.next = ListNode(cur.val)
                lessPtr = lessPtr.next
            else:
                morePtr.next = ListNode(cur.val)
                morePtr = morePtr.next
            
            cur = cur.next
        
        lessPtr.next = more.next

        return less.next