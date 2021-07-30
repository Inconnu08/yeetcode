class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while 1:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break

                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    def preorder(self, node):

        if node is not None:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):

        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val)


bst = BST()

inputs = [8, 3, 1, 6, 4, 7, 10, 14, 13]
for i in inputs:
    bst.insert(i)

# print('Breadth-First Traversal')
# tree.bft()

print('Inorder Traversal')
bst.inorder(bst.root)

print('Preorder Traversal')
bst.preorder(bst.root)

print('Postorder Traversal')
bst.postorder(bst.root)
