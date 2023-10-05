import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    return np.pi*(x**3)-12*np.pi*x*x + 15

def f_x(x):
    return np.pi*3*x*x -24*np.pi*x

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
        if xi < 0 or xi > 12 :
            print("Value out of range")
            x0 = float(input("Enter new initial guess : "))
            i = 1
            continue
        x0 = xi
        i+=1
        
        
plt.close('all')
        
#Code for plotting

xleft = -4
xright = 4
ydown = -1000
yup = 1000

xpoints = np.linspace(xleft,xright,30)
ypoints = fx(xpoints)

plt.plot(xpoints, ypoints, '.-b', markersize = 8, label='f(x)', markerfacecolor='w')
plt.plot([xleft-10,xright+10],[0,0], '.-k') #x-axis
plt.plot([0,0],[ydown,yup], '.-k') #y-axis
plt.plot([1,1],[ydown,yup], '.-r', label='x = 1') 
plt.plot([2,2],[ydown,yup], '.-g', label='x = 2') 

plt.legend(loc='best')

plt.xlim([xleft-10,xright+10])
plt.ylim([ydown,yup])

# plt.xticks(np.arange(xleft,xright,11))
# plt.yticks(np.linspace(-ydown,yup,11))

plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()

plt.title("$False$ $Position$")
plt.show()
        
#Code for newton-raphson

print("Newton-Raphson Method")

init = float(input("Initial Guess = "))
approxerr = float(input("Expected relative approximation error = "))
iterations = int(input("Iterations = "))

result = nwt_raph(init, approxerr, iterations)
print("Approximate result = {0:3.4f}".format(result))