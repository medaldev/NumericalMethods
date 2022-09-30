import sys
sys.path.append("C:\\Users\\sanch\\Desktop\\Лаба\\NumericalMethods")
from math import *
from lib.main_lib import *


def newton(x0,eps = None,max_iter = -1):

    i = 0

    x = copy_matrix(x0)
    while eps is None or eps_local > eps:
        if i > max_iter and max_iter > 0:
            break

        arr = mult_matrix(inv_matrix(f(*x0[0],*x0[1])),f(*x0[0],*x0[1])) 
        eps_local = norm_I(arr)
        x+=arr
        i+=1
         
    return eps_local

def f(x,y):

    return [[(y/cos(x*y+0.3)**2)-2*x,x/cos(x*y+0.3)**2],[8*x,2*y]]

def F(x,y):
    return [[tan(x*y+0,3)-x**2],[4*x**2+y**2]]
     
print(newton([[2],[3]],max_iter =10000))