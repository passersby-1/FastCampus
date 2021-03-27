from collections import deque

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    

class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]
        
        self.root = node_list[0]
    
    def preorder(self):
        def recursion(node):
            nonlocal s
            if node is None:
                return
            s += str(node.value) + ' '
            recursion(node.left)
            recursion(node.right)
        
        s = ''
        recursion(self.root)
        print(s)

    def inorder(self):
        def recursion(node):
            nonlocal s
            if node is None:
                return
            recursion(node.left)
            s += str(node.value) + ' '
            recursion(node.right)
        
        s = ''
        recursion(self.root)
        print(s)

    def postorder(self):
        def recursion(node):
            nonlocal s
            if node is None:
                return
            recursion(node.left)
            recursion(node.right)
            s += str(node.value) + ' '
        
        s = ''
        recursion(self.root)
        print(s)

    def bfs(self, value):
        queue = deque([self.root])

        while len(queue) != 0:
            node = queue.popleft()
            if node.value == value:
                return True
            if node.left is not None: queue.append(node.left)
            if node.right is not None: queue.append(node.right)

        return False
    
    def dfs(self, value):
        def recursion(node):
            nonlocal is_found
            if node is None:
                return
            
            if is_found is True:
                return

            if node.value == value:
                is_found = True
                return
            recursion(node.left)
            recursion(node.right)

        is_found = False
        recursion(self.root)
        return is_found


if __name__ == '__main__':
    bt = BinaryTree([1, 2, 3, 4, 5, 6, 7])
    bt.preorder()
    bt.inorder()
    bt.postorder()
    print(bt.dfs(0))
    print(bt.bfs(4))
    print(bt.bfs(10))