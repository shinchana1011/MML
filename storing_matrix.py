from sympy import *
import numpy as np
from sympy import symbols,sin,cos
x0,x1,x2,x3=symbols('x0 x1 x2 x3')
f=sp.Matrix([[sin(x0+2*x1),2*x1+x3],[2*x0+x2,cos(2*x2+x3)]])
k=sp.Matrix([[x0,x1],[x2,x3]])
display("F Matrix:",f)
display("K Matrix:",k)
reshape_f=f.reshape(4,1).jacobian(k.reshape(4,1))
J_matrix=ImmutableDenseNDimArray(reshape_f).reshape(2,2,2,2)
print("the gradient of matrix is:")
display(J_matrix)
