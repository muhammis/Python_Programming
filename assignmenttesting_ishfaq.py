# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:48:01 2018

@author: ishfaq
"""
import time
import numpy as np
#Approach # 1
from numpy import linalg as LA
size = 2000
A = np.matrix([[0,11,-5] , [-2,17,-7] , [-4,26,-10]])
X0 = np.matrix([1,1,1]).T
iterations = 3

for i in range (iterations):
    A = A*A

x = A*X0
norm = LA.norm(x)
print(x/norm)
print(LA.eig(A)[1])

start = time.time()
print((time.time()-start)*1000)


