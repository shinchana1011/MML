from sympy import *
x,y=symbols('x y')
f=x-y+2*(x**2)+2*x*y+y**2
print("the function is")
display(f)

grad_f = Matrix([diff(f, x), diff(f, y)])
print("the gradient function is")
display(grad_f)
x0=Matrix([0,0])
grad_fs = grad_f.subs({x: x0[0], y: x0[1]}).evalf()
display(grad_fs)
h=hessian(f,(x,y))
print("the hessian matrix")
display(h)
tolerance =0.01
max_iter = 25
iter_count =0
while True:
    s1=-grad_fs
    h1=h.subs({x: x0[0], y: x0[1]}).evalf()
    
    lamda = (s1.T * s1)[0] / (s1.T * h1 * s1)[0].evalf()
    
    x0 = x0 + lamda * s1 
    grad_fs = grad_f.subs({x: x0[0], y: x0[1]}).evalf()
    print("point is :")
    display(x0)    
    f1=f.subs({x: x0[0], y: x0[1]}).evalf()
    print("the optimum value of function is",f1)  
    iter_count += 1
    if all(abs(val) < tolerance for val in grad_fs) or iter_count > max_iter:
        break
