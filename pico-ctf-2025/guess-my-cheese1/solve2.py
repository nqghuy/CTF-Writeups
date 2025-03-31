import string
s = input('cheese 1: ')
s_encrypted = input('encrpted chees 1: ')

s = s.lower()
s_encrypted = s_encrypted.lower()
def find_ab(s, s_encrypted):
    for a in range(100):
        for b in range(100):
            found = True
            for  i in range (len(s)):
                if s[i] not in string.ascii_lowercase:
                    continue
                p = ord(s[i]) - ord('a')
                c = ord(s_encrypted[i]) - ord('a')
                if (a * p + b) % 26 != c:
                    found = False
            if found == True:
                return a, b
    return None
def solve(a, b, secret):
    res = ''
    a_inv = pow(a, -1, 26)
    for c in secret:
        c = ord(c) - ord('a')
        res += chr(a_inv * (c - b) % 26 + ord('a'))
    return res
a, b = find_ab(s, s_encrypted)
print(a, b)
secret = input('secret: ')
secret = secret.lower()
print(solve(a, b, secret))