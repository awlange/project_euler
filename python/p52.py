def check(n):
    sn = str(n)
    if len(str(6*n)) > len(sn):
        return False
    for m in range(2, 7):
        smn = str(m*n)
        for d in sn:
            if d not in smn:
                return False

    return True

i = 10
while not check(i):
    i += 1

print i