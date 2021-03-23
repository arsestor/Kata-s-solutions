def next_bigger(n):
    n = list(str(n))
    if -1 in [1 if n[i]>=n[i+1] else -1 for i in range(len(n)-1)]:
        for i in range(len(n)-1,-1,-1):
            print(i)
            if i == len(n)-1:
                continue
            if n[i]<n[i+1]:
                n[len(n)-1-n[::-1].index(min(n[i+1:]))], n[i] = n[i], n[len(n)-1-n[::-1].index(min(n[i+1:]))]
                first = n[:i+1]
                second = n[i+1:]
                second.sort()
                print(int(''.join(first+second)))
                break
    else:
        print(-1)


next_bigger(1234567890)  # 1234567089 should equal 1234567908
