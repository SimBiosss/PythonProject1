numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    count = 0
    for k in range(1, i + 1):
        if i % k == 0:
            count += 1
        if count == 2:
            is_prime = True
        else:
            is_prime = False
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)


print("Primes: ", primes)
print("Not Primes: ", not_primes)

