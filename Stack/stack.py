def push(val):
    if top==maxsize-1:
        print('overflow')
    stack.append(val)
    return stack

def pop():
    k=stack[top]:
    stack.pop()
    top=top-1
    return k


maxsize=10
top=-1
stack=[]
print('top',top,'maxsize',maxsize)
while top!=maxsize-1:
    top+=1
    val=input("Enter the value to insert in stack: ")
    a=push(val)
    print(a)
