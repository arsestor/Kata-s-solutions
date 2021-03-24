def to_postfix(infix):
    stack = []
    postfix = ''
    p = {'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
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
            while len(stack)!=0 and p[i]<=p[stack[0]]:
                postfix += stack.pop(0)
            stack.insert(0, i)
    while len(stack)!=0:
        postfix += stack.pop(0)
    return postfix
