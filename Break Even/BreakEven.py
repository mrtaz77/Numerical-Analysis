import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    p = 2/3
    return 1000-298*x+3*pow(x,p)

def f_x(x):
    p = -1/3
    return -298+2*pow(x,p)


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

xleft = -8
xright = 8
ydown = -200
yup = 750

xpoints = np.linspace(xleft,xright,30)
ypoints = fx(xpoints)

plt.plot(xpoints, ypoints, '.-b', markersize = 8, label='f(x)', markerfacecolor='w')
plt.plot([xleft-1,xright+1],[0,0], '.-k') #x-axis
plt.plot([0,0],[ydown-1,yup+1], '.-k') #y-axis
plt.plot([3,3],[ydown-1,yup+1], '.-r', label='x = 3') 
plt.plot([4,4],[ydown,yup], '.-g', label='x = 4') 

plt.legend(loc='best')

plt.xlim([xleft-1,xright+1])
plt.ylim([ydown-1,yup+1])

plt.xticks(np.arange(xleft,xright,10))
plt.yticks(np.linspace(ydown,yup,10))

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