def fake_bin(x):
    return ''.join([str(0) if int(i)<5 else str(1) for i in x])
