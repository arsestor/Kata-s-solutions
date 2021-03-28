def enough(cap, on, wait):
    return list(map(lambda x: max(x,0),[on+wait-cap]))[0]
