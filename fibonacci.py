def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    fibonacci(n)
