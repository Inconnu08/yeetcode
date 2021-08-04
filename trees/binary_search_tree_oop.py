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

    def insert_recursive(self, root, val):
        if root is None:
            self.root = Node(val)
        else:
            if val < root.val:
                if root.left:
                    self.insert_recursive(root.left, val)
                else:
                    root.left = Node(val)
            elif val > root.val:
                if root.right:
                    self.insert_recursive(root.right, val)
                else:
                    root.right = Node(val)
            else:
                return

    def __get_height(self, root):
        if not root:
            return 0
        if root.left and root.right:
            return 1 + max(self.__get_height(root.left), self.__get_height(root.right))
        elif self.root.left:
            return 1 + self.__get_height(root.left)
        elif self.root.right:
            return 1 + self.__get_height(root.right)
        else:
            return 1

    def get_height(self):
        return self.__get_height(self.root)

    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

    def preorder(self, node):

        if node is not None:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):

        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=' ')


bst = BST()

inputs = [8, 3, 1, 6, 4, 7, 10, 14, 13]
for i in inputs:
    bst.insert(i)

# print('Breadth-First Traversal')
# tree.bft()

print('\nInorder Traversal')
bst.inorder(bst.root)

print('\nPreorder Traversal')
bst.preorder(bst.root)

print('\nPostorder Traversal')
bst.postorder(bst.root)

bstr = BST()

inputs = [8, 3, 1, 6, 4, 7, 10, 14, 13]
for i in inputs:
    bstr.insert_recursive(bstr.root, i)

# print('Breadth-First Traversal')
# tree.bft()

print('\nInorder Traversal')
bstr.inorder(bstr.root)

print('\nPreorder Traversal')
bstr.preorder(bstr.root)

print('\nPostorder Traversal')
bstr.postorder(bstr.root)

print('\n\nheight:', bstr.get_height())
