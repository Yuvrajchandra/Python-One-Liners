num1 = 5
num2 = 0
num3 = 10
num4 = 12
factorial = lambda num : 1 if num <= 1 else num*factorial(num-1)
print("Factorial of", num1, ":", factorial(num1))
print("Factorial of", num2, ":", factorial(num2))
print("Factorial of", num3, ":", factorial(num3))
print("Factorial of", num4, ":", factorial(num4))
