def encode(s):
    if s == '':
        return [""]
    matrix = []
    string = [[i for i in s][i-1] for i in range(len([i for i in s]))]
    matrix.append(string)
    while string != [i for i in s]:
        string = [string[i-1] for i in range(len(string))]
        matrix.append(string)
    if s!='':
        return ''.join([i[-1] for i in sorted(matrix)]), sorted(matrix).index([i for i in s])

def decode(s, n):
    if s == '':
        return ""
    temp = [s[i] for i in range(len(s))]
    string = [s[i] for i in range(len(s))]
    for k in range(len(temp)):
        for i in range(len(string)):
            string[i] = temp[i]+string[i]
        string = sorted(string)
    return [i[0:-1] for i in string][n-1]
