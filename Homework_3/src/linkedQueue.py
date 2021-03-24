class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
    

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def put(self, value):
        if self.tail is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail = Node(value, self.tail, None)
            self.tail.prev.next = self.tail

    def get(self):
        if self.head is None:
            return None
        
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def print(self):
        if self.head is None:
            print('[]')
        else:
            cur = self.head
            print('[', end='')
            while cur is not None:
                print(f'{cur.value} ', end='')
                cur = cur.next
            print('\b]')

linkedQueue = LinkedQueue()
linkedQueue.print()
linkedQueue.put(1)
linkedQueue.put(2)
linkedQueue.put(3)
linkedQueue.put(4)
linkedQueue.put(5)
linkedQueue.put(6)
linkedQueue.put(7)
linkedQueue.print()
print(linkedQueue.peek())
print(linkedQueue.get())
print(linkedQueue.get())
print(linkedQueue.get())
print(linkedQueue.get())
print(linkedQueue.get())
print(linkedQueue.get())
print(linkedQueue.get())
print(linkedQueue.get())
print(linkedQueue.get())
linkedQueue.print()