
# optimization tutorial  
########################################################################
# testing basic setup for optimization of single control parameter acting on state function 
#
# state vector x of variable size K
# 
# function f of state vector x and control parameter a
# f(x,a)=a*x
#
# find optimal value of control parameter a that minimizes distance between f(x,a) and target function
#
# no dynamics 
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

K=5 #number of elements in state array  


#initial state vector 
p_vals=np.ones(K,dtype=float)	

print("p_vals =",p_vals)


#target function
p_eq=np.ones(K,dtype=float)	
p_eq=p_eq/K

print("p_eq =",p_eq)


#cost function based on distance between function f(x,u) of state vector and target function f_eq 
#inputs u = control parameter, x = state vector, f_eq 
def cost_function(u,x,f_eq):  
	f_x=u*x  #define f(x,u) function that scales state vector by control parameter 
		
	y=f_x-f_eq

	return np.inner(y, y)
	


#check cost function on initial state	
u_val=0.5
c=cost_function(u_val,p_vals,p_eq)
print("c =",c)




u_0=1.0 #initial value for control parameter

#find optimal solution
opt_sol = minimize(cost_function, u_0, args=(p_vals,p_eq), method='Nelder-Mead')

u_sol=opt_sol.x[0]  #optimal value for control parameter 

print("u_sol =", u_sol)


u_theory=1.0/K  #theoretical optimal value for control parameter

print("u_theory =", u_theory)



	
	
		

print("Fin")
