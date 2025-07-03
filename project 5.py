# This program prints the Fibonacci sequence using recursion
# Define the recursive function
def fibonacci(n):
    if n < 0:
        print("Please enter a positive number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Ask the user how many terms to print
terms = int(input("Enter how many terms of Fibonacci sequence you want: "))
# Print the sequence
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i))