def solution(string,markers):
    elements = string.splitlines()
    for i in elements:
        for j in i:
            if j in markers:
                elements[elements.index(i)] = i[:i.index(j)].strip()
                break
    return r'\n'.join(elements).encode().decode('unicode_escape')
