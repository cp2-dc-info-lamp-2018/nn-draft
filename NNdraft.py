# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:47:41 2018

@author: arsil
"""
import math
in_ = ([1,2,3]) 

w1 = ([[3,6,0,1], 
       [0,0,2,1],
       [1,4,0,1]])

w2 = ([[0,0], 
       [1,2],
       [2,3],
       [1,0]])

r = ([])
A = 0
for i in range(len(w1[0])): 
    A = 0
    for j in range(len(in_)): 
        A += in_[j] * w1[j][i]     
    r.append(A)


def sigmoid(x):
  return 1 / (1 + math.exp(-x))

b = 0
hidden = ([])
for i in range (len(r)):
    b = sigmoid (r[i])
    hidden.append(b) 



out = ([])
for i in range(len(w2[0])): 
    c = 0
    for j in range(len(hidden)): 
        c += hidden[j] * w2[j][i]     
    out.append(c)

z = 0
outsig1 = ([])
z = sigmoid (out[0])
outsig1.append(z) 
    
print (outsig1)

x = 0
outsig2 = ([])
x = sigmoid (out[1])
outsig2.append(x) 
    
print (outsig2)




