def isPrime(n):

    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Check divisibility from 2 to √n using i*i <= n
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    # If no divisors were found, n is prime
    return True

if __name__ == "__main__":
    n = 8
    if isPrime(n):
        print("true")
    else:
        print("false")