def digital_sum(n):
    sn = str(n)
    total = 0
    for digit in sn:
        total += int(digit)
    return total

most = 0
for a in range(1, 100):
    for b in range(1, 100):
        most = max(most, digital_sum(a**b))

print most