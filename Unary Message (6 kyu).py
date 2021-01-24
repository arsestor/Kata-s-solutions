import re

def send(s):
    return ' '.join([f'0 {len(i)*"0"}' if '1' in i else f'00 {len(i)*"0"}' for i in re.findall("1+|0+", ''.join(f'{i:07b}' for i in map(ord, s)))])

def receive(s):
    return re.sub(".{7}", lambda x: chr(int(x.group(), 2)), ''.join([("1" if i[:i.find(' ')] == '0' else "0") * len(i[i.find(' ')+1:]) for i in re.findall("0+ 0+", s)]))
