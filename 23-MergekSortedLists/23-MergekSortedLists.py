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
            val, node = heapq.heappop(heap)  
            dummy.next = node  
            dummy = dummy.next

            if node.next:  
                heapq.heappush(heap, (node.next.val, node.next))  

        return ans.next
