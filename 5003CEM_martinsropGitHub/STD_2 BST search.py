import math

"""Node class"""

class Node:
    def __init__(self, data = None):
        self.data = data #main data 
        self.left = None #left side data
        self.right = None #right side data

"""BST class with insert and display methods. display pretty prints the tree"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None: #check if the root is empty
            self.root = Node(data) #assign the data to root
        else:
            self._insert(data, self.root) #if the root is not empty, call the fuction _insert

    def _insert(self, data, cur_node):
        if data < cur_node.data:  #if the data is less then the current node 
            if cur_node.left is None:  #if the left data of the current node is empty
                cur_node.left = Node(data) #assign the data to left node
            else:                        #else it will run until reach the end
                self._insert(data, cur_node.left) 
        elif data > cur_node.data:  #if the data is grater than current node
            if cur_node.right is None: #if right data on current node is empty
                cur_node.right = Node(data) #assign the data to the right side
            else:                          #else it will run until reach the end
                self._insert(data, cur_node.right)
        else:                              #if the data already exist print the message
            print("Value already present in tree")

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
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
    
    def find_i(self,target): 
        cur_node = self.root #to check that the search starts at the root
        while cur_node != None: #only gonna rune when is equal to node
            if cur_node.data == target: #when is equal to the target
                return True 
            elif cur_node.data > target: #when the current node is less than the target
                cur_node = cur_node.left #progress to the left node
            else:
                cur_node = cur_node.right #progress to the right node
        return False #when the target is not found
    
    def find_r(self, target):
        if self.root:  #start the root if the tree exist
            if self._find_r(target, self.root): #if target is found will return true
                return True
            return False  #if not return false
        else:       #else return false if tree doens´t exist
            return None

    def _find_r(self, target, cur_node):
        if target > cur_node.data and cur_node.right: #if the target is grater than node and the right side exist 
            return self._find_r(target, cur_node.right) #move target to the righ side
        elif target < cur_node.data and cur_node.left: #if the target is less than the node and left side exist
            return self._find_r(target, cur_node.left) #move target to the left side
        if target == cur_node.data: #if the is not found
            return True

    

#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)

bst.display(bst.root)



print(bst.find_r(5))
print(bst.find_i(19))

