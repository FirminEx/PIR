from utils import *
from Crypto.Util import number
from math import gcd


class Paillier:
    def __init__(self, bits):
        self.key_gen(bits)

    def key_gen(self, bits):
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
        

    def encrypt(self, message: int, public_key: (int, int)):
        if (message >= public_key[0] or message < 0):
            raise Exception('Message should be smaller than n and positive')

        r = generate_random_encrypt(public_key[0])
        g_message = pow(public_key[1], message, public_key[0] ** 2)
        r_n = pow(r, public_key[0], public_key[0] ** 2) 
        
        return (g_message * r_n) % (public_key[0] ** 2)
            
    def decrypt(self, ciphertext: int):
        x = pow(ciphertext, self.lambda_, self.n ** 2)
        lx = x // (self.n - 1)
        
        return (lx * self.mu) % self.n
    
phe = Paillier(1024)

m = "Trying to encrypt this message using Paillier"
c = phe.encrypt(string_to_int(m), phe.public_key)
assert(int_to_string(phe.decrypt(c)) == m)


m1 = string_to_int('This is the first message')
m2 = string_to_int('That is another message')
c1 = phe.encrypt(m1, phe.public_key)
c2 = phe.encrypt(m2, phe.public_key)

c1_c2_product = (c1 * c2) % phe.n2
assert(phe.decrypt(c1_c2_product) == m1 + m2)

c1_gm2_product =  c1 * pow(phe.g, m2, phe.n2)
assert(phe.decrypt(c1_gm2_product) == m1 + m2)

c1_pow_m2 = pow(c1, m2, phe.n2)
assert(phe.decrypt(c1_pow_m2) == m1 * m2)





