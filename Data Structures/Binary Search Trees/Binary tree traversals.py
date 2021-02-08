import sys, threading

sys.setrecursionlimit(10 ** 8)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, nodes, idx):
    r, lft, rt = idx
    if not root:
        root = TreeNode(r)

    if lft != -1:
        root.left = insert(root.left, nodes, nodes[lft])

    if rt != -1:
        root.right = insert(root.right, nodes, nodes[rt])

    return root


def inorder(root):
    if not root:
        return root
    inorder(root.left)
    inn.append(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return root
    pre.append(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return root
    postorder(root.left)
    postorder(root.right)
    post.append(root.val)


inn, pre, post = list(), list(), list()


def main():
    root = None
    nodes = list()
    for i in range(int(input())):
        nodes.append(list(map(int, input().split())))

    root = insert(root, nodes, nodes[0])

    inorder(root)
    preorder(root)
    postorder(root)
    print(*inn)
    print(*pre)
    print(*post)

threading.Thread(target=main).start()
