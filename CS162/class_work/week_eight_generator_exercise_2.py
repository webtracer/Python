def all_primes(limit):
    """
    prints all primes
    :param limit:
    :return:
    """
    if limit <= 2:
        raise StopIteration
    yield 2
    for i in range(3, limit, 2):
        for x in range(3, int(i**0.5)+2, 2):
            if not i % x:
                break
        else:
            yield i


if __name__ == '__main__':

    primes = all_primes(1000)

    for prime in primes:
        print(prime)

