def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
terms = 10
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")
