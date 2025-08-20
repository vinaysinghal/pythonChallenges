# Get values using math module
import math

def mathcalculations(n):
    sqrt = math.sqrt(n)
    print(f'Square root: {sqrt}')
    naturllog = math.log(n)
    print(f'Logarithm: {naturllog}')
    sin = math.sin(n)
    print(f'Sine: {sin}')

# Take input from user
num_1 = int(input('Enter a number: '))

# Call function to get calculations
mathcalculations(num_1)