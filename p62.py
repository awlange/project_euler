"""
Find the smallest cube for which exactly five permutations of its digits are cube.
"""

# Note: I am proud of my solution! It fucking rocked.

import time


def transform_n_to_mask(n):
    sn = str(n)
    mask = [0 for _ in range(11)]  # additional leading number 9 to make easy to convert to int
    mask[0] = 9
    for d in sn:
        mask[int(d)+1] += 1
    smask = ''
    for x in mask:
        smask += str(x)
    return int(smask)


def main():

    start = time.time()

    mask_map = {}
    n = 0
    while True:
        n += 1

        n3 = n**3
        mask = transform_n_to_mask(n3)
        mask_val = mask_map.get(mask, [])
        mask_val.append(n3)
        mask_map[mask] = mask_val

        if n % 50 == 0:
            # Check if any mask values are of length 5
            found = False
            for key in mask_map:
                if len(mask_map[key]) == 5:
                    print mask_map[key]
                    found = True

            if found:
                break

    print "Time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()