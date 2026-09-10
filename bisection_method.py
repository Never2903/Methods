from math import *

a = 2.0
b = 4.0
eps = 0.0001

def f(x):
    return 3*x - 4*log(x) - 5

def bisection(a, b, eps):
    if f(a) * f(b) > 0:
        return 'Корней нет'
    while abs(b - a) > eps:
        c = (a + b) / 2.0
        if abs(f(c)) < eps:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

k = bisection(a, b, eps)
print(k)