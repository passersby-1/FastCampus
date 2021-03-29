class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __search(self, value):
        node = self.root
        parent = None
        direction = None

        while node:
            if node.value == value:
                break
            elif value < node.value:
                parent = node
                node = node.left
                direction = 'left'
            else:
                parent = node
                node = node.right
                direction = 'right'
        
        return node, parent, direction

    def insert(self, value):
        node, parent, direction = self.__search(value)
        if node is not None:
            return False

        if parent is None:
            self.root = Node(value)
        else:
            if direction == 'left':
                parent.left = Node(value)
            else:
                parent.right = Node(value)
        return True

    def search(self, value):
        node, _, _ = self.__search(value)
        return node

    def remove(self, value):
        node, parent, direction = self.__search(value)
        # 삭제할 노드가 없다면 False 리턴
        if node is None:
            return False
        
        # 자식 노드가 없을 때
        if node.left is None and node.right is None:
            # Root Node
            if parent is None:
                self.root = None
            # Other Node
            else:
                if direction == 'left':
                    parent.left = None
                else:
                    parent.right = None
        # 왼쪽 자식 노드만 존재할 경우
        elif node.left is not None and node.right is None:
            # Root Node
            if parent is None:
                self.root = node.Left
            # Other Node
            else:
                if direction == 'left':
                    parent.left = node.left
                else:
                    parent.right = node.left
        # 오른쪽 자식 노드만 존재할 경우
        elif node.left is None and node.right is not None:
            # Root Node
            if parent is None:
                self.root = node.right
            # Other Node
            else:
                if direction == 'left':
                    parent.left = node.right
                else:
                    parent.right = node.right
        # 양쪽 자식 노드 모두 존재할 경우
        else:
            second_parent = node
            second_node = node.right
            second_direction = 'right'

            while second_node.left is not None:
                second_parent = second_node
                second_node = second_node.left
                second_direction = 'left'

            if second_direction == 'right':
                second_node.left = second_parent.left
                if parent is None:
                    self.root = second_node
                else:
                    if direction == 'left':
                        parent.left = second_node
                    else:
                        parent.right = second_node
            else:
                second_parent.left = second_node.right if second_node.right else None
                print('[*]' + str(second_parent.value))
                second_node.left = node.left
                second_node.right = node.right
                if parent is None:
                    self.root = second_node
                else:
                    if direction == 'left':
                        parent.left = second_node
                    else:
                        parent.right = second_node
        return True



if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    tree.insert(8)
    tree.insert(7)
    tree.insert(10)
    tree.insert(9)
    tree.insert(6)
    tree.root.display()
    tree.remove(6)
    tree.root.display()
    tree.remove(10)
    tree.root.display()
    tree.remove(8)
    tree.root.display()
    tree.insert(15)
    tree.insert(12)
    tree.insert(18)
    tree.root.display()
    tree.remove(9)
    tree.root.display()