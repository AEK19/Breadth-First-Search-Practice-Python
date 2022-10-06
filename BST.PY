# ***** BREADTH First Tree****

class Node:
    def __str__(self, data):
        self.left = None
        self.right = None
        self.data = None

    def insert(self, data):
        if self.data == None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

root = Node('A')
root.insert('I')
root.insert('L')
root.insert('O')
root.insert('V')
root.insert('E')
root.insert('M')
root.insert('a')
root.insert('T')
root.insert('H')
root.insert('S')



