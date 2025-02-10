# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        
        for l in lists:
            if l: 
                heapq.heappush(heap, (l.val, l))  
        
        ans = dummy = ListNode(None)

        while heap:
            dummy.next = heapq.heappop(heap)[1]  
            dummy = dummy.next

            if dummy.next:  
                heapq.heappush(heap, (dummy.next.val, dummy.next))  

        return ans.next
