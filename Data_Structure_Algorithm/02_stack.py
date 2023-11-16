'''
    Stack is a linear data structure that stores items in a LastIn-FirstOut
    or FirstIn-LastOut manner. 
    Push and Pop happends at same end
'''

## Methods
# empty() -> stack is empty
# size() -> size of stack
# top -> topmost element
# push() -> inserts element at top   append
# pop() -> deletes element at top

stack=[]
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

print(stack)

stack.pop()
stack.pop()
print(stack)

stack.pop()
stack.pop()
#below line raise indexerror
stack.pop()
