# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap = []

        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        
        ans = dummy = ListNode(None)

        while heap:
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
        
        return ans.next