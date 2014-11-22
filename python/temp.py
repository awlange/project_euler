def f(x):
    return 2*x


def g(x):
    return 3*x


def foo(x, func):
    print func(x)


foo(2, f)
foo(2, g)