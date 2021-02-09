def validate(n):
    n = str(n)[::-1]
    for i in range(1,len(n)+1):
        if i % 2 == 0:
            dn = int(n[i-1])*2
            if dn > 9:
                dn -= 9
            n = n[:i-1]+str(dn)+n[i:]
    return sum(map(int, n[::-1]))%10==0
