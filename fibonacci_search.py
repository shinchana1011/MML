
#fibonacci search
from sympy import *
x=symbols('x')
a,b,n=-2,3,6
f=x**2-2.6*x+2
fi=[1,1,2,3,5,8,13]

for k in range(1,7):
  l=fi[n-k]*(b-a)/fi[n-k+1]
  xk=b-l
  yk=a+l
  print()
  print(f"Iteration {k}")
  print(f"l : {l:.4f}")

  print(f"x : {xk:.4f}")
  print(f"y : {yk:.4f}")
  fx=f.subs(x,xk)
  fy=f.subs(x,yk)
  print(f"fx : {fx:.4f}")
  print(f"fy : {fy:.4f}")
  if fx>fy:
    a=xk
  elif fx<fy:
    b=yk
  
print(f"the value of a is {a:.4f} b is")
x_ans=(a+b)/2
print("the value of function is",f.subs(x,x_ans))


OR 



from sympy import *
def f(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    l,m=0,1
    for _ in range(2,n+1):
        l,m=m,l+m
    return m
x = symbols('x')
f_ex = x**2 - 2.6*x + 2
a = -2
b = 3
n = 6
print(f"iteration\t l \t xk \t{yk:.4f}\t{f_xk:.4f}\t{f_yk:.4f}\t[{a:.4f},{b:.4f}]")
for i in range(n):
    l=f(n-i)*(b-a)/f(n-i+1)
    xk=b-l
    yk=a+l
    f_xk=f_ex.subs({x:xk})
    f_yk=f_ex.subs({x:yk})
    if f_xk > f_yk:
        a,b=xk,b
    elif f_xk<f_yk:
        a,b=a,yk
    else:break
    print(f"{i+1}\t\t{l:.4f}\t{xk:.4f}\t{yk:.4f}\t{f_xk:.4f}\t{f_yk:.4f}\t[{a:.4f},{b:.4f}]")
x_res=(a+b)/2
display('x-value:',x_res,'function value:',f_ex.subs({x:x_res}))
