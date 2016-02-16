"""

Make all possible parens

# 0
x =  a  +  b  +  c  +  d

# 1
x = (a  +  b) +  c  +  d
x = (a  +  b  +  c) +  d
x =  a  + (b  +  c) +  d
x =  a  + (b  +  c  +  d)
x =  a  +  b  + (c  +  d)

# 2
x = ((a  +   b) +   c)  +  d
x =  (a  +   b) +  (c   +  d)
x =  (a  +  (b  +   c)) +  d
x =   a  + ((b  +   c)  +  d)
x =   a  +  (b  +  (c   +  d))
"""

import math

def is_integer(x):
    """
    Not accurate for large numbers... precision
    """
    return int(x) == int(math.ceil(x))

def generate_equations():
    parens = [
        "x =  a  {0}  b  {1}  c  {2}  d",
        "x = (a  {0}  b) {1}  c  {2}  d",
        "x = (a  {0}  b  {1}  c) {2}  d",
        "x =  a  {0} (b  {1}  c) {2}  d",
        "x =  a  {0} (b  {1}  c  {2}  d)",
        "x =  a  {0}  b  {1} (c  {2}  d)",
        "x = ((a  {0}   b) {1}   c)  {2}  d",
        "x =  (a  {0}   b) {1}  (c   {2}  d)",
        "x =  (a  {0}  (b  {1}   c)) {2}  d",
        "x =   a  {0} ((b  {1}   c)  {2}  d)",
        "x =   a  {0}  (b  {1}  (c   {2}  d))"
    ]
    operators = ["+", "-", "*", "/"]

    lines = []
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                for p in parens:
                    lines.append(p.format(op1, op2, op3))

    for line in lines:
        print("    " + line)
        print("    if valid_number(x):")
        print("        nums.add(int(x))")

def valid_number(x):
    return x > 0 and is_integer(x)


def compute_nums(a, b, c, d):
    nums = set()
    x =  a  +  b  +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  + (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) +   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) +  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  +   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  +   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  +  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  + (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) +   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) +  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  +   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  +   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  +  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  + (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) +   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) +  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  +   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  +   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  +  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  +  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  + (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) +   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) +  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  +   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  +   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  +  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  - (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) -   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) -  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  -   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  -   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  -  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  - (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) -   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) -  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  -   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  -   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  -  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  - (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) -   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) -  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  -   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  -   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  -  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  -  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  - (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) -   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) -  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  -   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  -   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  -  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  * (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) *   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) *  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  *   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  *   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  *  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  * (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) *   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) *  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  *   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  *   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  *  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  * (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) *   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) *  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  *   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  *   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  *  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  *  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  * (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) *   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) *  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  *   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  *   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  *  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  / (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) /   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) /  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  /   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  /   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  /  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  / (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) /   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) /  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  /   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  /   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  /  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  / (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) /   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) /  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  /   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  /   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  /  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b) /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  +  b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  + (b  /  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  +  b  / (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  +   b) /   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +   b) /  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  +  (b  /   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  + ((b  /   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  +  (b  /  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  + (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) +   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) +  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  +   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  +   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  +  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  + (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) +   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) +  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  +   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  +   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  +  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  + (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) +   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) +  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  +   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  +   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  +  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  +  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  + (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) +   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) +  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  +   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  +   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  +  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  - (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) -   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) -  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  -   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  -   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  -  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  - (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) -   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) -  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  -   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  -   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  -  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  - (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) -   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) -  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  -   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  -   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  -  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  -  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  - (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) -   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) -  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  -   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  -   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  -  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  * (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) *   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) *  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  *   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  *   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  *  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  * (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) *   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) *  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  *   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  *   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  *  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  * (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) *   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) *  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  *   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  *   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  *  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  *  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  * (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) *   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) *  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  *   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  *   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  *  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  / (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) /   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) /  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  /   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  /   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  /  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  / (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) /   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) /  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  /   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  /   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  /  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  / (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) /   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) /  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  /   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  /   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  /  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b) /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  -  b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  - (b  /  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  -  b  / (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  -   b) /   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -   b) /  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  -  (b  /   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  - ((b  /   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  -  (b  /  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  + (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) +   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) +  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  +   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  +   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  +  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  + (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) +   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) +  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  +   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  +   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  +  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  + (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) +   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) +  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  +   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  +   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  +  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  +  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  + (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) +   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) +  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  +   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  +   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  +  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  - (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) -   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) -  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  -   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  -   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  -  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  - (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) -   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) -  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  -   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  -   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  -  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  - (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) -   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) -  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  -   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  -   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  -  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  -  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  - (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) -   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) -  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  -   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  -   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  -  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  * (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) *   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) *  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  *   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  *   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  *  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  * (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) *   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) *  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  *   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  *   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  *  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  * (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) *   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) *  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  *   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  *   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  *  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  *  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  * (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) *   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) *  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  *   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  *   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  *  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  / (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) /   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) /  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  /   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  /   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  /  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  / (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) /   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) /  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  /   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  /   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  /  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  / (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) /   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) /  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  /   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  /   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  /  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b) /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  *  b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  * (b  /  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  *  b  / (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  *   b) /   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *   b) /  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  *  (b  /   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  * ((b  /   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  *  (b  /  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) +  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  + (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) +   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) +  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  +   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  +   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  +  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) +  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  + (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) +   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) +  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  +   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  +   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  +  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) +  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  + (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) +   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) +  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  +   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  +   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  +  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) +  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  +  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  + (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) +   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) +  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  +   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  +   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  +  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) -  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  - (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) -   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) -  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  -   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  -   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  -  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) -  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  - (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) -   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) -  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  -   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  -   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  -  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) -  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  - (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) -   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) -  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  -   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  -   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  -  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) -  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  -  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  - (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) -   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) -  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  -   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  -   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  -  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) *  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  * (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) *   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) *  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  *   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  *   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  *  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) *  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  * (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) *   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) *  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  *   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  *   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  *  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) *  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  * (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) *   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) *  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  *   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  *   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  *  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) *  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  *  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  * (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) *   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) *  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  *   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  *   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  *  (c   /  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) /  c  +  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c) +  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  / (c  +  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) /   c)  +  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) /  (c   +  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  /   c)) +  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  /   c)  +  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  /  (c   +  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) /  c  -  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c) -  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  / (c  -  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) /   c)  -  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) /  (c   -  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  /   c)) -  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  /   c)  -  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  /  (c   -  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) /  c  *  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c) *  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  / (c  *  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) /   c)  *  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) /  (c   *  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  /   c)) *  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  /   c)  *  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  /  (c   *  d))
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b) /  c  /  d
    if valid_number(x):
        nums.add(int(x))
    x = (a  /  b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c) /  d
    if valid_number(x):
        nums.add(int(x))
    x =  a  / (b  /  c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  a  /  b  / (c  /  d)
    if valid_number(x):
        nums.add(int(x))
    x = ((a  /   b) /   c)  /  d
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /   b) /  (c   /  d)
    if valid_number(x):
        nums.add(int(x))
    x =  (a  /  (b  /   c)) /  d
    if valid_number(x):
        nums.add(int(x))
    x =   a  / ((b  /   c)  /  d)
    if valid_number(x):
        nums.add(int(x))
    x =   a  /  (b  /  (c   /  d))
    if valid_number(x):
        nums.add(int(x))

    return nums

if __name__ == "__main__":
    # generate_equations()

    nums = compute_nums(1, 2, 3, 4)
    nums = list(nums)
    nums.sort()
    for n in nums:
        print(n)

