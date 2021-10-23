import collections
import itertools


def get_prime_divisors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def calc_product(iterable):
    acc = 1
    for i in iterable:
        acc *= i
    return acc


def get_all_divisors(n):
    primes = get_prime_divisors(n)

    primes_counted = collections.Counter(primes)

    divisors_exponentiated = [
        [int(div) ** i for i in range(count + 1)]
        for div, count in primes_counted.items()
    ]

    for prime_exp_combination in itertools.product(*divisors_exponentiated):
        yield calc_product(prime_exp_combination)


a = int(input())
total = []
for g in range(1, a + 1):
    D = list(get_all_divisors(g))
    try:
        D.remove(g)
    except ValueError:
        pass
    if sum(D) == g:
        total.append(g)
if total:
    print(*total)
else:
    print(0)
