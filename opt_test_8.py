
# optimization tutorial  
########################################################################
# testing basic setup for optimization with two control parameters acting on state function 
#
# state vector x of variable size K
#
# f(x,a,b)=a*(x_1,x_2,...,x_k,0,...)+b*(0,...,0,x_{k+1},...,x_K)
#
# find optimal value of parameters a and b that minimizes distance between f(x,a,b) and target function
#
# no dynamics 
#
# cost function with three inputs (control parameters, state, target)
#
# notes:
# create a state vector to be optimized (non-normalized distribution)
# create a target state (uniform distribution)
# create a control parameter vector
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

K=10 #number of elements in state array  

k_step=7 #location of step in function f[k_step-1] != f[k_step]

#initial state vector 
p_vals=np.ones(K,dtype=float)	

print("p_vals =",p_vals)


#target function  (step function)
p1=1.5 #first value in step function
p2=0.2 #second value in step function
p_eq=np.ones(K,dtype=float)	
p_eq[0:k_step]=p1
p_eq[k_step:K]=p2

print("p_eq =",p_eq)



#define step function 
def step_function(u,x,K,k_step):
	f_x=np.zeros(K,dtype=float)
	x_1=np.zeros(K,dtype=float)
	x_1[0:k_step]=x[0:k_step]
	x_2=np.zeros(K,dtype=float)
	x_2[k_step:K]=x[k_step:K]
	
	f_x=u[0]*x_1+u[1]*x_2
		
	return f_x


#test step function 

u_step=np.zeros(2,dtype=float)
u_step[0]=0.1
u_step[1]=1.5

f_step=step_function(u_step,2*p_vals,K,k_step)

print("f_step =",f_step)





#cost function based on distance between state and target distribution 
def cost_function(u,x,f_eq):  
	f_x=step_function(u,x,K,k_step)  
		
	y=f_x-f_eq

	return np.inner(y, y)
	


#check cost function on initial state	
u_vals=np.zeros(2,dtype=float)
u_vals[0]=0.2
u_vals[1]=0.9
c=cost_function(u_vals,p_vals,p_eq)
print("c =",c)




#set control parameter bounds
u_min0=0
u_max0=3
u_min1=0
u_max1=1
bounds = [(u_min0, u_max0),(u_min1, u_max1)]

#set initial values for control parameters
u_0=1.0 
u_1=1.0

#initialize vector of control parameters
u=np.zeros(2,dtype=float)
u[0]=u_0 
u[1]=u_1


#find optimal solution
opt_sol = minimize(cost_function, u, args=(p_vals,p_eq), method='L-BFGS-B', bounds=bounds)

u0_sol=opt_sol.x[0]  #optimal value for 1st control parameter ("a")
u1_sol=opt_sol.x[1]  #optimal value for 2nd control parameter ("b")

print("u0_sol =", u0_sol)
print("u1_sol =", u1_sol)


u_theory=[p1, p2]  #theoretical optimal values for control parameters

print("u_theory =", u_theory)






	
		

print("Fin")
