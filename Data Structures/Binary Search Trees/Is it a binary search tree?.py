import sys, threading

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
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


def isbst(root, mini, maxi):
    if not root:
        return True

    if root.val < mini or root.val > maxi:
        return False

    lft = isbst(root.left, mini, root.val)
    rt = isbst(root.right, root.val, maxi)

    return lft and rt

inn= list()
def main():
    root = None
    nodes = list()
    for i in range(int(input())):
        nodes.append(list(map(int, input().split())))

    if nodes:
        root = insert(root, nodes, nodes[0])
        '''
        # Method 1
        check for both left and right node values.
        print('CORRECT') if isbst(root, float('-inf'), float('inf')) else print('INCORRECT')
        '''

        # Method 3
        '''
        By using Inorder Traversal, we always get the values in the sorted order. If tree is BST.
        '''
        flag = True
        inorder(root)
        for i in range(1, len(inn)):
            if inn[i] < inn[i - 1]:
                flag = False
                break

        print('CORRECT') if flag else print('INCORRECT')
    else:
        print('CORRECT')


threading.Thread(target=main).start()
