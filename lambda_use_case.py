
"""
A lambda function is a small anonymous function. 
A lambda function can take any number of arguments, but can only have one expression.

"""

# Regular function
def square(x):
    return x ** 2

# Equivalent lambda function
lambda_square = lambda x: x ** 2

# Using both functions
print(square(5))           
print(lambda_square(5))     


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

