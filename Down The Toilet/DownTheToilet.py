import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    return x**3-3*6*x**2+4*0.55*(6)**3

def f_x(x):
    return 3*x**2-36*x

def bisection(l,u,e,itr):
    
    if fx(l)*fx(u) > 0:
        print("Invalid bounds , enter new bounds")
        l = float(input("Lower Bound = "))
        u = float(input("Upper Bound = "))
        return bisection(l,u,e,itr)
    
    if fx(l) == 0: return l
    if fx(u) == 0: return u
    
    m_old = 0
    
    for i in range(1,itr+1,1):
        
        m = (l+u)/2
        
        if fx(l)*fx(m)<0:
            u = m
        elif fx(l)*fx(m)>0:
            l = m
        else:
            error = 0
            print("Iteration : {0:2d} Error : {1:3.4f}%".format(i, error))     
            return m
        
        if i != 1:
            error = abs(((m-m_old)/m)*100)
            print("Iteration : {0:2d} Error : {1:3.4f}%".format(i, error))
            if error <= e:
                return m
        
        else:
            print("Iteration : {0:2d}".format(i))
        
        if i == itr:
            print("Iteration limit reached")
            return m
        m_old = m

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

xpoints = np.linspace(-2,14,27)
ypoints = fx(xpoints)

plt.plot(xpoints, ypoints, '.-b', markersize = 8, label='f(x)', markerfacecolor='w')
plt.plot([-2,14],[0,0], '.-k') #x-axis
plt.plot([0,0],[-500,500], '.-k') #y-axis
plt.plot([6,6],[-500,500], '.-r', label='x = 6') 
plt.plot([7,7],[-500,500], '.-g', label='x = 7') 

plt.legend(loc='best')

plt.xlim([-2,14])
plt.ylim([-500,500])

plt.xticks(np.arange(-2,15,1))
plt.yticks(np.linspace(-500,500,11))

plt.xlabel("x,Depth of submergence(cm)")
plt.ylabel("f(x)")

plt.grid()

plt.title(" $Determination$ $of$ $Depth$ $of$ $Submergence$ ")

plt.show()

#Code for Bisection

print("Bisection Method")

lower_bound = float(input("Lower Bound = "))
upper_bound = float(input("Upper Bound = "))
approxerr = float(input("Expected relative approximation error = "))
iterations = int(input("Iterations = "))

result = bisection(lower_bound, upper_bound, approxerr, iterations)
print("Approximate result = {0:3.4f}".format(result))

#Code for newton-raphson

print("Newton-Raphson Method")

init = float(input("Initial Guess = "))
approxerr = float(input("Expected relative approximation error = "))
iterations = int(input("Iterations = "))

result = nwt_raph(init, approxerr, iterations)
print("Approximate result = {0:3.4f}".format(result))

