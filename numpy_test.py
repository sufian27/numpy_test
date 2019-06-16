#Task 1
import numpy as np 

#Task 2
print("VERSION")
print(np.__version__)

print("CONFIGURATION")
print(np.show_config())

#Task 3
null_vector = np.zeros(10)
print(null_vector)

#Task 4
print("Size of array: " + str(null_vector.size))
print("ItemSize of array: " + str(null_vector.itemsize))

#Task 5
print(np.info(np.add))

#Task 6
a = np.zeros(10)
a[4] = 1
print(a)

#Task 7
b = np.arange(10, 50)
print(b)

#Task 8
c = b[::-1]
print(c)

#Task 9
d = np.arange(9).reshape(3, 3)
print(d)

#Task 10
e = ([1, 2, 0, 0, 4, 0])
nonzero_tuple = np.nonzero(e)
print("Indices of non-zero elements: ", nonzero_tuple)