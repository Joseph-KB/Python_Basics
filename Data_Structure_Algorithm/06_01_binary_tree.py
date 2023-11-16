class Node:
    def __init__(self,key) -> None:
        self.left=None
        self.right=None
        self.val=key

root=Node(1)

root.left=Node(2)
root.right=Node(3)

root.left.left=Node(4)
root.left.left.left=Node(5)