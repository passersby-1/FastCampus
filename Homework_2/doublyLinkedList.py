class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.head = Node(value, self.head, None)
            self.head.next.prev = self.head

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail = Node(value, None, self.tail)
            self.tail.prev.next = self.tail 

    def set_head(self, index):
        if self.head is None:
            return False
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
            if cur is None:
                return False
        self.head = cur
        return True

    def access(self, index):
        if self.head is None or index < 0:
            return False
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
            if cur is None:
                return False
        return cur.value

    def insert(self, index, value):
        if self.head is None and index != 0:
            return False
        
        if index == 0:
            self.prepend(value)
        else:
            cur = self.head
            prev = None
            for _ in range(index):
                prev = cur
                cur = cur.next
                if cur is None:
                    return False
            prev.next = Node(value, cur, prev)
            cur.prev = prev.next
        return True

    def remove(self, index):
        if self.head is None or index < 0:
            return False
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            cur = self.head
            prev = None
            for _ in range(index):
                prev = cur
                cur = cur.next
                if cur is None:
                    return False
            
            if cur.next is None:
                prev.next = None
                self.tail = prev
            else:
                prev.next = cur.next
                cur.next.prev = prev
        return True

    def print(self):
        if self.head is None:
            print('[]')
            return

        print('[', end='')
        cur = self.head
        while cur is not None:
            print(f'{cur.value} ', end='')
            cur = cur.next
        print('\b]')


d = DoublyLinkedList()
d.prepend(10)
d.print()
d.append(20)
d.print()
d.append(30)
d.print()
d.append(40)
d.print()
d.prepend(5)
d.print()
d.set_head(2)
d.print()
print(d.access(-1))
d.insert(1, 25)
d.print()
d.insert(3, 35)
d.print()
d.insert(5, 50)
d.print()
d.remove(4)
d.print()
d.remove(0)
d.print()
d.remove(1)
d.print()