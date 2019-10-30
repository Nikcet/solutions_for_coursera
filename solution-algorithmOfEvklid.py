def gcd(a, b):
    if a != 0 and b != 0:
        if a < b:
            a, b = a, b % a
            gcd(a, b)
            if a == 0 or b == 0:
                print(a + b)
        else:
            a, b = a % b, b
            gcd(a, b)
            if a == 0 or b == 0:
                print(a + b)


a, b = int(input()), int(input())
gcd(a, b)
