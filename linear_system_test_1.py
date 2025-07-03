
# linear dynamical system tutorial 
########################################################################
# 1D linear dynamical system time evolution 
#
# system state x 
#
# state evolution equations: 
# dx/dt = -a(x-x_eq) in continuous time
# x(n+1)=x(n)(1-a)+a*x_eq  (dt=1)
# 
# notes:
# evolve the system state x(n) in time starting from initial state x(0)
# save the resulting x(n) trajectory data to a text file
######################################################################## 	

#import
import numpy as np
import math as m



#set constant parameters

N=101 #total number of time steps (n=0,1,2,...,N-1)

a=0.1 #relaxation rate

x_eq=1 #equilibrium state

x_0=2 #initial state

print("N =",N)
print("a =",a)
print("x_eq =",x_eq)
print("x_0 =",x_0)


#define state dynamical evolution function 
def get_x_traj(a,x_eq,x0,N):
	x=np.zeros(N,dtype=float)	
	x[0]=x0
	
	#evolve dynamical system in time
	for n in range(N-1):
		x[n+1]=x[n]*(1.0-a)+a*x_eq
		
	return x


x_vals=get_x_traj(a,x_eq,x_0,N)

n_vals=np.linspace(0,N-1,N)

#print("n_vals =",n_vals)
#print("x_vals =",x_vals)



#output data to a text file

output=open('linear_system_A.txt','w')

for n in range (N):
	output.write(str(n_vals[n]))
	output.write('    ')
	output.write(str(x_vals[n]))
	output.write('\n')

output.close()
	
		

print("Fin")
