from math import *

a = 2.0
b = 4.0
eps = 0.0001

def f(x):
    return 3*x - 4*log(x) - 5


def chord_m(a, b, eps):

    prevx = a

    while True:
        xk = a - f(a) * (b - a) / (f(b) - f(a)) #высчитываем точку

        if f(xk)==0.0:
            return xk
        elif f(a)*f(xk)<0:
            b = xk
        else:
            a = xk
        
        if abs(xk-prevx) <= eps:
            break

        prevx = xk
        
    return xk 

print(chord_m(a,b, 0.0001))