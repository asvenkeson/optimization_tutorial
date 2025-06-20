
# optimization tutorial  
########################################################################
# testing basic setup for optimization with single control parameter acting on state function 
#
# state vector x of variable size K
#
# f(x,a)=a*x
#
# find optimal value of parameter a that minimizes distance between f(x,a) and target function
#
# no dynamics 
#
# include bounds for control parameter (a_min < a < a_max)
#
# cost function with three inputs (control parameter, state, target)
#
# notes:
# create a state vector to be optimized (non-normalized distribution)
# create a target state (uniform distribution)
# define a cost function
# set constraints 
# minimize cost function
# check optimal solution 
######################################################################## 	

#import
import numpy as np
import math as m

from scipy.optimize import minimize



#set constant parameters

K=3 #number of elements in state array  


#initial state vector 
p_vals=np.ones(K,dtype=float)	

print("p_vals =",p_vals)


#target function
p_eq=np.ones(K,dtype=float)	
p_eq=p_eq/K

print("p_eq =",p_eq)


#cost function based on distance between state and target distribution 
def cost_function(u,x,f_eq):  
	f_x=u*x  
		
	y=f_x-f_eq

	return np.inner(y, y)
	


#check cost function on initial state	
u_val=0.5
c=cost_function(u_val,p_vals,p_eq)
print("c =",c)


#set control parameter bounds
u_min=0
u_max=5
bounds = [(u_min, u_max)]

u_0=1.0 #initial value for control parameter

#find optimal solution
opt_sol = minimize(cost_function, u_0, args=(p_vals,p_eq), method='L-BFGS-B', bounds=bounds)

u_sol=opt_sol.x[0]  #optimal value for control parameter 

print("u_sol =", u_sol)


u_theory=1.0/K  #theoretical optimal value for control parameter

print("u_theory =", u_theory)
















			


	
	
		

print("Fin")
