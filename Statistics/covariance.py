# Q) Calculate the variance for a set of random numbers.

import numpy as np

# getting random data 
data = np.random.randint(1, 100, size=10)

# printing the random data
print(f"Ramdom data = {data}")

# calculating the variance
result = np.var(data)

# printing out the result
print(f"Variance = {result}")