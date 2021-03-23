input = "(5-4-1)+9/5/2-7/1/7"
output_n = "54-1-95/2/+71/7/-"

priority = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':0}
stack = []

output = ''
digits = [i for i in input if i.isdigit()]
for i in input:
    if i.isdigit():
        output += i
        if i == input[-1] and len(output) != 1:
            for i in stack:
                output += i
        continue
    if not stack:
        stack.insert(0,i)
    else:
        if i == ')':
            while '(' in stack:
                if stack[0] != '(':
                    output += stack[0]
                del stack[0]
            continue
        if priority[i]==priority[stack[0]] and stack[0]!='^':
            output += stack[0]
            del stack[0]
        elif i=='^' and stack[0]=='^':
            stack.insert(0,i)
        if priority[i]>priority[stack[0]]:
            stack.insert(0,i)
        if i == '(':
            stack.insert(0,i)


print(output, output_n)
