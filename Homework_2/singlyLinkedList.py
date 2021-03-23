class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(value, None)

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
        if self.head is None:
            return False
        
        if index == 0:
            return self.head.value
        
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
            self.head = Node(value, self.head)
        else:
            cur = self.head
            prev = None
            for _ in range(index):
                prev = cur
                cur = cur.next
                if cur is None:
                    return False
            prev.next = Node(value, cur)
        return True

    def remove(self, index):
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            for _ in range(index):
                prev = cur
                cur = cur.next
                if cur is None:
                    return False
            prev.next = cur.next
        return True


    def print(self):
        if self.head is None:
            print('[]')
            return
        
        print('[', end='')
        cur = self.head
        while cur != None:
            print(f'{cur.value} ', end='')
            cur = cur.next
        print('\b]')


s = SinglyLinkedList()
s.print()
s.append(10)
s.append(20)
s.append(30)
print(s.access(3))
s.print()
s.insert(2, 25)
s.print()
s.remove(2)
s.print()
s.remove(1)
s.print()
s.remove(1)
s.print()
s.remove(0)
s.print()