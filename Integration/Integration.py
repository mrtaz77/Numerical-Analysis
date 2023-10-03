from numpy import *
from matplotlib.pyplot import *

# Function
def f(x,C_me):
    return -((6.73*x+6.725*10**-8+7.26*C_me*10**-4)/(x*3.62*10**-12+x*C_me*3.908*10**-8))


# Function for Multiple-application Trapezoid Rule
def multiTrap(C_me,n,x1,x2):
    f_x1 = f(x1,C_me)
    f_x2 = f(x2,C_me)
    h = (x2-x1)/n
    sum = 0
    for j in range(1,n):
        sum += f(x1+j*h,C_me)
    
    integral = ((x2-x1)/(2*n)) * (f_x1+f_x2+2*sum)
    
    return integral


# Function for Simpson's 1/3 rd rule
def simpson(C_me,n,x1,x2):
    f_x1 = f(x1,C_me)
    f_x2 = f(x2,C_me)
    
    h = (x2-x1)/(n)
    odd = 0
    for j in range(1,n,2):
        odd += f(x1+j*h,C_me)

    even = 0
    for j in range(2,n,2):
        even += f(x1+j*h,C_me)        
    
    integral = (h/3) * (f_x1+f_x2+4*odd+2*even)
        
    return integral
        
    
# Console Input
n = int(input("Enter no.of segments: "))

# Initilizations for integration
x0 = 1.22*10**-4
C_me = 5*10**-4
x1 = 0.75*x0
x2 = 0.25*x0

print("Multiple-application Trapezoid Rule")
prevInt = 0
for i in range(n):
    trapInt =  multiTrap(C_me,i+1,x1,x2)
    if i != 0:
        error = abs(trapInt-prevInt)/trapInt * 100
        print("Segments : "+str(i+1)+"\tIntegral : "+str(round(trapInt,4)) +" Error : "+str(round(error,6))+"%")
        
    else :
        print("Segments : "+str(i+1)+"\tIntegral : "+str(round(trapInt,4)))
    prevInt = trapInt


print("Simpson's 1-3rd Rule") 
prevInt = 0
for i in range(2,2*n+1,2):
    simpInt =  simpson(C_me,i,x1,x2)
    if i != 2:
        error = abs(simpInt-prevInt)/simpInt * 100
        print("Segments : "+str(i)+"\tIntegral : "+str(round(simpInt,4)) +" Error : "+str(round(error,6))+"%")
        
    else :
        print("Segments : "+str(i)+"\tIntegral : "+str(round(simpInt,4)))
    prevInt = simpInt

close('all')

#Code for plotting

xpoints = arange(1.4,0,-0.2)
xpoints[0] = 1.22
ypoints = zeros(len(xpoints),dtype=float)
for i in range(1,len(xpoints)):
    ypoints[i] = (simpson(C_me,10,xpoints[0]*10**-4,xpoints[i]*10**-4))/(10**7)

plot(xpoints,ypoints, '.-b', markersize = 8, label='Time', markerfacecolor='w')
legend(loc='best')

xlim([1.22,0])
ylim([0,3])

xticks(arange(1.4,-0.2,-0.2))
yticks(arange(0,3.1,0.5))

xlabel("Oxygen Concentration ($10^-$$^4$ $moles/$$cm^3$)")
ylabel("Time ($10^7$s)")

grid()

title("Oxygen Consumption Over Time")

show()