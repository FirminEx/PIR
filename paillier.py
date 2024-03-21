from utils import *
from Crypto.Util import number
from math import gcd


class Paillier:
    def __init__(self, bits):
        self.keyGen(bits)

    def keyGen(self, bits):
        p = number.getPrime(bits)
        q = number.getPrime(bits)
        n = p * q
        g = n + 1
        lambda_ = (p - 1) * (q - 1)
        mu = number.inverse(lambda_, n)
        
        self.n = n
        self.n2 = n **2
        self.g = g
        self.lambda_ = lambda_
        self.mu = mu
        self.public_key = (n, g)
        self.private_key = (lambda_, mu)
        

    def encrypt(self, message: int):
        if (message >= self.n or message < 0):
            raise Exception('Message should be smaller than n and positive')

        r = generate_random_encrypt(self.public_key[0])
        g_message = pow(self.g, message, self.n2)
        r_n = pow(r, self.n, self.n2) 
        
        return (g_message * r_n) % (self.n2)
            
    def decrypt(self, ciphertext: int):
        x = pow(ciphertext, self.lambda_, self.n ** 2)
        lx = x // (self.n - 1)
        
        return (lx * self.mu) % self.n
    
phe = Paillier(1024)

m = "Trying to encrypt this message using Paillier"
c = phe.encrypt(string_to_int(m))
assert(int_to_string(phe.decrypt(c)) == m)


m1 = string_to_int('This is the first message')
m2 = string_to_int('That is another message')
c1 = phe.encrypt(m1)
c2 = phe.encrypt(m2)

c1_c2_product = (c1 * c2) % phe.n2
assert(phe.decrypt(c1_c2_product) == m1 + m2)

c1_gm2_product =  c1 * pow(phe.g, m2, phe.n2)
assert(phe.decrypt(c1_gm2_product) == m1 + m2)

c1_pow_m2 = pow(c1, m2, phe.n2)
assert(phe.decrypt(c1_pow_m2) == m1 * m2)





