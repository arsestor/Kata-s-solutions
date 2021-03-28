def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for i in range(len(spl)):
        if len(spl[i]) > longest:
            longest = len(spl[i])
    return longest
