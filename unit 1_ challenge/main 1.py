def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


num = int(input("enter a non-negative number :"))

if num < 0:
  print("factorial is not defined for negative number")

else:
  result = factorial(num)
  print(f"the factorial of {num} is {result}")
