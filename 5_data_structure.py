#----------------------------------------------------------
#Tuples
t = (1, 2.5, 'data') 
type(t) 

t = 1, 2.5, 'data'
type(t)

t[2] 

type(t[2])

t.count('data') 
t.index(1)  

#----------------------------------------------------------
#Lists
l = [1, 2.5, 'data'] 
l[2] 

#----------------------------------------------------------
#Disctionaries
d = { 'Name' : 'Angela Merkel', 'Country' : 'Germany', 'Profession' : 'Chancelor', 'Age' : 64 } 
type(d) 
print(d['Name'], d['Age']) 

d.keys() 

d.values() 

d.items() 

#----------------------------------------------------------
#Sets
s = set(['u', 'd', 'ud', 'du', 'd', 'du']) 
s 
t = set(['d', 'dd', 'uu', 'u'])

#All of s and t.
s.union(t) 

#Items in both s and t.
s.intersection(t) 

#Items in s but not in t.
s.difference(t) 

#Items in t but not in s.
t.difference(s) 

#Items in either s or t but not both.
s.symmetric_difference(t) 

#----------------------------------------------------------
#Arrays With Python Lists
v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = [v, v, v] 
m 

v1 = [0.5, 1.5] 
v2 = [1, 2] 
m  = [v1, v2] 
c  = [m, m] 

c 

c[1][1][0]

#----------------------------------------------------------
#Numpy Arrays

#Import the numpy package
import numpy as np 

#Create an ndarray object out of a list object with floats
a = np.array([0, 0.5, 1.0, 1.5, 2.0])
a 
type(a)

#Create an ndarray object out of a list object with strs
a = np.array(['a', 'b', 'c'])
a

#np.arange() works similar to range()
a = np.arange(2, 20, 2)
a

#… but takes as additional input the dtype parameter.
a = np.arange(8, dtype=float)
a

#With one-dimensional ndarray objects, indexing works as usual.
a[5:]
a[:2]

#Built-in methods, operations on arrays
a.sum()
a.std()
a.cumsum()

l = [0., 0.5, 1.5, 3., 5.]
2 * l

#By contrast, working with ndarray objects implements a proper scalar multiplication
a
2 * a

#This calculates element-wise the square values.
a ** 2

#This interprets the elements of the ndarray as the powers
2 ** a

#This calculates the power of every element to itself.
a ** a

#This calculates element-wise the square values.
a ** 2

#This interprets the elements of the ndarray as the powers
2 ** a

#This calculates the power of every element to itself.
a ** a

#Calculates the exponential values element-wise.
np.exp(a)

#Calculates the square root for every element
np.sqrt(a)

#Calculates the square root for a Python float object
#import math
#math.sqrt(a)  #It doesn't work with arrays, only floats!

import timeit

import_module_np = "import numpy as np"
print(timeit.timeit('np.sqrt(2.5)',setup=import_module_np))
#1.5095000000001164

import_module_math = "import math"
print(timeit.timeit('math.sqrt(2.5)',setup=import_module_math))
#0.2866000010001244

#For float operations, we want to use the math library!

c = np.zeros((2, 3), dtype='i', order='C')
c

d = np.ones_like(c, dtype='float16', order='C')
d

e = np.empty((2, 3, 2))
e

#-------------------------------------------------------
#Reshaping and Resizing
g = np.arange(15)
g

g.shape
np.shape(g)

g.reshape((3, 5))

h = g.reshape((5, 3))
h 

h.transpose()

g
np.resize(g, (1, 5))

#Stacking
h
np.hstack((h, 2 * h))

#-------------------------------------------------------
#Boolean Arrays
h 
h > 8 

np.where(h > 7, 1, 0)

#-------------------------------------------------------
#Speed Comparison
import timeit

timeit.timeit("[random.gauss(0, 1) for j in range(5000)]", setup="import random", number=10)
#0.09359999999992397

timeit.timeit("numpy.random.standard_normal((5000,1))", setup="import numpy", number=10)
#0.0025000000000545697


#-------------------------------------------------------
#Structured ndarray

#The complex dtype is composed
dt = np.dtype([('Name', 'S10'), ('Age', 'i4'), ('Height', 'f'), ('Children/Pets', 'i4', 2)])

#The structured ndarray is instantiated with two records
s = np.array([('Smith', 45, 1.83, (0, 1)), ('Jones', 53, 1.72, (2, 2))], dtype=dt)
type(s) 

#The object type is still ndarray.

#-------------------------------------------------------
#Basic Vectorization
np.random.seed(100) 

#Create an ndarray object with random numbers
r = np.arange(12).reshape((4, 3)) 

#Create a second ndarray object with random numbers
s = np.arange(12).reshape((4, 3))*0.5

r 

s 

#Element-wise addition as a vectorized operation (no looping).
r + s 

#During scalar addition, the scalar is broadcast and added to every element.
r + 3 

#simple Python function implementing a linear transform on parameter x.
def f(x):
    return 3 * x + 5 

#The function f() applied to a Python float object.
f(0.5) 

#The same function applied to an ndarray object, resulting in a vectorized and element-wise evaluation of the function.
f(r)