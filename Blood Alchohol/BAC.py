from numpy import *
from matplotlib.pyplot import *

def sum_of_power(arr, exponent):
    return sum(power(arr, exponent))

def sum_of_elementwise_powers(arr1, arr2, exponent):
    return sum(power(arr1, exponent) * arr2)

def exp_co_efficients(X,Y):
    n = len(X)
    a1 = (n*sum(X*Y) - (sum(X) * sum(Y)))/(n*sum_of_power(X,2) - (sum(X))**2)
    a0 = average(Y)- a1 * average(X)
    return [exp(a0),a1]    

def estimate(a,b,x):
    return a*exp(b*x)

x = float(input("Enter Blood Alchohol Level: "))

bac = arange(-0.01,0.22,0.02,dtype = float64)
bac[0] = 0
crash = array([1,1.03,1.06,1.38,2.09,3.54,6.41,12.6,22.1,39.05,65.32,99.78],dtype=float64)
ln_crash = log(crash)

co_efficients = exp_co_efficients(bac,ln_crash)

print("Best fit model :\n",end="y = ")
print("{:3.4f}".format(co_efficients[0])+"e^({:3.4f}".format(co_efficients[1])+"x)")

print("Estimate : "+str(estimate(co_efficients[0],co_efficients[1],x)))


close('all')

#Code for plotting

xpoints = arange(0,0.22,0.01)
ypoints = estimate(co_efficients[0],co_efficients[1],xpoints)

plot(xpoints,ypoints, '.-r', markersize = 8, label='Crash Risk', markerfacecolor='w')

scatter(bac,crash)
legend(loc='best')

xlim([0,0.21])
ylim([0,110])

xticks(arange(0,0.25,0.03))
yticks(arange(0,111,10))

xlabel("Blood Alchohol Level")
ylabel("Relative Risk of Crashing")

grid()

title("Alchohol impaired driving")

show()

