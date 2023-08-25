import numpy as np
'''n=[]
a=int(input("Enter size of list: "))
for x in range(0,a):   
   c=int(input("Enter:"))
   n.append(c)

print("Before Sorting: ",n)  
n.sort()
print("After Sorting: ",n)
z=np.array(n)
q1= 1/4*a+1
b1=int(q1-1)
q2= 1/2*a+1
b2=int(q2-1)
q3= 3/4*a+1
b3=int(q3-1)
l1=n[b1]
l2=n[b2]
l3=n[b3]
print("Q1=",l1,"Q2=",l2,"Q3=",l3)'''

def calculate_iqr(data):
    data.sort()
    n = len(data)
    
    if n % 2 == 0:
        q1 = (data[n//4 - 1] + data[n//4]) / 2
        q3 = (data[3*n//4 - 1] + data[3*n//4]) / 2
    else:
        q1 = data[n//4]
        q3 = data[3*n//4]
    
    iqr = q3 - q1
    return iqr

# Get user input for the dataset
data = []
n = int(input("Enter the number of data points: "))
for i in range(n):
    value = float(input(f"Enter data point {i+1}: "))
    data.append(value)

# Calculate and print the IQR
iqr = calculate_iqr(data)
print(f"The Interquartile Range (IQR) is: {iqr}")
