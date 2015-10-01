palindrome_prime = lambda N: `N` == `N`[::-1] and N > 1 and all(N % i for i in range(2, N))

for i in range(1000):
    print(i)
    print(palindrome_prime(i))
    if palindrome_prime(i):
        print(i)

