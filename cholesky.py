from sympy import *
def cholesky_decomposition(A):
    n=A.shape[0]
    L=Matrix.zeros(n)
    for i in range(n):
        for j in range(i+1):
            if i==j:
                L[i,j]=sqrt(A[i,j]-sum(L[i,k]**2 for k in range(i)))
            else:
                L[i,j]=(A[i,j]-sum(L[i,k]*L[j,k] for k in range(j)))/L[j,j]
    return L
# M=Matrix(([1,-2,2],[-2,5,-3],[2,-3,6]))
M=Matrix(([1,2,-1],[2,7,-8],[-1,-8,15]))
B=Matrix(([-5,-19,25]))
L=cholesky_decomposition(M)
Lt=L.T
print("matrix is:\n")
display(M)
print("L transpose:\n")
display(Lt)
P=L.row_join(B)
Y=Matrix(list(linsolve(P))).T
Q=Lt.row_join(Y)
X=Matrix(list(linsolve(Q))).T
print("solution matrix of X:")
display(X)
