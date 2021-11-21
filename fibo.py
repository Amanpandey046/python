#! /usr/bin/env python

# Function to print Fibonacci Series.
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# Take input from User.
number = int(input("Enter the Number : "))

# Call Series Function.
temp = list()

while number > -1:
   value = fibo(number)
   number = number - 1
   temp.append(value)

temp.reverse()
print(temp)
