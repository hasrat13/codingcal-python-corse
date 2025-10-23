def factorial(n):
    ans = 1
    for i in range(1, n + 1): # Loop from 1 up to n
        ans = ans * i
    return ans

num = 5
print(f"The factorial of {num} is {factorial(num)}")