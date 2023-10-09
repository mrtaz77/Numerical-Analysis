from numpy import *
from matplotlib.pyplot import *

def co_efficients(X,Y):
    n = len(X)
    a1 = (n*sum(X*Y) - (sum(X) * sum(Y)))/(n*sum(power(X,2)) - (sum(X))**2)
    a0 = average(Y)- a1 * average(X)
    return [pow(a0,-1),a1/a0]

def estimate(a,b,x):
    return (a*(x**2))/(b+(x**2))

n = int(input("Enter the number of estimates : "))
predict = zeros(n,dtype=float64)

for i in range(n):
    predict[i] = float(input())

x = array([0.5,0.8,1.5,2.5,4],dtype=float64)
y = array([1.1,2.4,5.3,7.6,8.9],dtype=float64)

invY = pow(y,-1)
inv2X = pow(x,-2)

parameters = co_efficients(inv2X,invY)

print("Model , y = ({:.4f}".format(parameters[0])+"x^2) / ({:.4f}".format(parameters[1])+" + x^2)")

output = estimate(parameters[0],parameters[1],predict)


for i in range(n):
    print("x("+str(predict[i])+") : y = "+str(output[i]))

close('all')

#Code for plotting

xpoints = arange(0,5.1,0.2)
ypoints = estimate(parameters[0],parameters[1], xpoints)
scatter(x,y)
plot(xpoints,ypoints, '-r')

for i in range(n):
    scatter(predict[i],output[i],c ="white",linewidths = 2,edgecolor ="green",s = 50)

xlim([0,5])
ylim([0,10])

xticks(arange(0,6,1))
yticks(arange(0,11,1))

xlabel("x")
ylabel("y")

grid()

title("Model")

show()
