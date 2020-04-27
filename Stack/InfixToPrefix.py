
# W.A.P to find Prefix Notation from Infix Notation
# Infix Notation:- '(a-b/c)*(a/k-l)'
# Postfix Notation:- lka/-cb/a-*
# Prefix Notation:- *-a/bc-/akl


stack=[]
def push(symbol):
    global stack
    stack.append(symbol)
    return stack

def pop():
    global stack
    k=stack.pop()
    return k

def isoperand(symbol):
    if (symbol>='a' and symbol<='z') or (symbol>='A' and symbol<='Z'):
        return 1
    else:
        return 0

def isoperator(symbol):
    if symbol=='+' or symbol=='-' or symbol=='*' or symbol=='/':
        return 1
    else:
        return 0
def precedence(symbol):
    preference={
    '(': 0,
    ')': 0,
    '-': 1,
    '+': 1,
    '*': 2,
    '/': 2
    }
    return preference.get(symbol,'Invalid operator')

def reverse(string):
    x=0
    y=len(string)
    for i in range(y/2):
        a=string[x]
        string[x]=string[y-1]
        string[y-1]=a
        y-=1
        x+=1
    for i in range(len(string)):
        if string[i]=='(':
            string[i]=')'
        elif string[i]==')':
            string[i]='('

def main():
    global stack
    postfix=[]
    infix=list(input("Enter a Infix Expression : "))
    reverse(infix)
    push('(')
    for i in infix:
        symbol=i
        if isoperand(symbol):
            postfix.append(symbol)
        elif symbol=='(':
            push(symbol)
        elif isoperator(symbol):
            while (precedence(stack[-1]) >= precedence(symbol)):
                temp=pop()
                postfix.append(temp)
            push(symbol)
        elif symbol==')':
            while (stack[-1] != '('):
                temp=pop()
                postfix.append(temp)
            temp=pop()
        else:
            Print("Enter a valid Expression")
            return
    while stack[-1]!='(':
        temp=pop()
        postfix.append(temp)

    a=''
    for i in postfix:
        a+=i
    print("Postfix Expression is : {}").format(a)
    reverse(postfix)
    b=''
    for i in postfix:
        b+=i
    print("Prefix Expression is : {}").format(b)

main()
