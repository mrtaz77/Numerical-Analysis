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

t = arange(0,31,5,dtype=float64)
w = array([1000,550,316,180,85,56,31],dtype=float64)

h = float64(input("Enter number of hours: "))

ln_w = log(w)

co_efficients = exp_co_efficients(t,ln_w)

print("Best fit model :\n",end="y = ")
print("{:3.4f}".format(co_efficients[0])+"e^({:3.4f}".format(co_efficients[1])+"x)")

print("Estimate : "+str(estimate(co_efficients[0],co_efficients[1],h)))


close('all')

#Code for plotting

xpoints = arange(0,31,1)
ypoints = estimate(co_efficients[0],co_efficients[1],xpoints)

plot(xpoints,ypoints, '.-r', markersize = 8, label='Drug level', markerfacecolor='w')

scatter(t,w)
legend(loc='best')

xlim([0,31])
ylim([0,1110])

xticks(arange(0,31,5))
yticks(arange(0,1110,100))

xlabel("Hours Since Drug was Administered")
ylabel("Amount of Drug in Body(mg)")

grid()

title("Dosage")

show()
