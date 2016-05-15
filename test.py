# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python
import sys

ArrayPick = int(sys.argv[1])
PreA = sys.argv[2].strip()
PreB = sys.argv[3].strip()

A = PreA.split(" ")
B = PreB.split(" ")


def am_prime(num):
    """Takes an integer and works if it's a Prime
       Input: integer
       Output: True/False
    """
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            return False
    return True

def divisableby(num,  num2):
    """Takes two integers and checks to see if they can be
    divided into a whole number
       Input: Integer/Intger
       Output: True/False
    """
    if (num % num2) == 0:
        return True
    return False

def am_coprime(num, num2):
    """Takes two integers and checks to see if they are both primes.
       Input: Integer/Integer
       Output: Integer (0,1,4,5)
    """
    coprime = 0
    if (am_prime(num)):
        coprime = 1
    if (am_prime(num2)):
        coprime = coprime + 4
    return coprime

Drop_count = 0
for ni in range(0, ArrayPick):
    for ib in range(0, len(B)):
        co_prime = am_coprime(int(A[ni]), int(B[ib]))
        if (co_prime == 0) or \
            (divisableby(int(A[ni]), int(B[ib]))) or \
            (divisableby(int(B[ib]), int(A[ni]))): 
            Drop_count += 1
            del B[0:ib]
            break
        elif (co_prime == 1):
            continue
        elif (co_prime == 5):
            break

print Drop_count
