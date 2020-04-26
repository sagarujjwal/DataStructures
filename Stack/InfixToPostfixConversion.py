#W.A.P to infix to postfix Conversion

# Q:- A+(B*C-(D/E*F)*G)*# H
#Ans:- ABC*DE/F*G*-H*+

stack=[]
# Function to insert a data in stack
def push(symbol):
    global stack
    stack.append(symbol)
    return stack

# Function top remove a data from stack
def pop():
    global stack
    k=stack.pop()
    return k
#Function to check whether symbol is operand or not
def isoperand(symbol):
    if (symbol >= 'a' and symbol<='z') or (symbol >= 'A' and symbol<='Z'):
        return 1
    else:
        return 0
# Function to check whether a symbol is operator or not
def isoperator(symbol):
    if symbol=='+' or symbol=="-" or symbol=="*" or symbol=='/':
        return 1
    else:
        return 0
# Function to check the preference of operators
def precedence(symbol):
    switch={
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    }
    return switch.get(symbol,'invalid symbol')

#Main Function
def main():
    global stack
    postfix=[]
    infix=input(str("Enter an Expression in string : "))
    push('(')
    #scaning each word of expression enter by user
    for i in infix:
        symbol=i
        if isoperand(symbol):
            postfix.append(symbol)
        elif symbol=='(':
            push(symbol)
        elif isoperator(symbol):
            while precedence(stack[-1])>=precedence(symbol):
                temp=pop()
                postfix.append(temp)
            push(symbol)
        elif symbol==')':
            while(stack[-1] != '('):
                temp=pop()
                postfix.append(temp)
            temp=pop()
        else:
            print('Enter a valid Expression')
            return
    # This while is for poping the remainig symbols from the stack and appending in the postfix untill we reach left parenthesis that
    # we push in stack in the begining of Main
    while(stack[-1] != '('):
        temp=pop()
        postfix.append(temp)


    a=''
    for i in postfix:
        a+=i
    print("postfix expression is : {}".format(a))



main()
