def isAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

with open('day4.txt') as f:
    lines = f.readlines()   #whole file stored as list

lines = [x.strip() for x in lines]
cnt = 0
for passphrase in lines:
    passwords = passphrase.split(' ')
    if len(passwords) == len(set(passwords)):
        cnt += 1
print('Number of valid passphrases is: ' + str(cnt))

print('----------------------------------')

cnt2 = 0
for passphrase in lines:
    passwords = passphrase.split(' ')
    flag = 0
    for i, password in enumerate(passwords):
        j = i+1
        while j < len(passwords):
            if isAnagram(password, passwords[j]):
                flag = 1
            j += 1
    if flag == 0:
        cnt2 += 1
print('Number of valid passphrases2 is:' + str(cnt2))