"""
A dataset of test scores is normally distributed with a mean of 70 and a standard deviation of 10. What percentage of students scored between 60 and 80?
"""
import math

# Function to calculate the z-score
def calculate_z(x, mean, std_dev):
    return (x - mean) / std_dev

# Function to calculate the CDF using the standard normal distribution approximation
def standard_normal_cdf(z):
    # Using an approximation for the CDF of standard normal distribution
    # CDF for N(0, 1)
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

# Function to calculate the probability of scores between x1 and x2
def gauss_distribution(x1, x2, mean, std_dev):
    z1 = calculate_z(x1, mean, std_dev)
    z2 = calculate_z(x2, mean, std_dev)
    
    # Computing CDF for z1 and z2
    phi1 = standard_normal_cdf(z1)
    phi2 = standard_normal_cdf(z2)
    
    # Probability is the difference between the CDF values
    return phi2 - phi1

# initializing the values
x1 = 60
x2 = 80
mean = 70
std_dev = 10

# calling he function 
result = gauss_distribution(x1, x2, mean, std_dev)

# printing out the result
print(f"Percentage of students scoring between {x1} and {x2}: {result * 100:.2f}%")
