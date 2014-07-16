"""
A common security method used for online banking is to ask the user for three random
characters from a passcode. For example, if the passcode was 531278, they may ask for the
2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as
to determine the shortest possible secret passcode of unknown length.
"""

import time
from p32 import all_permutations


def get_keys():
    keys = []
    # Presorted and removed non-unique entries
    with open("/Users/alange/programming/projectEuler/files/keylog_sortu.txt") as f:
    # with open("/Users/alange/programming/projectEuler/files/keylog_small.txt") as f:
        for line in f:
            keys.append(line.split()[0])
    return keys


# Brute force solution: 73162890


def test_key(passcode, key):
    k0 = key[0]
    k1 = key[1]
    k2 = key[2]
    if k0 in passcode and k1 in passcode and k2 in passcode:
        ik0 = passcode.index(k0)
        ik1 = passcode.index(k1)
        ik2 = passcode.index(k2)
        if ik0 < ik1 < ik2:
            return True
    return False


digits = [str(x) for x in [0, 1, 2, 3, 6, 7, 8, 9]]
def contains_digits(sn):
    for d in sn:
        if d not in digits:
            return False
    return True


# 8 unique digits, so should start at smallest 8 digit number with all unique digits: 10 234 567
# However, in the list, 4 and 5 do not appear. So, actually start at: 10 236 789
def brute_force(keys):
    i = 10236789
    passcode = str(i)
    while 1:
        # Digit check
        if contains_digits(passcode):
            # Key check
            all_pass = True
            for key in keys:
                if not test_key(passcode, key):
                    all_pass = False
                    break

            if all_pass:
                break

        i += 1
        passcode = str(i)

    return passcode


def permutation_approach(keys):
    result = ""
    for perm in all_permutations(digits):
        passcode = ''.join(perm)
        all_pass = True
        for key in keys:
            if not test_key(passcode, key):
                all_pass = False
                break

        if all_pass:
            result = passcode
            break
    return result


def main():
    t_start = time.time()

    # small solution: 168029

    keys = get_keys()

    # passcode = brute_force(keys)
    passcode = permutation_approach(keys)

    print "Passcode: ", passcode
    print "Run time: {}".format(time.time() - t_start)


if __name__ == '__main__':
    main()
