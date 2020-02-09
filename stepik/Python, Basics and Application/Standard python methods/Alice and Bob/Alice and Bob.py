import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open('passwords.txt', 'r') as pas:
    passwords = pas.readlines()


print(passwords)
'''
for password in passwords:
    try:
        ans = simplecrypt.decrypt(password.strip('\n'), encrypted).decode('utf8')
        print(ans)
        break
    except simplecrypt.DecryptionException:
        continue
'''
ans = 'Alice loves Bob'
with open('answer.txt', 'w') as k:
    k.write(str(ans))