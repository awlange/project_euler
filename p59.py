"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for
Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
"halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge
that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values
in the original text.
"""

import time
import string

COMMON_WORDS = [' ', 'the', 'an', 'and', 'but', 'him', 'her', 'it', 'this', 'that', 'is', 'was', 'be', 'will']


def get_codes():
    codes = []
    with open("/Users/alange/programming/projectEuler/files/cipher1.txt") as f:
        for line in f:
            codes += line.strip('\n').split(',')
    return [int(k) for k in codes]


def decode(key, codes):
    okeys = [ord(k) for k in (key * 400 + key[0])]
    xor = ''
    i = 0
    for c in codes:
        xor += chr(okeys[i] ^ c)
        i += 1
    return ''.join(xor)


def contains_common_words(message):
    thresh = 8
    n = 0
    for word in COMMON_WORDS:
        if word in message:
            n += 1
            if n >= thresh:
                return True
    return False


def ascii_sum(message):
    total = 0
    for l in message:
        total += ord(l)
    return total


LETTERS = [l for l in string.ascii_lowercase]


def main():
    ts = time.time()

    found = False
    message = ''

    codes = get_codes()
    for a in LETTERS:
        for b in LETTERS:
            for c in LETTERS:
                key = a + b + c
                message = decode(key, codes)
                if contains_common_words(message):
                    print message
                    found = True
                    break
            if found:
                break
        if found:
            break

    print "ASCII sum: ", ascii_sum(message)
    print "Time: {}".format(time.time() - ts)


if __name__ == '__main__':
    main()