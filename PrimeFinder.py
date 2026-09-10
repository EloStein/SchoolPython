from math import sqrt

# Checks for Prime Number
def isPrime(num):

    if not num.is_integer():
        return "Gib 'ne Zahl ein, du Mendez"

    num_root = sqrt(num)

    if num == 1 :
        return False

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(num_root), 6) :
        if num % i == 0 or num % (i + 2) ==  0:
            return False
    return True


i = 0
while i < 1000000:
    if isPrime(i) :
        print(i)
    i = i + 1

