# This is a calculator by Jonathan Gautreaux
# It will use the infix it algorithm to do calculations based on a string
# I modified code from the following link to work for modulus and power functions
# https://www.geeksforgeeks.org/expression-evaluation/ and
# http://code.activestate.com/recipes/579123-infix-expression-evaluation/
# it will also accept input from the users until they say Stop

# issues with program
# Cannot go to previous inputs.
# I tried to save into a stack and bring it back if you entered up but was unable to do it.
# Cannot handle when there is a mistake in the input.
# Cannot handle if a negative is given



def isOp(c): #tests if opporator
    if c != "":
        return (c in "+-*/%^")
    else:
        return False


def pri(c):  # operator priority
    if c in "+-": return 0
    if c in "*/%": return 1
    if c in "^": return 2


def isNum(c):
    if c != "":
        return (c in "0123456789.")
    else:
        return False


def calc(op, num1, num2):
    if op == "+": return str(float(num1) + float(num2))
    if op == "-": return str(float(num1) - float(num2))
    if op == "*": return str(float(num1) * float(num2))
    if op == "/": return str(float(num1) / float(num2))
    if op == "%": return str(float(num1) % float(num2))
    if op == "^": return str(float(num1) ** float(num2))


def Infix(expr):
    expr = list(expr)
    stackChr = list()  # character stack
    stackNum = list()  # number stack
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if len(expr) > 0:
            d = expr[0]
        else:
            d = ""
        if isNum(c):
            num += c
            if not isNum(d):
                stackNum.append(num)
                num = ""
        elif isOp(c):
            while True:
                if len(stackChr) > 0:
                    top = stackChr[-1]
                else:
                    top = ""
                if isOp(top):
                    if not pri(c) > pri(top):
                        num2 = stackNum.pop()
                        op = stackChr.pop()
                        num1 = stackNum.pop()
                        stackNum.append(calc(op, num1, num2))
                    else:
                        stackChr.append(c)
                        break
                else:
                    stackChr.append(c)
                    break
        elif c == "(":
            stackChr.append(c)
        elif c == ")":
            while len(stackChr) > 0:
                c = stackChr.pop()
                if c == "(":
                    break
                elif isOp(c):
                    num2 = stackNum.pop()
                    num1 = stackNum.pop()
                    stackNum.append(calc(c, num1, num2))

    while len(stackChr) > 0:
        c = stackChr.pop()
        if c == "(":
            break
        elif isOp(c):
            num2 = stackNum.pop()
            num1 = stackNum.pop()
            stackNum.append(calc(c, num1, num2))

    return stackNum.pop()


# TEST
stack=[]
stack2=[]
print("Enter an expression:")
expr = input()
while( expr == 'Up'):
    popped=stack.pop()
    print(popped)
    stack2.append(popped)
    expr = input()
    while(expr=="Up"):
        popped = stack.pop()
        print(popped)
        stack2.append(popped)
        expr = input()
    while(expr=="down"):
        popped=stack2.pop
        print(popped)

while(expr!='Up'):
    stack.append(expr)
    while(expr!= "Stop"):
        print("Enter an expression:")
        print ("Expression: " + expr)
        print ("infix: " + Infix(expr))
        expr = input()