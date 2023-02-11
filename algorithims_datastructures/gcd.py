# GCD: greatest common denominator

# Psuedo code
# 1. for a and b, a greater than b, divide a by b
#  2. set remainder to b, if b or remainder is 0 return b
#  3. else set a to b, b to remainder and go back to 1 until b is 0

def gcd(a, b):
    while (b):
        tmp = a  # creating a tmp a
        a = b  # setting a to b
        b = tmp % b  # b to remainder
    return a


print(gcd(20, 8))
print(gcd(60,  96))
