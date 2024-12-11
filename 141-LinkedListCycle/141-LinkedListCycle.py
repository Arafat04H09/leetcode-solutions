def hasCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# 96.56%