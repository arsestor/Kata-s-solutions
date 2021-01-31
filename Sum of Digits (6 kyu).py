def digital_root(n):
    while int(len(str(n))) != 1:
        n=list(str(n))
        li = []
        for i in n:
            li.append(int(i))
        n = sum(li)
    return n
