import random
# Thuật toán euclid mở rộng
def extended_euclid(a, b):
    x_2, x_1 = 1, 0
    y_2, y_1 = 0, 1
    while b > 0:
        q = a // b
        r = a % b
        x = x_2 - q * x_1
        y = y_2 - q * y_1

        a = b
        b = r
        x_2 = x_1
        x_1 = x
        y_2 = y_1
        y_1 = y

    return a, x_2, y_2

# Thuật toán lũy thừa theo modulo
def expo_modulo(b, n, m):
    x = 1
    power = b % m
    binary_n = []
    while n > 0:
        binary_n.append(n % 2)
        n = n // 2
    for i in binary_n:
        if i == 1:
            x = (x * power) % m
        power = (power * power) % m
    return x

def convert_name_to_number(name):
    m = 0
    for i in range(0, len(name)):
        m += (ord(name[i]) - ord('a')) * pow(26, len(name)-i-1)
    return m

def convert_number_to_name(m):
    name = ""
    while m > 0:
        q = m // 26
        r = m % 26
        name += chr(r+ord('a'))
        m = q
    return name[::-1]

def getD(phi_n, e):      # d = e^-1 mod phi_n
    d = extended_euclid(phi_n, e)[2]
    if d < 0:
        d += phi_n
    return d

def encode(name, e, n):    # c = m^e mod n
    m = convert_name_to_number(name)
    c = expo_modulo(m, e, n)
    return c

def decode(c, d, n):
    m = expo_modulo(c, d, n)
    return convert_number_to_name(m)
    

#tim so prime n bit
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,

                     31, 37, 41, 43, 47, 53, 59, 61, 67, 

                     71, 73, 79, 83, 89, 97, 101, 103, 

                     107, 109, 113, 127, 131, 137, 139, 

                     149, 151, 157, 163, 167, 173, 179, 

                     181, 191, 193, 197, 199, 211, 223,

                     227, 229, 233, 239, 241, 251, 257,

                     263, 269, 271, 277, 281, 283, 293,

                     307, 311, 313, 317, 331, 337, 347, 349]
 

def nBitRandom(n):

    return random.randrange(2**(n-1)+1, 2**n - 1)
 

def getLowLevelPrime(n):

    '''Generate a prime candidate divisible 

    by first primes'''

    while True:


        pc = nBitRandom(n) 
 

       

        for divisor in first_primes_list:

            if pc % divisor == 0 and divisor**2 <= pc:

                break

        else: return pc
 

def isMillerRabinPassed(mrc):

    '''Run 20 iterations of Rabin Miller Primality test'''

    maxDivisionsByTwo = 0

    ec = mrc-1

    while ec % 2 == 0:

        ec >>= 1

        maxDivisionsByTwo += 1

    assert(2**maxDivisionsByTwo * ec == mrc-1)
 

    def trialComposite(round_tester):

        if pow(round_tester, ec, mrc) == 1:

            return False

        for i in range(maxDivisionsByTwo):

            if pow(round_tester, 2**i * ec, mrc) == mrc-1:

                return False

        return True
 

   

    numberOfRabinTrials = 20

    for i in range(numberOfRabinTrials):

        round_tester = random.randrange(2, mrc)

        if trialComposite(round_tester):

            return False

    return True
 

def result(n):

    while True:

        

        prime_candidate = getLowLevelPrime(n)

        if not isMillerRabinPassed(prime_candidate):

            continue

        else:

            return prime_candidate

            break

if __name__ == '__main__':
    
    p = result(500)
    q = result(500)
    n = p * q
    e = 10000000000002342167
    name = "nguyenthiminhanh"
    
    d = getD((p-1)*(q-1), e)
    c = encode(name, e, n)
    
    print("HE MAT RSA")
    
    print('Ciphertext: ',name )
    print('p =',p)
    print('q =',q)
    print( 'e =',e)
    print('Public key: ( n =', n )
    print('e =' ,e)
    print('Text_to_number:', c)
    print('Private key: ( n =', n) 
    print( 'd =',d)
    print('Plaintext:', decode(c, d, n))
