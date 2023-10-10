# give point of approximation as input

import numpy as np
import matplotlib.pyplot as plt
from os import path

def nClosest(arr, target, n):
    result = []
    for i in range(len(arr)):
        if len(result) < n:
            result.append(arr[i])
        else:
            max_diff = max([abs(x - target) for x in result])
            if abs(arr[i] - target) < max_diff:
                result.remove(max([(abs(x - target), x) for x in result], key=lambda x: x[0])[1])
                result.append(arr[i])
    return result


def divDiff(x,y,n):
    for i in range(1, n+1):
        for j in range(n+1 - i):
            y[j,i] = (y[j+1,i-1]-y[j,i-1])/(x[j+i]-x[j])
    return y    

def printDiffTable(y,n):
    for i in range(n+1):
        for j in range(n+1 - i):
            print(round(y[i][j], 4), "\t",end = " ")
        print()
        
def interpolate(time,gen_exp,n,value):
    x = np.array(nClosest(time,value,order+1))
    y = np.zeros((order+1,order+1),dtype = float)
    for i in range(len(x)):
        for j in range(len(time)):
            if time[j] == x[i]:
                y[i][0] = gen_exp[j]
                break
    y = divDiff(x,y,n)
    f_x = y[0][0]
    for i in range(1, n+1):
        f_x += (product(i, value, x) * y[0][i])
    return f_x

def product(i, value, x):
    p = 1
    for j in range(i):
        p *= (value - x[j])
    return p



# Get the current directory of the script
current_directory = path.dirname(path.abspath(__file__))

# File input using the correct path
file_path = path.join(current_directory, "gene.txt")
time, gen_exp = np.loadtxt(file_path, delimiter='\t', unpack=True)

order = 3
n = len(time)
value = float(input())
x = np.array(nClosest(time,value,order+1))
y = np.zeros((order+1,order+1),dtype = float)
for i in range(len(x)):
    for j in range(len(time)):
        if time[j] == x[i]:
            y[i][0] = gen_exp[j]
            break        

y = divDiff(x,y,order)
printDiffTable(y,order)       
cubic = interpolate(time,gen_exp,order,value)
quadratic = interpolate(time,gen_exp,order-1,value)

print("Gene expression value at  "+str(value)+" = "+str(round(cubic,4)))
error = abs((cubic-quadratic)/cubic) * 100
print("Error: "+str(round(error,4))+"%")


plt.close('all')

#Code for plotting

xpoints = np.arange(0,time[len(time)-1],0.5)
ypoints = np.zeros(len(xpoints),dtype=float)
for i in range(len(xpoints)):
    ypoints[i] = interpolate(time,gen_exp,order,xpoints[i])

plt.plot(time, gen_exp, '.-k', markersize = 2, label='Cell Cycle', markerfacecolor='w')
plt.scatter(xpoints,ypoints)
plt.plot([value,value],[0,10], '.-r')
plt.plot([0,40],[cubic,cubic], '.-g')

plt.legend(loc='best')

plt.xlim([0,40])
plt.ylim([0,10])

plt.xticks(np.arange(0,41,5))
plt.yticks(np.arange(0,11,1))

plt.xlabel("Time(seconds)")
plt.ylabel("Gene expression")

plt.grid()

plt.title("Gene Expression Profile")

plt.show()