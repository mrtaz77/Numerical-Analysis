import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    return (x**3) - x - 1

def false_pos(l,u,e,itr):
    if fx(l)*fx(u) > 0:
        print("Invalid bounds , enter new bounds")
        l = float(input("Lower Bound = "))
        u = float(input("Upper Bound = "))
        return false_pos(l,u,e,itr)
    
    if fx(l) == 0: return l
    if fx(u) == 0: return u
    
    r_prev = 0
    
    for i in range(1,itr+1,1):
        r = (u*fx(l) - l*fx(u))/(fx(l)-fx(u))
        
        if fx(l)*fx(r) > 0:
            l = r
        elif fx(l)*fx(r) < 0:
            u = r 
    
        else:
            error = 0
            print("Iteration : {0:2d} Error : {1:3.4f}%".format(i, error))     
            return r
        
        if i != 1:
            if r == 0:
                r += 0.00001
            
            error = abs(((r-r_prev)/r)*100)
            print("Iteration : {0:2d} Error : {1:3.4f}%".format(i, error))
            if error <= e:
                return r
        
        else:
            print("Iteration : {0:2d}".format(i))
        
        if i == itr:
            print("Iteration limit reached")
            return r
        r_prev = r
        

plt.close('all')
        
#Code for plotting

xleft = -5
xright = 5
ydown = -10
yup = 10

xpoints = np.linspace(xleft,xright,30)
ypoints = fx(xpoints)

plt.plot(xpoints, ypoints, '.-b', markersize = 8, label='f(x)', markerfacecolor='w')
plt.plot([xleft-1,xright+1],[0,0], '.-k') #x-axis
plt.plot([0,0],[ydown,yup], '.-k') #y-axis
plt.plot([1,1],[ydown,yup], '.-r', label='x = 1') 
plt.plot([2,2],[ydown,yup], '.-g', label='x = 2') 

plt.legend(loc='best')

plt.xlim([xleft-1,xright+1])
plt.ylim([ydown,yup])

# plt.xticks(np.arange(xleft,xright,11))
# plt.yticks(np.linspace(-ydown,yup,11))

plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()

plt.title("$False$ $Position$")
plt.show()
        

        
# Code for False Position

print("False Position")

lower_bound = float(input("Lower Bound = "))
upper_bound = float(input("Upper Bound = "))
approxerr = float(input("Expected relative approximation error = "))
iterations = int(input("Iterations = "))

result = false_pos(lower_bound, upper_bound, approxerr, iterations)
print("Approximate result = {0:3.4f}".format(result))
    


    