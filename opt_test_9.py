
# optimization tutorial  
########################################################################
# testing basic setup for (1D) dynamical system optimization  
#
# system state x(n) evolves for N time steps toward equilibrium value x_eq
#
# evolution equation:
# x(n+1)=x(n)(1-a)+a*x_eq  
#
# equilibrium value is treated as control parameter
#
# optimal value of control parameter minimizes distance between state x(N) and target state 
#
# notes:
# define the dynamical system
# create a target state (time-independent value)
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

x_0=2.0 #initial state  

x_t=1.0 #target state

N=31 #total number of time steps (n=0,1,2,...,N-1)

a=0.1 #relaxation rate

print("x_0 =",x_0)
print("x_t =",x_t)
print("N =",N)
print("a =",a)



#define state dynamical evolution function 
def get_x_traj(a,x_eq,x0,N):
	x=np.zeros(N,dtype=float)	
	x[0]=x0
	
	#evolve dynamical system in time
	for n in range(N-1):
		x[n+1]=x[n]*(1.0-a)+a*x_eq
		
	return x





#cost function based on distance between final system state and target state 
def cost_function(u,a,N,x_0,x_t):  
	x_traj=get_x_traj(a,u[0],x_0,N)  
		
	y=x_traj[N-1]-x_t  #compare final state of x(n) dynamics to target state

	return np.inner(y, y)
	



#set control parameter bounds
u_min0=0
u_max0=2
bounds = [(u_min0, u_max0)]

#set initial values for control parameters
u_0=1.5 

#initialize vector of control parameters
u=np.zeros(1,dtype=float)
u[0]=u_0 


#find optimal solution
opt_sol = minimize(cost_function, u, args=(a,N,x_0,x_t), method='L-BFGS-B', bounds=bounds)

u0_sol=opt_sol.x[0]  #optimal value for 1st control parameter ("x_eq")

print("u0_sol =", u0_sol)


u_theory=x_t  #theoretical optimal value for control parameter for infinite time evolution 

print(f"u_theory = {u_theory} (in limit where N = infinity)")


#reconstruct dynamics of optimal solution
x_vals=get_x_traj(a,u0_sol,x_0,N) #optimal system trajectory

print("x_opt(N) =", x_vals[N-1]) #final state of optimal dynamical system


n_vals=np.linspace(0,N-1,N) #array of time values


#output data to a text file

output=open('opt_linear_system_A.txt','w')

for n in range (N):
	output.write(str(n_vals[n]))
	output.write('    ')
	output.write(str(x_vals[n]))
	output.write('    ')
	output.write(str(x_t))
	output.write('\n')

output.close()



	
		

print("Fin")
