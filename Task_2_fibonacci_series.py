
# Task 2: Generate Fibonacci Series

def fibonacci_series(n):
    if n <= 1 :
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
    
try:
    x = int(input("enter the no. of terms for fibonacci series : "))    
    if x <= 0:
        print("enter a positive number.")
    else:
        for i in range(x):
            print(fibonacci_series(i),end=' ')
except:
    print("enter a valid integer.")