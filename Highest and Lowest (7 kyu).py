import re

def high_and_low(numbers):
    a = [int(i) for i in re.findall(r'[-]?\d+', numbers)]
    return str(max(a)) +" "+ str(min(a))
