
# optimization tutorial  
########################################################################
# testing basic setup for optimization 
# (just optimization, no dynamics or control)
#
# state vector of variable size K
#
# constrain subset of elements in state vector to be zero
# (to mimic time-dependent uniform distribution relaxing to equilibrium)
#
# cost function with two inputs (state and target)
#
# notes:
# create a (probability distribution) state vector to be optimized 
# create a target state (uniform distribution)
# define a cost function
# set constraints 
# minimize cost function
# check optimal solution is equal to uniform distribution 
######################################################################## 	


#import
import numpy as np
import math as m

from scipy.optimize import minimize



#set constant parameters

K=13 #number of elements in state array  
print("K =",K)

K_nz=10 #number of nonzero elements in state array
K_z=K-K_nz #number of zero elements in state array

print("K_nz =",K_nz)


#initial distribution
p_vals=np.zeros(K,dtype=float)	
p_vals[0]=1

print("p_vals =",p_vals)

#target distribution
p_eq=np.ones(K,dtype=float)	
p_eq=p_eq/K

print("p_eq =",p_eq)


#cost function based on distance between state and target distribution 
def cost_function(x,x_eq):
	
	y=x-x_eq

	return np.inner(y, y)
	

#check cost function on initial state	
c=cost_function(p_vals,p_eq)

print("c =",c)


#set probability constraints for state vector
def eq_constraint(x):
	return np.sum(x)-1	#normalization

constraints = [
	{'type': 'eq', 'fun': eq_constraint}
	]

bounds = tuple((0,1) for _ in range(K_nz))  #nonzero elements in state 
bounds += tuple((0,0) for _ in range(K_z))  #zero elements in state

#find optimal solution
p_sol = minimize(cost_function, p_vals, args=(p_eq,), method='SLSQP', bounds=bounds, constraints=constraints)

print("p_sol =", p_sol.x)


#check normalization constraint
p_sol_sum = np.sum(p_sol.x)

print("p_sol_sum =", p_sol_sum)


#get cost associated with optimal solution
c_sol=cost_function(p_sol.x,p_eq) 

print("c_sol =", c_sol)


#compare cost of optimal solution to theoretical prediction
c_theory=1.0/K_nz-1.0/K

print("c_theory =", c_sol)


print("c_sol - c_theory =", c_sol-c_theory)







print("Fin")
