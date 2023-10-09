from numpy import *
from matplotlib.pyplot import *

def sum_of_power(arr, exponent):
    return sum(power(arr, exponent))

def sum_of_elementwise_powers(arr1, arr2, exponent):
    return sum(power(arr1, exponent) * arr2)

#Intermediate output
def printMat(A,B):
    for i in range(0, len(A)):
        for j in range(0,len(A[i])):
            if j == len(A[i])-1:
                print("{:3.4f}".format(A[i][j]),end = '\t')
                print("{:3.4f}".format(B[i]))
            else :
                print("{:3.4f}".format(A[i][j]),end = ' ')
        
#Solution output
def printSoln(x):
    for i in range(0, len(x)):
        print(str(x[i]))
        
#determinant of upper triangular co-efficient matrix
def det(x,flag):
    det = x[0][0]
    for i in range(1, len(x)):
        det *= x[i][i]
    return det*(-1)**flag 

#Gaussian elimination
def GaussianElimination(A,B,pivot = True,showAll = True):
    n = len(A)
    flag = 0
    for i in range(0,n-1):
        #Partial Pivoting
        if pivot :
            max_index = i
            for j in range(i+1,n):
                if abs(A[j][i]) > abs(A[max_index][i]):
                    max_index = j
            if i != max:
                flag += 1
                A[[i,max_index]] = A[[max_index,i]]
                B[[i,max_index]] = B[[max_index,i]]
        elif A[i][i] == 0:
            print("Gaussian elimination failed . Division by zero")
            exit(1)
        
        #Forward elimination
        for j in range(i+1,n):
            B[j] = B[j] - (A[j][i]/A[i][i]) * B[i]
            A[j] = A[j] - (A[j][i]/A[i][i]) * A[i]
            if showAll :
                printMat(A,B)
                print()
    #Back substitution
    soln = empty(n,dtype = float)
    for i in range(n-1,-1,-1):
        soln[i] = B[i]
        for j in range(n-1,i,-1):
            soln[i] -= A[i,j]*soln[j]
        soln[i] /= A[i][i]
    
        
    if showAll :
        return [soln,det(A,flag)]
    else:
        return [soln]

# Co-efficients for curve fitting
def co_efficients(X,Y,n):
    A = empty((n+1,n+1),dtype = float)
    B = empty(n+1,dtype = float)
    
    A[0][0] = len(X)
    
    for i in range(1,n+1):
        A[0][i] = sum_of_power(X,i)
    
    for i in range(1,n+1):
        A[i][n] = sum_of_power(X,n+i)
    
    for i in range(1,n+1):
        for j in range(0,n):
            A[i][j] = A[i-1][j+1]
        
    for i in range(n+1):
        B[i] = sum_of_elementwise_powers(X,Y,i)
        
    # printMat(A,B)
    # print()
    ans = GaussianElimination(A,B,True,False)
    
    # printSoln(ans[0])
    
    return ans[0]  

def estimate(a,b,c,x):
    return a + b*x + (c/x)

n = int(input("Enter the number of estimates : "))
predict = zeros(n,dtype=float64)
for i in range(n):
    predict[i] = float(input())
    
x = arange(1,6,1,dtype = float64)
y = array([2.2,2.8,3.6,4.5,5.5],dtype = float64)

XY = x*y

co_efficients = co_efficients(x,XY,2)

# Parameters
c = co_efficients[0]
a = co_efficients[1]
b = co_efficients[2]

print("Best fit model :\n",end="y = ")
print("" if a >= 0 else "-","{:3.6f}".format(abs(a)),end = " ")
print("+" if b >= 0 else "-","{:3.6f}".format(abs(b)),end = "x ")
print("+" if c >= 0 else "-","{:3.6f}".format(abs(c)),end = "/x\n")

output = estimate(a,b,c,predict)

for i in range(n):
    print("x("+str(predict[i])+") : y = "+str(output[i]))


close('all')

#Code for plotting
xpoints = arange(0.1,7.1,0.1)
ypoints = estimate(a,b,c,xpoints)
plot(xpoints,ypoints, '-r')
scatter(x,y,c = "blue")

for i in range(n):
    scatter(predict[i],output[i],c ="white",linewidths = 2,edgecolor ="green",s = 50)


xlim([0,7])
ylim([0,10])

xticks(arange(0,8,1))
yticks(arange(0,11,1))

xlabel("x")
ylabel("y")

grid()

title("Model")

show()
