import stack as st

def evalPostfix(expr):
    s = st.Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if token=='+': s.push(val1+val2)
            elif token=='-': s.push(val1-val2)
            elif token=='*': s.push(val1*val2)
            elif token=='/': s.push(val1/val2)
        else:
            s.push(float(token))
    return s.pop()

def precedence(op):
    if op=='(' or op==')' : return 0
    elif op=='+' or op=='-' : return 1
    elif op=='*' or op=='/' : return 2
    else: return -1

def Infix2Postfix(expr):
    s = st.Stack()
    output = []
    for temp in expr:
        if temp in "+-/*":
            while not s.isEmpty():
                op = s.peek()
                if precedence(temp) <= precedence(op):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(temp)
        elif temp=='(':
            s.push('(')
        elif temp==')':
            while True:
                op = s.pop()
                if op=='(': break
                else:
                    output.append(op)
        else:
            output.append(temp)
    while not s.isEmpty():
        output.append(s.pop())
    return output
