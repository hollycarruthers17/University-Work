import numpy as np 
import matplotlib.pyplot as plt 
import scipy
from scipy import integrate

x = np.linspace(0.0,2.0,51)

x

f_x =  ([1.        , 1.03918944, 1.0767164 , 1.11252084, 1.14654549,
       1.17873591, 1.2090406 , 1.23741109, 1.26380198, 1.28817106,
       1.31047934, 1.33069113, 1.3487741 , 1.36469932, 1.37844131,
       1.38997809, 1.3992912 , 1.40636574, 1.4111904 , 1.41375746,
       1.4140628 , 1.41210595, 1.40789002, 1.40142178, 1.39271155,
       1.38177329, 1.36862448, 1.35328617, 1.33578289, 1.31614264,
       1.29439684, 1.27058028, 1.24473107, 1.21689055, 1.18710327,
       1.15541687, 1.12188206, 1.08655247, 1.04948463, 1.01073784,
       0.97037408, 0.92845793, 0.88505645, 0.84023907, 0.79407748,
       0.74664554, 0.69801912, 0.64827602, 0.59749582, 0.54575976,
       0.49315059])

plt.scatter(x,f_x, label = "Plot of Unknown Function") 
plt.legend() 
plt.show() 


#1 Compute the forward, backward, and central derivative of the function using the finite differences formula.
# Forward Derivative 

f_prime_x          = np.diff(f_x)/0.04
f_prime_x_central = np.subtract(f_x[2:],f_x[:-2])/0.04


#2 Plot the derivative against its corresponding domain

plt.scatter(x[:-1],f_prime_x,label = "Forward Derivative") 
plt.scatter(x[1:],f_prime_x,label = "Backward Derivative") 
plt.scatter(x[1:-1],f_prime_x_central,label = "Central Derivative") 
plt.legend() 
plt.show()


#3 Compute the left and right Rieman integral of the function given in fx for each subinterval in the domain. 
#  Add the integrals obtained in each subinterval to obtain the global integral.

#Riemann  Integrals
I_sub_int_left = np.dot(0.04,f_x[:-1])
I_sub_int_left

np.sum(I_sub_int_left)

I_sub_int_right = np.dot(0.04,f_x[1:])
I_sub_int_right

np.sum(I_sub_int_right)

#4 Compare your result in question 3 with the outcome obtained using Simpson’s rule. 

scipy.integrate.simpson(f_x,x)
