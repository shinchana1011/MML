from sympy import *
x,y=symbols('x y')
f=x-y+2*x+2*y*x+y
grad_f=Matrix([diff(f,x),diff(f,y)])
print("gradient of matrix:")
display(grad_f)
x0=Matrix([0,0])
G1=grad_f.subs({x:x0[0],y:x0[1]}).evalf()
H=hessian(f,[x,y])
print("hessian matrix:")
display(H)

for i in range(3):
    H1=H.subs({x:x0[0],y:x0[1]}).evalf()
    s=-G1
    x0=x0-(H1.inv()*G1)
    G1=grad_f.subs({x:x0[0],y:x0[1]}).evalf()
    if all(abs(val)<=0 for val in G1):
        break
print("local minimum found at:")
display(x0)
f1=f.subs({x:x0[0],y:x0[1]}).evalf()
print("the minimunm value function is:",f1)
    
