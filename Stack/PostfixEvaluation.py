# W.A.P to evaluate postfix notation
# Infix Notation: a*(b+c)-d/e
# postfix Notation: 'abc+*de/-'
# values a=5, b=6, c=2, d=12, e=4
# After putting value in Postfix Notation : 5 6 2  + * 12 4 / -
# Ans:- 37


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
    if (symbol>='a' and symbol<='z') or (symbol>='A' and symbol <='Z'):
        return 1
    else:
        return 0

def isoperator(symbol):
    if symbol=='+' or symbol=='-' or symbol=='*' or symbol=='/':
        return 1
    else:
        return 0

def main():
    global stack
    postfix=input('Enter a Postfix Expression : ')

    for i in postfix:
        symbol=i
        if isoperand(symbol):
            val=input("Enter the value of {} : ".format(symbol))
            if isinstance(val,int):
                push(val)
            else:
                print('Enter Integer only')
                return
        elif isoperator(symbol):
            A=pop()
            B=pop()
            switch={
            '+' : B + A,
            '-' : B - A,
            '*' : B * A,
            '/' : B / A
            }
            result=switch.get(symbol)
            push(result)
        else:
            print('Enter a valid Expression')
            return
    output=pop()
    print("Result of Postfix Evaluation is : {}".format(output))

main()
