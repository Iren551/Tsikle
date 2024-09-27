numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    is_prime = True
    if i < 2:
        continue
    else:
        f = i ** (1 / 2)
    for a in range(2, int(f + 1)):
        if i % a == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(i)
    else:
        primes.append(i)
print('Список простых чисел: ', primes)
print('Список составных чисел: ', not_primes)