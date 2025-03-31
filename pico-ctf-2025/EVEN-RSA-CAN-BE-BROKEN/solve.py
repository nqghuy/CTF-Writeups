from pwn import *
from sage.all import *
from Crypto.Util.number import long_to_bytes
server = remote ('verbal-sleep.picoctf.net', 55510)
server.recvuntil(b'N: ')
N = int(server.recvline().decode())

server.recvuntil(b'text: ')
cypher = int(server.recvline().decode())
e = 65537
_privkey = euler_phi(N)
d = pow(e, -1, _privkey)
flag = pow(cypher, d, N) 
print(long_to_bytes(flag).decode())


