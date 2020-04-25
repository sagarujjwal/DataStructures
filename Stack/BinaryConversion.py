
'''
Conversion from decimal to binary no
'''
def push(val):
    global stack,top
    top=top+1
    stack.append(val)
    return stack

def pop():
    global stack,top
    k=stack[top]
    top=top-1
    return k



def main():
    num=input("Enter a decimal no")
    while num!=0:
        d=num%2
        push(d)
        num=num/2
    print("Binary value is:")
    while (top != -1):
        x=pop()
        print(x)





stack=[]
top=-1
main()

print('stack',stack)
