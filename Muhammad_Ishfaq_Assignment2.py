# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:07:03 2018

@author: ishfaq
"""
import numpy as np # import numpy to use numpy functions like power function 
import math #  to calcualte mathematical functions math library is imported
import time ## timeit will show the time proecessing how  long it tale to execute the code. 
import matplotlib.pyplot as plt
from time import clock
from scipy.linalg import eigh as largest_eigh
from scipy.sparse.linalg.eigen.arpack import eigsh as largest_eigsh
#import sys # system efficieny is used to calcualte functinos 
size = (1000) #   to calcualte total time taken to process the edxcution of this code. *1000 means we want to 
# to know the time taken to execute the code in mili seconds 
# implementation 3 approach. 
N = int(input('Please enter the diemention you want (N*N):'))
N = (N)
d = np.random.random((N,N)) -0.5

print(d)
start = time.time()
print((time.time()-start)*500)# this is the similar way to implement the mehtod like it has been 
# implemented twice in this code see below to find other eigh and eigsh values and iterations to 
# compute the total time consumded to calculate largest values of eigenvalues and eigenvectors. 
print("d :  \n",d)
# now we will find out the eigenvalues of 4 by 4 matrix 
print("Eigenvalues :", np.linalg.eigvals(d))
# to find eigenvectors of the n by n matrix we will use eigenvector method. 
eigenvalue,eigenvector = np.linalg.eig(d)
print("First tuple of eig:", eigenvalue)
print("Second tuple of eig:", eigenvector)
start = time.time()
print((time.time()-start)*100)

tol = int(input('input error tolerance (tol): ')) # to get input error tolerance, greater values and 
# more tolerance erros to computing values of the tolerance. 
start = time.time()
print((time.time()-start)*100)
# Using dot product we implement the new method 
 
np.set_printoptions(suppress=True)
np.random.seed(3)# to calculate the values of time with random seed in this case we have given
# 0 and we can chnage it to many other things like. let sy to value 2 or we can implement for loop
# to iterate the function and get required values. 
N=5000
k=10
X = np.random.random((N,N)) - 2.5
X = np.dot(X, X.T) #create a symmetric matrix

# Benchmark the dense routine
start = clock()
evals_large, evecs_large = largest_eigh(X, eigvals=(N-k,N-1))
elapsed = (clock() - start)
print("eigh elapsed time: ", elapsed)
print(X)
# Benchmark the sparse routine
start = clock()
evals_large_sparse, evecs_large_sparse = largest_eigsh(X, k, which='LM')
elapsed = (clock() - start)
print("eigsh elapsed time: ", elapsed)
# defining power method 


