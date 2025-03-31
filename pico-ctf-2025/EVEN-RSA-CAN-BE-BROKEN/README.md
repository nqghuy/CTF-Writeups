### 📌 Công thức giải mã RSA

**Mã hóa:**
cypher = flag ^ e (MOD N)

**Giải mã:**
flag = cypher ^ d (MOD N)

**Tính khóa bí mật: **
d = e ^ -1 (MOD euler_phi(N))

**Trong đó:**

euler_phi(N) = (p - 1) * (q - 1)

với p, q là 2 số nguyên tố



```code
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
```

```flag: picoCTF{tw0_1$_pr!m302ce519d} ```