s1 = input('cheese 1: ')
s1_encrypted = input('encrpted chees 1: ')
s2 = input('cheese 2 : ')
s2_encrypted = input('encrypted cheese 2 : ')

hsh = dict()

# create hash table from (encrypted) s1, s2
for i in range(len(s1)):
    hsh[s1[i]] = s1_encrypted[i]
for i in range(len(s2)):
    hsh[s2[i]] = s2_encrypted[i]

# the cheese need to be decrypted
cheese = input('secret: ')
result = ''
for x in cheese:
    ok = False
    for key in hsh:
        if hsh[key] == x:
            ok = True
            result = result + key
            break
    # can't found hash of the char
    if ok == False :
        result = result + '-'
print (result)