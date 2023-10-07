from numpy import *
from matplotlib.pyplot import *

n = 2

def co_efficients(X,Y):
    n = len(X)
    a1 = (n*sum(X*Y) - (sum(X) * sum(Y)))/(n*sum(X**2) - (sum(X))**2)
    a0 = average(Y)- a1 * average(X)
    return [a0,a1] 

def predict(a,b,x):
    return a*(x**b)

x = array([4, 5, 7, 8, 9,10],dtype=float64)
y = array([5800, 5700, 4200, 4100, 3100,2500],dtype=float64)

co_efficient = co_efficients(x,y)

co_efficient = co_efficients(log(x),log(y))

a = exp(co_efficient[0])
b = (co_efficient[1])

print("Best fit model :\n",end="y = ")
print("" if a >= 0 else "-","{:3.6f}".format(abs(a)),end = "x^")
print("+" if b >= 0 else "-","{:3.6f}".format(abs(b)),end = "\n")

xpoints  = arange(0.1,10.1,0.1)
ypoints = predict(a,b,xpoints)

close('all')

#Code for plotting
scatter(x,y,c = "blue")
plot(xpoints,ypoints, '-r')

xlim([0,11])
ylim([0,6000])

xticks(arange(0,11,1))
yticks(arange(0,6000,500))

xlabel("x")
ylabel("y")

grid()

title("Model")

show()




