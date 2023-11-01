import math

# Given prime numbers
p = 7
q = 13

# Calculate n
n = p * q
print("n =", n)

# Calculate Euler's totient function (phi)
phi = (p - 1) * (q - 1)

# Choose a public exponent (e)
e = 5

# Find a valid public exponent e
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

print("e =", e)

# Calculate the private exponent (d)
k = 2
d = (k * phi + 1) / e

# Make sure d is an integer
if not d.is_integer():
    raise ValueError("d is not an integer")

d = int(d)
print("d =", d)

# Display public and private keys
print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')

# Message to be encrypted
msg = 25
print(f'Original message: {msg}')

# Encryption
C = pow(msg, e, n)

print(f'Encrypted message: {C}')

# Decryption
M = pow(C, d, n)

print(f'Decrypted message: {M}')
