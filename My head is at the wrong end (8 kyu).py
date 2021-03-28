def fix_the_meerkat(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr
