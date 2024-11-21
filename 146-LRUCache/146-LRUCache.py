class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = dict()
        self.head = ListNode(0,0)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            node = self.d[key]
            self.delete(node)
            self.insert(node)
            return node.value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            node = self.d[key]
            self.delete(node)
            node.value = value
            self.insert(node)
        else:
            if len(self.d) >= self.capacity:
                self.deleteFromTail()
            node = ListNode(key, value)
            self.d[key] = node
            self.insert(node) 

    def deleteFromTail(self):
        tailNode = self.tail.prev
        del self.d[tailNode.key]
        self.delete(tailNode)

    def insert(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)