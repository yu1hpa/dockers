###
# Sample for gmpy2
###
from gmpy2 import *
print(iroot(125,3))
assert iroot(125,3)==(mpz(5), True)


###
# Sample for pycryptodome
###
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

def gen_key():
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    phi = (p-1)*(q-1)
    e = 65537
    d = inverse(e,phi)
    return (e,n),(d,n)

def encrypt(m,e,n):
    return pow(m,e,n)

def decrypt(c,d,n):
    return pow(c,d,n)

if __name__ == "__main__":
    (e,n),(d,n) = gen_key()
    m = bytes_to_long(b"Hello World")
    c = encrypt(m,e,n)
    print(long_to_bytes(decrypt(c,d,n)))
    assert long_to_bytes(decrypt(c,d,n))==b"Hello World"
