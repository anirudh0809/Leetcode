# Simple implementation of breadth first search of a binary tree 


class tree:
    def __init__(self,value):
        self.right = None 
        self.left = None 
        self.val = value

# Function to get level order lraversal
def level_order(root):
    if root:
        h = height(root)

        for lvl in range(1,h+1):
            current_level(root,lvl)

def current_level(root,level):
    if root is None:
        return
    if level == 1:
        print(root.data,end=" ")
    elif level > 1:
        current_level(root.left,level-1)
        current_level(root.right,level-1)

def height(tree):
    if tree is None:
        return 0
    else :
        left_height = height(tree.left)
        right_height = height(tree.right)
 
        
        if left_height > right_height :
            return left_height+1
        else:
            return right_height+1


# driver 
if __name__ == '__main__':
    root = tree(1)
    root.right = tree(2)
    root.left = tree(3)
    root.right.right = tree(4)
    root.right.left = tree(5)
    root.left.right = tree(6)
    root.left.left = tree(7)

    print("Level order traversal of binary tree is -")
    level_order(root)