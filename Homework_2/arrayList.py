import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        return self.length == 0

    def prepend(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            
            tmp = array.array('l', [0] * self.capacity)
            tmp[0] = value
            for i in range(self.length):
                tmp[i + 1] = self.array[i]
            self.length += 1
            self.array = tmp
        else:
            for i in range(self.length - 1, -1, -1):
                self.array[i + 1] = self.array[i]
            self.array[0] = value

    def append(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            tmp = array.array('l', [0] * self.capacity)
            for i in range(self.length):
                tmp[i] = self.array[i]
            self.array = tmp
                
        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        if self.length <= index:
            return False
        
        for i in range(index, self.length):
            self.array[i - index] = self.array[index]
        self.length -= index
        return True

    def access(self, index):
        if self.length <= index:
            return False
        return self.array[index]

    def insert(self, index, value):
        if self.length <= index:
            return False
        
        if self.capacity == self.length:
            self.capacity *= 2
            tmp = array.array('l', [0] * self.capacity)
            for i in range(index):
                tmp[i] = self.array[i]
            for i in range(index, self.length):
                tmp[i + 1] = self.array[i]
            self.array = tmp
        else:
            for i in range(self.length - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            
        self.array[index] = value
        self.length += 1
        return True

    def remove(self, index):
        if self.length <= index:
            return False
        
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

        return True

    def print(self):
        if self.length == 0:
            return '[]'
        
        rst = '['
        for i in range(self.length):
            rst += f'{self.array[i]} '
        rst += '\b]'
        return rst

arrayList = ArrayList(3)
print(arrayList.print())
arrayList.append(10)
print(arrayList.print())
arrayList.append(20)
print(arrayList.print())
arrayList.append(30)
print(arrayList.print())
arrayList.insert(1, 5)
print(arrayList.print())
arrayList.append(40)
print(arrayList.print())

arrayList.insert(0, 5)
print(arrayList.print())
arrayList.insert(4, 50)
print(arrayList.print())

arrayList.remove(2)
print(arrayList.print())