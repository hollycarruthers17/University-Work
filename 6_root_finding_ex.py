import numpy as np 
from scipy import optimize 

f = lambda x: np.cos(x) - x 
r = optimize.fsolve(f, -2) 
print("r =", r)

f = lambda x: 1/x 

r, infodict, ier, mesg = optimize.fsolve(f, -2, full_output=True) 
print("r =", r) 
result = f(r) 

print("result=", result) 
print(mesg) 


#Bisection Method
import numpy as np 
import matplotlib.pyplot as plt

# approximates a root, R, of f bounded by a and b to within tolerance | f(m) | < tol with m being the midpoint between a and b. 
#Recursive implementation 
def my_bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")
    # get midpoint
    m = (a + b)/2
    if np.abs(f(m)) < tol:    #stopping condition, report m as root
        return m
    elif np.sign(f(a)) == np.sign(f(m)):  #case where m is an improvement on a. Make recursive call with a = m
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):  #case where m is an improvement on b. Make recursive call with b = m
        return my_bisection(f, a, m, tol)

f = lambda x: x**2 - 2
x1 = np.linspace(0,3,50)

plt.plot(x1,f(x1))
plt.xlabel("x")
plt.ylabel("x^2 - 2")
plt.show()

r1 = my_bisection(f, 0, 1, 0.1)
print("r1 =", r1)

r2 = my_bisection(f, 0, 3, 0.1)
print("r2 =", r2)

r3 = my_bisection(f, 0, 3, 0.01)
print("r3 =", r3)
print("f(r3) =", f(r3))
print("f(r2) =", f(r2))



#Newton Raphson Method
import numpy as np
f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
newton_raphson = 1.4 - (f(1.4))/(f_prime(1.4))

print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))



#Root Finding in Python
from scipy.optimize import fsolve 
f = lambda x: x**3-100*x**2-x+100 
fsolve(f, [2, 80])