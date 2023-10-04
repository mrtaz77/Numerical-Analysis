import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    return 70*np.exp(-1.5*x) +25*np.exp(-0.075*x) -47.5

def f_x(x): 
    return -105*np.exp(-1.5*x) - 1.875*np.exp(-0.075*x)

def nwt_raph(x0,e,itr):
    
    i = 1
    
    while i <= itr:
        if f_x(x0) == 0 :
            print("Invalid initial value")
            x0 = float(input("Enter new initial guess : "))
            i = 1
            continue
        
        xi = x0 - fx(x0)/f_x(x0)
        
        error = abs(((xi-x0)/xi)*100)
        print("Iteration : {0:2d} Error : {1:3.4f}%".format(i, error))
        
        if error <= e:
            return xi
        if i == itr:
            print("Iteration limit reached")
            return xi
        
        if  xi > 20 :
            print("Value out of range")
            x0 = float(input("Enter new initial guess : "))
            i = 1
            continue
        
        x0 = xi
        i+=1
        
plt.close('all')
        
#Code for plotting

xleft = -1
xright = 20
ydown = -40
yup = 20

xpoints = np.linspace(xleft,xright,60)
ypoints = fx(xpoints)

plt.plot(xpoints, ypoints, '.-b', markersize = 8, label='f(x)', markerfacecolor='w')
plt.plot([xleft-1,xright+1],[0,0], '.-k') #x-axis
plt.plot([0,0],[ydown,yup], '.-k') #y-axis
plt.plot([1,1],[ydown,yup], '.-r', label='x = 1') 

plt.legend(loc='best')

plt.xlim([xleft-1,xright+1])
plt.ylim([ydown,yup])


plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()

plt.title("$Online$ $A1$")
plt.show()
        

        
#Code for newton-raphson

init = float(input("Initial Guess = "))
approxerr = float(input("Expected relative approximation error = "))
iterations = int(input("Iterations = "))

result = nwt_raph(init, approxerr, iterations)
print("Approximate result = {0:3.4f}".format(result))