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

# Prediction
def predict(A,x):
    p = 0
    for i in range(len(A)):
        p += (A[i]*(x**i))
    return p


#File input
years = arange(1900,2001,10,dtype = float64)
population = array([10.3,13.5,13.9,14.2,11.6,10.3,9.7,9.6,14.1,19.8,31.1],dtype=float64)

# Initializations
n = int(input("Enter n(must be less than "+str(len(years)-1)+") : "))
y = int(input("Year : "))


co_efficients = co_efficients(years,population,n)

print("Best fit model :\n",end="y = ")

for i in range(n+1):
    if i == 0:
        print("-" if co_efficients[i] < 0 else " ","{:3.6f}".format(abs(co_efficients[i])),end = " ")
    else:
        print("+" if co_efficients[i] >= 0 else "-","{:3.6f}".format(abs(co_efficients[i])),end = "*x^{}".format(i)+" ")
        
print()

print("Prediction : " + "{:3.4f}".format(predict(co_efficients,y)))


close('all')

#Code for plotting

xpoints = arange(1900,2001,2.5)
ypoints = predict(co_efficients,xpoints)

plot(xpoints,ypoints, '-r', label='Immigrants')

scatter(years,population,c="blue")
legend(loc='best')

xlim([1900,2010])
ylim([0,35])

xticks(arange(1900,2011,10))
yticks(arange(0,36,5))

xlabel("Immigration Population (in millions)")
ylabel("Years")

grid()

title("Number of foreign-born immigrants in the United States")

show()
