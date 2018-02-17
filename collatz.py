# Kirsty O'Brien 17/02/2018
#Collatz conjecture https://en.wikipedia.org/wiki/Collatz_conjecture
n = int(input("Please enter an integer: "))


while n > 1:
    if n % 2 == 0:
        n = n/2
        print(n)

    elif n % 2 == 1:
        n = n*3 + 1
        print(n)
    n = n
