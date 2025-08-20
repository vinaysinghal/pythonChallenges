# Function to get factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Take input from user
num_1 = int(input('Enter a number: '))

# Print factorial of the number
print(f"Factorial of {num_1} is: ", factorial(num_1))