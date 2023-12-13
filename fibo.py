def fibonacci(n):
    fib_series = []
    a, b = 0, 1

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

# Example: Generate Fibonacci series up to 10 terms
num_terms = 10
result = fibonacci(num_terms)
print(f"Fibonacci series up to {num_terms} terms: {result}")
