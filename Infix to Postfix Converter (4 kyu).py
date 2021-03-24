def to_postfix(infix):
    stack = []
    postfix = ''

    def preced(i):
        if i == '+' or i == '-':
            return 1
        elif i == '*' or i == '/':
            return 2
        elif i == '^':
            return 3
        else:
            return 0

    for i in infix:
        if i.isdigit():
            postfix += i
        elif i == '(':
            stack.insert(0,i)
        elif i == '^':
            stack.insert(0,i)
        elif i == ')':
            while len(stack)!=0 and stack[0]!='(':
                postfix += stack.pop(0)
            stack.remove('(')
        else:
            while len(stack)!=0 and preced(i)<=preced(stack[0]):
                postfix += stack.pop(0)
            stack.insert(0, i)
    while len(stack)!=0:
        postfix += stack.pop(0)
    return postfix
