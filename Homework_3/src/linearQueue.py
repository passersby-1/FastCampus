import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            return False
        
        self.array[self.rear] = value
        self.rear += 1
        return True

    def get(self):
        if self.front == self.rear:
            return None
        
        value = self.array[self.front]
        self.front += 1
        return value

    def peek(self):
        if self.front == self.rear:
            return None
        return self.array[self.front]

    def print(self):
        if self.front == self.rear:
            print('[]')
        else:
            print('[', end='')
            for i in range(self.front, self.rear):
                print(f'{self.array[i]}, ', end='')
            print('\b\b]')

lQueue = LinearQueue(5)
lQueue.print()
print(lQueue.put(10))
print(lQueue.put(20))
print(lQueue.put(30))
print(lQueue.put(40))
print(lQueue.put(50))
print(lQueue.put(50))
lQueue.print()
print(lQueue.peek())
print(lQueue.get())
print(lQueue.get())
print(lQueue.get())
print(lQueue.get())
print(lQueue.get())
print(lQueue.get())
print(lQueue.put(60))
lQueue.print()