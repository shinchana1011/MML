import cv2
from google.colab.patches import cv2_imshow
import numpy as np
img=cv2.imread('strawberry-small.jpg',0)
cv2_imshow(img)
A=img
print("\nGrayscale image matrix : \n",A)
# convert to svd
U,S,Vt=np.linalg.svd(A)
k=int(input("\nenter the value for compression:"))
U=U[:,:k]
S=np.diag(S[:k])
Vt=Vt[:k,:]
new_A=np.dot(U,np.dot(S,Vt))
print("\n compressed matrix:\n",new_A)
#convert matrix to image
cv2_imshow(new_A)
