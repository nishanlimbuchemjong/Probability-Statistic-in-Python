"""
A fair coin is tossed 10 times. What is the probability of getting exactly 6 heads? Hint: Use the formula P(X=k)=( k n)p^k(1-p)^(n-k), where p=0.5

"""
# a funciton that gives the factorial of any number
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# a function that returns the value using the binomial distribution 
def binomial_distribution(n, k, p):
    binomial_coefficient = factorial(n)/(factorial(k) * factorial(n-k))

    return binomial_coefficient * (p**k) * (1-p)**(n-k)

# initializing the values
n = 10  # total tosses
k = 6 # no. of heads
p = 0.5 #(probability of getting heads on a fair coin)

# calling the binomial_distribution() function
result = binomial_distribution(n, k, p)

# printing out the result
print(f"Approximate value = {result}")