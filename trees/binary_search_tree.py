from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if root.val == key:
        return root

    if key > root.val:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root


def search(root, key):
    if root is None or root.val == key:  # return null(null root) or value found
        return root

    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def getHeight(root):
    if not root:
        return 0

    if root.left and root.right:
        return 1 + max(getHeight(root.left), getHeight(root.right))
    elif root.left:
        return 1 + getHeight(root.left)
    elif root.right:
        return 1 + getHeight(root.right)
    else:
        return 1


def bfs(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].val)
        node = queue.popleft()

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of the BST
inorder(r)

print('Tree height:', getHeight(r))

bfs(r)
