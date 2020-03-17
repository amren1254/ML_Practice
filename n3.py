#3. Write a NumPy program to test whether none of the elements of a given array is zero. Go to the editor 

import numpy as np
x = np.array([1,2,3,4])
y = np.array([0,1,2,3,4])

print(x)
print(np.all(x))
print(y)
print(np.all(y))
