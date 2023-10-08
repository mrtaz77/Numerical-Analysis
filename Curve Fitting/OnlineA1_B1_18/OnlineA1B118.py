# data.txt must be in the same directory

from numpy import *
from matplotlib.pyplot import *

def co_efficients(X,Y):
    n = len(X)
    a1 = (n*sum(X*Y) - (sum(X) * sum(Y)))/(n*sum(X**2) - (sum(X))**2)
    a0 = average(Y)- a1 * average(X)
    return [a0,a1]  

def predict(a,b,x):
    return a*x+b*exp(x)

x,y = loadtxt("data.txt",delimiter=' ',unpack = 'true')

ye_x = y * exp(-x)
xe_x = x * exp(-x)

b,a = co_efficients(xe_x,ye_x)

print("Best fit model :\n",end="y = ")
print("" if a >= 0 else "-","{:3.6f}".format(abs(a)),end = "x ")
print("+" if b >= 0 else "-","{:3.6f}".format(abs(b)),end = "e^x")

xpoints  = arange(0,5.1,0.1)
ypoints = predict(a,b,xpoints)

close('all')

#Code for plotting
scatter(x,y,c = "blue")
plot(xpoints,ypoints, '-r')

xlim([0,7])
ylim([-11,11])

xticks(arange(0,8,1))
yticks(arange(-11,11,1))

xlabel("x")
ylabel("y")

grid()

title("Model")

show()
