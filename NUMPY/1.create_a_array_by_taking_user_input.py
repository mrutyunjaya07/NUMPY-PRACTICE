# import numpy liabrary
import numpy as np

# initialize a empty list
l=[]

# taking input
for i in range(5):
    int_1=int(input("Enter a integer :"))
    l.append(int_1)

# creating numpy array by passing the list
print(np.array(l))