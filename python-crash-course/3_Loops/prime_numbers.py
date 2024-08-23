# Math concepts on the practice quiz

# prime numbers - Integers that have only two factors, which are the number itself multiplied by 1.
# The first ten prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29. Each of these prime numbers can be evenly divided only by itself and 1.

# prime factors - Prime numbers that are factors of an integer. For example, the prime numbers 2 and 5 are the prime factors of the number 10 (2x5=10).
# The prime factors of an integer will not produce a remainder when used to divide that integer.

# divisor - A number (denominator) that is used to divide another number (numerator). For example, if the number 10 is divided by 5, the number 5 is the divisor.

# sum of all divisors of a number - The result of adding all of the divisors of a number together.

# multiplication table - An integer multiplied by a series of numbers and their results formatted as a table or a list.


def count_factors(given_number):
    factor = 1
    count = 1

    if given_number == 0:
        return 0

    while factor < given_number:
        if given_number % factor == 0:
            count += 1
        factor += 1
    return count


print(count_factors(0))
print(count_factors(3))
print(count_factors(10))
