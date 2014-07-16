N = 1001
seq = [1]

stride = 2
i = 1
dir = 1
while i < N*N:
    i += stride
    seq.append(i)
    if dir % 4 == 0:
        stride += 2
    dir += 1

print sum(seq, 0)

