x = 2231129

isPrime = True
for i in range(2, x):
    if (x % i) == 0:
        isPrime = False

if isPrime:
    print x, "is prime"
else:
    print x, "is not prime"
