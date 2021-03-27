def is_vow(inp):
    for i in range(len(inp)):
        if inp[i] == 117:
            inp[i] = 'u'
        elif inp[i] == 97:
            inp[i] = 'a'
        elif inp[i] == 101:
            inp[i] = 'e'
        elif inp[i] == 111:
            inp[i] = 'o'
        elif inp[i] == 105:
            inp[i] = 'i'
    return inp
