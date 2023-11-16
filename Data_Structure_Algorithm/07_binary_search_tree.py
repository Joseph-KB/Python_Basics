'''
    Node based binary tree data structure
        - left subtree contains only nodes with keys lesser than the node's key
        - rifht subtree has keys greater than node's key
        - all forthcoming subtree should have the above charctrestics
'''
class Node:
    def __init__(self,key) -> None:
        self.val= key
        self.left = None
        self.right = None

def search(root,key):
    if root is None or root.val==key:
        return root
    if root.val < key:
        return search(root.right,key)
    return search(root.left,key)

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val < key:
            root.right= insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root=Node(10)
insert(root,9)
insert(root,8)
insert(root,7)
insert(root,3)
insert(root,5)

inorder(root)

print(search(root,5))
