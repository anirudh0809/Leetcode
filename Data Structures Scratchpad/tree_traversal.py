
# Simple code to traverse a tree 
# Inorder,preorder and postorder traversals 


class tree:

    def __init__(self,value):
        self.left = None
        self.right = None 
        self.val = value

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


if __name__ == '__main__':
    root = tree(1)
    root.right = tree(2)
    root.left = tree(3)
    root.right.right = tree(4)
    root.right.left = tree(5)
    root.left.right = tree(6)
    root.left.left = tree(7)

    print('In order traversal for the tree is ')
    inorder(root)
    print('\n')


    print('Pre order traversal for the tree is ')
    preorder(root)
    print('\n')

    print('Post order traversal for the tree is ')
    postorder(root)