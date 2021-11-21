#! /usr/bin/env python

# Function to print Fibonacci Series.
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = fibo(n-1)
        print(temp)

# Take input from User.
number = int(input("Enter the Number"))

# Call Series Function.
fibo(number)

