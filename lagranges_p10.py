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



OR


from sympy import *
x,y,z,lamda=symbols('x y z lamda')
cir=x**2+y**2+z**2-1
f=(x-3)**2+(y-4)**2+(z-12)**2
l=f+lamda*cir
sol=solve((diff(l,x),
           diff(l,y),
           diff(l,z),
           diff(l,lamda)),
            (x,y,z,lamda),dict=True)
final=[]
for i in sol:
  print("the x,y,z is",((i[x], i[y], i[z])))
  final.append(f.subs(i))
print("the minima is",min(final))
print("the maxima is",max(final))



from sympy import *
x,y,z,lamda=symbols('x y z lamda')
cir=x**2+y**2+z**2-1
f=(x-3)**2+(y-4)**2+(z-12)**2
l=f+lamda*cir
sol=solve((diff(l,x),
           diff(l,y),
           diff(l,z),
           diff(l,lamda)),
            (x,y,z,lamda),dict=True)
final=[]
point=[]
for i in sol:
  print("the x,y,z is",((i[x], i[y], i[z])))
  point.append((i[x], i[y], i[z]))
  final.append(f.subs(i))
min_=min(final)
max_=max(final)
print("the minima is funtion is ",min_,"point is ",point[final.index(min_)])
print("the maxima is funtion is ",max_,"point is ",point[final.index(max_)])

