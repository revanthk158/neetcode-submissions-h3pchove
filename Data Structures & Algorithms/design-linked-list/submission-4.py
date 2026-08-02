class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
    
    def addAtHead(self, val):
        node = LinkedNode(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def addAtTail(self, val):
        # Dynamically handles finding the end of the list safely
        self.addAtIndex(self.length, val)
    
    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return

        node = LinkedNode(val)
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
            
        node.next = cur.next
        cur.next = node
        self.length += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
            
        cur.next = cur.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
