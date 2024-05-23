#1 Import the numpy library (as np), the matplotlib.pyplot library (as plt), and the random library. Pick a seed for replicability.

import numpy as np
import random
random.seed(0)      #replicate random numbers       

#2 Define T as the number of periods and P as the number of independent variables. Set T =100000 and P = 2.

T = 100000          #number of periods
P = 2               #number of independent variables

#3 Let the true data generating process for be given by:

beta = np.random.uniform(0,2,P)     #choose true coefficients by drawing from a uniform distribution on [0,1]
#beta1 =np.random.uniform(P)        #choose true coefficients by drawing from a uniform distribution on [0,1]

beta 

alpha = np.random.uniform(0,1,1)    #intercept 

#4 Print true values for the intercept and the betas
print("True Intercept ", alpha)
print("True Coefficient ", beta)

#5 Generate a vector of disturbance e of size T
#Stimulate error terms
u = np.random.standard_normal((T,1))

len(u)

#6 Generate a vector for 𝑋1and 𝑋2 of size T
#Stimulate the dependent variable x_t
x1 = np.random.uniform(0,5,(T,1))
x2 = np.random.uniform(0,5,(T,1))


#7 Compute the vector 𝑦 using the equation for the data generating process given above.
#Calculate the resulting y_t
y = np.ones((T,1))*alpha + x1*beta[0] + x2*beta[1] + u


#8 Plot in two contiguous subplots two scatterplots: one for 𝑋1 and 𝑦 and one for 𝑋2 and 𝑦. Label the axis accordingly.
import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.scatter(x1, y)
plt.xlabel("x1")
plt.ylabel("y")
plt.grid()

plt.subplot(1, 2, 2)
plt.scatter(x2, y)
plt.xlabel("x2")
plt.ylabel("y")
plt.grid()

plt.show()

#9 Create a matrix 𝑋 containing your three independent variables
X_mat = np.hstack((np.ones((T,1)),x1,x2))

X_mat


#10 Compute the OLS estimator for 𝛼, 𝛽1, 𝛽2.
beta_hat = np.linalg.inv(X_mat.T.dot(X_mat)).dot(X_mat.T).dot(y)

print(beta_hat)


#11 
import statsmodels.api as sm
results = sm.OLS(y, X_mat).fit()
print(results.summary())