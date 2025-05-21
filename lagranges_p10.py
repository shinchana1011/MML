from sympy import *

x, y,z, l =symbols('x y z l')

f=(x-3)**2+(y-4)**2+(z-12)**2 
g = x**2 + y**2+z**2 - 1 
L = f + l * g
L_x = diff(L, x)
L_y = diff(L, y)
L_z = diff(L, z)
L_l = diff(L, l)
solutions = solve([L_x, L_y, L_z,L_l], [x, y,z, l])
print("Solutions:", solutions)
