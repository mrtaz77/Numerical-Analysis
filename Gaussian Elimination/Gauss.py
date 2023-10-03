import numpy as np

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
        print("{:.4f}".format(x[i]))
        
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
    soln = np.empty(n,dtype = float)
    for i in range(n-1,-1,-1):
        soln[i] = B[i]
        for j in range(n-1,i,-1):
            soln[i] -= A[i,j]*soln[j]
        soln[i] /= A[i][i]
    
        
    if showAll :
        return [soln,det(A,flag)]
    else:
        return [soln]
        

#input
n = int(input())
A = np.empty((n,n),dtype = float)
B = np.empty(n,dtype = float)

for i in range(0,n):
    temp = input().split(" ")
    for j in range(0,n):
        A[i,j] = float(temp[j])

for i in range(0,n):
    B[i] = float(input())
    


#np.linalg.det() returns determinant of the matrix
if np.linalg.det(A) == 0 :
    print("Infinite or no solutions exist")
    
else :
    print()
    pivot = True
    showAll = True
    ans = GaussianElimination(A, B,pivot,showAll)
    
    if len(ans) == 2 :
        printSoln(ans[0])
        print("Determinant : {0:3.4f}".format(ans[1]))
    else :
        printSoln(ans[0])

    