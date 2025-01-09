"""
A call center receives an average of 4 calls per minute. What is the probability of receiving exactly 6 calls in a given minute? Hint: Use the formula 
P(X=k)= (λ**k * e**(-λ)) /k! , where λ=4
"""
import math

# a funciton for calculating factorial of a number 
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)

# a function to find the possion distribution
def possion_distribution(lam_symbol, k):
    return (lam_symbol**k * (math.exp(-lam_symbol))) / factorial(k)

# initializing the value of λ, and k
average_call = 4    # λ
exact_call = 6  # k

# calling the possion_distribution() function
result = possion_distribution(average_call, exact_call)

# printing out the result
print(f"The probability of receiving exactly {exact_call} calls in a given minute is approximately {result}")