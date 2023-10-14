from numpy import *
from matplotlib.pyplot import *

def sum_of_power(arr, exponent):
    return sum(power(arr, exponent))

def exp_co_efficients(X,Y):
    n = len(X)
    a1 = (n*sum(X*Y) - (sum(X) * sum(Y)))/(n*sum_of_power(X,2) - (sum(X))**2)
    a0 = average(Y)- a1 * average(X)
    return [exp(a0),a1]    

def estimate(a,b,x):
    return a*x*exp(b*x)

x = array([ 0.1 ,0.2 ,0.4 ,0.6 ,0.9 ,1.3 ,1.5 ,1.7 ,1.8],dtype=float64)
y = array([0.75, 1.25, 1.45, 1.25, 0.85, 0.55, 0.35, 0.28, 0.18],dtype=float64)

y_x = log(y/x)

parameters = exp_co_efficients(x,y_x)

a = parameters[0]
b = parameters[1]

# Add points in this line for prediction
predict = array([1.6,2.0,2.5,1],dtype=float64)

print("Model , y = {:.4f}".format(parameters[0])+"xe^({:.4f}".format(parameters[1])+"x)")

output = estimate(parameters[0],parameters[1],predict)

for i in range(len(predict)):
    print("x("+str(predict[i])+") : y = "+str(output[i]))

close('all')

#Code for plotting

xpoints = arange(0,2.5,0.05)
ypoints = estimate(parameters[0],parameters[1], xpoints)
scatter(x,y,c="blue")
plot(xpoints,ypoints, '-r')

for i in range(len(predict)):
    scatter(predict[i],output[i],c ="white",linewidths = 2,edgecolor ="green",s = 50)

xlim([0,2.4])
ylim([0,2.4])

xticks(arange(0,2.5,0.2))
yticks(arange(0,2.5,0.2))

xlabel("x")
ylabel("y")

grid()

title("Model")

show()

