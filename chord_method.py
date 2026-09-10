from math import *

a = 2.0
b = 4.0
eps = 0.0001

def f(x):
    return 3*x - 4*log(x) - 5

def chord_m(a, b, eps):

    prevx = a #инициализируем переменную, которая будет хранить предыдущую точку

    while True:
        xk = a - f(a) * (b - a) / (f(b) - f(a)) #высчитываем точку

        if f(xk)==0.0: #проверяем, попали ли мы в нее сразу
            return xk
        elif f(a)*f(xk)<0: #если разные знаки, сдвигаем границу 
            b = xk
        else:
            a = xk #аналогично сдвигаем границу

        if abs(xk-prevx) <= eps:
            break

        prevx = xk #обновляем предыдущую точку

    return xk

print(chord_m(a,b, 0.0001))