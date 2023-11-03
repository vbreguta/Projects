
import numpy as np

#Creating the array containing the values from 1 to 15 
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

#Reshaping the array into a 3 by 5
ar_reshaped = ar.reshape(3,5)

#Print to verify
print(ar_reshaped)

#Make all operations using indexing and slicing techniques
operation_a = ar_reshaped[2,:]
operation_b = ar_reshaped[:,4]
operation_c = ar_reshaped[0:2,:]
operation_d = ar_reshaped[:,2:5]
operation_e = ar_reshaped[1,4]
operation_d = ar_reshaped[1:3, [0,2,4]]


#Print all the values
print("The values in row 2 are: \n", operation_a)
print("The values in column 4 are: \n", operation_b)
print("The values in rows 0 and 1 are: \n", operation_c )
print("The values in columns 2-4 are: \n", operation_d)
print("The element element that is in row 1 and column 4 is: \n", operation_e)
print("The elements from rows 1 and 2 that are in columns 0, 2 and 4 are: \n", operation_d)

