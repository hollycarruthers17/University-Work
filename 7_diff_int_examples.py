
## Numerical Differentiation and Numerical Integration Examples

### Numerical Differentiation

import numpy as np 
import matplotlib.pyplot as plt 

#step size 
h = 0.1 

#define grid 
x = np.arange(0, 2*np.pi, h) 

#compute function 
y = np.cos(x)

#compute vector of forward differences 
forward_diff = np.diff(y)/h 

#compute corresponding grid 
x_diff = x[:-1:] 

#compute exact solution 
exact_solution = -np.sin(x_diff)

#Plot solution 
plt.figure(figsize = (12, 8)) 
plt.plot(x_diff, forward_diff, "-",  label = "Finite difference approximation")
plt.plot(x_diff, exact_solution, label = "Exact solution") 
plt.legend() 
plt.show()

#Compute max error between numerical derivative and exact solution 
max_error = max(abs(exact_solution - forward_diff)) 
print(max_error)

### Numerical Integration

#Use the left and right Riemann integral, as well as midpoint rule, to approximate  int^{0}_{π} sin(x)dx with 11 evenly spaced grid points over the whole interval
##Compare this value to the exact value of 2.

import numpy as np 
a = 0 
b = np.pi 
n = 11 
h = (b - a) / (n - 1) 
x = np.linspace(a, b, n) 
f = np.sin(x) 

I_riemannL = h * sum(f[:n-1]) 
err_riemannL =2-I_riemannL 

I_riemannR = h * sum(f[1::]) 
err_riemannR =2- I_riemannR 

I_mid = h * sum(np.sin((x[:n-1] + x[1:])/2)) 
err_mid =2- I_mid 

print(I_riemannL) 
print(err_riemannL) 
print(I_riemannR) 
print(err_riemannR) 
print(I_mid) 
print(err_mid) 

#Use the trapezoid rule to approximate  int^{0}_{π} sin(x)dx with 11 evenly spaced grid points over the whole interval
#Compare this value to the exact value of 2.
import numpy as np 
a = 0 
b = np.pi 
n = 11 
h = (b - a) / (n - 1) 
x = np.linspace(a, b, n) 
f = np.sin(x) 

I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1]) 
err_trap = 2 - I_trap 

print(I_trap) 
print(err_trap) 

#Use the trapez function to approximate  int^{0}_{π} sin(x)dx with 11 evenly spaced grid points over the whole interval
#Compare this value to the one computed in the earlier example using the trapezoid rule.
#Compare this value to the exact value of 2.

import numpy as np 
from scipy.integrate import trapz 

a = 0 
b = np.pi 
n = 11 
h = (b - a) / (n - 1) 
x = np.linspace(a, b, n) 
f = np.sin(x) 
I_trapz = trapz(f,x) 

I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1]) 

print(I_trapz) 
print(I_trap) 

#Use the cumtrapz function to approximate the cumulative integral  of f(x)=sin(x) from 0 to \pi,with a discretization step of 0.01. 
#The exact solution of this integral is F(x) = sin(x).
#Plot the results.

from scipy.integrate import cumtrapz 
import matplotlib.pyplot as plt
#matplotlib inline 
plt.style.use("seaborn-poster") 

x = np.arange(0, np.pi, 0.01) 
F_exact = -np.cos(x) 
F_approx = cumtrapz(np.sin(x), x) 

plt.figure(figsize = (8,4)) 
plt.plot(x, F_exact) 
plt.plot(x[1::], F_approx) 
plt.grid() 
plt.tight_layout() 
plt.title("$F(x) = \int_0^{x} sin(y) dy$") 
plt.xlabel("x") 
plt.ylabel("f(x)") 
plt.legend(["Exact with Offset", "Approx"]) 
plt.show()

#Use the integrate.quad function to compute  π 0 sin(x)dx. Compare your answer with the correct answer of 2.
from scipy.integrate import quad 
I_quad, est_err_quad = quad(np.sin, 0, np.pi) 
print(I_quad)

err_quad = 2 - I_quad 
print(est_err_quad, err_quad)