'''
    Linked list is a linear data structure in which elements are not
    stored at contigous memory locations. Elements are linked using pointers
        
'''

class Node:

    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def printList(self) -> None :
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


linklist=LinkedList()
linklist.head=Node(1)
second=Node(2)
third=Node(3)

linklist.head.next=second
second.next=third

linklist.printList()