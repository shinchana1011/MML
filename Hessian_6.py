from sympy import *
x,y=symbols('x y')
f=x**2+(y**2)-4*x+2*y
print("the function is")
display(f)
fx=diff(f,x)
fy=diff(f,y)
h=hessian(f, (x, y))
s=solve((fx,fy), (x, y))
x=h.eigenvals()
print("the critical point is")
display(s)
print("the hessian matrix")
display(h)
print("the hessian matrix after substitution")
h1=h.subs(s)
display(h1)
print("the eigen values of hessian matrix")
val=h1.eigenvals()
display(val)

if all(i > 0 for i in val.values()):
    print("The function is a local minima")
    f1=f.subs(s)
    print("the minimum value of funtion is",f1)
elif all(i < 0 for i in val.values()):
    print("The function is a local maxima")
    f1=f.subs(s)
    print("the maximum value is",f1)
elif any(i > 0 for i in val.values()) and any(i < 0 for i in val.values()):
    print("The function is a saddle point")
elif any(i == 0 for i in val.values()):
    print("The function needs to be investigated")A
