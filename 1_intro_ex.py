#1: numpy example
#For example, let’s build some arrays:
import numpy as np                      #Load the library
a = np.linspace(-np.pi, np.pi, 100)     #Create even grid from -π to π 
b = np.cos(a)                           #Apply cosine to each element of a 
c = np.sin(a)                           #Apply sin to each element of a

#Now let’s take the inner product
b @ c

#2: scipy example
#Integrate the Std Normal PDF using Gaussian quadrature 
from scipy.stats import norm 
from scipy.integrate import quad

ϕ            = norm()                  #Standard Normal Distribution
value, error = quad(ϕ.pdf, -2, 2)      #Integrate the Std Normal PDF using Gaussian quadrature 
value

#3: matplotlib example
import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 10, 100)         #make data x
y = 4 + 2 * np.sin(2 * x)           #make data y
fig, ax = plt.subplots()            
ax.plot(x, y, linewidth=2.0)        #plot x,y
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()

#4: sympy example
from sympy import Symbol
x, y = Symbol('x'), Symbol('y')    #Treat 'x' and 'y' as algebraic symbols x + x + x + y
expression = (x + y)**2 
expression.expand()

#5: pandas example
import pandas as pd 
np.random.seed(1234)

# 5x2 matrix of N(0, 1) random draws 
dates = pd.date_range('2010-12-28', periods=5)
data  = np.random.randn(5, 2)
df    = pd.DataFrame(data, columns=('price', 'weight'), index=dates) 
print(df)
df.mean()