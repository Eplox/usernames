#!/usr/bin/python
# -*- coding: UTF-8 -*-

names = open('names.txt','r').readlines()
x = []
for name in names:
    name = name.lower()
    if 'æ' in name or 'ø' in name or 'å' in name:
        name = name.replace('æ','a')
        name = name.replace('ø','o')
        name = name.replace('å','a')
    a = name.split()
    if len(a) == 2:
        x.append(a[0]+a[1])             # FirstnameLastname
        x.append(a[0]+'.'+a[1])         # Firstname.Lastname
        x.append(a[1]+''+a[0])          # LastnameFirstname
        x.append(a[1]+'.'+a[0])         # Lastname.Firstname
        x.append(a[0][0:3]+a[1][0:3])   # 3 first letters in first, then last name
        x.append(a[1][0:3]+a[0][0:3])   # 3 first letters in last, then first name
        x.append(a[0][0:2]+a[1][0:4])   # 2 first letters in first name, then 4 in last name
        x.append(a[1][0:2]+a[0][0:4])   # 2 first letters in last name, then 4 in first name
        x.append(a[0][0:4]+a[1][0:2])   # 4 first letters in first name, then 2 in last name
        x.append(a[1][0:4]+a[0][0:2])   # 4 first letters in last name, then 2 in first name
        x.append(a[0][0:3]+a[1][0:4])   # 3 first letters in first name, then 4 in last name
        x.append(a[1][0:3]+a[0][0:4])   # 3 first letters in last name, then 4 in first name
        x.append(a[0][0:4]+a[1][0:3])   # 4 first letters in first name, then 3 in last name
        x.append(a[1][0:4]+a[0][0:3])   # 4 first letters in last name, then 3 in first name
        x.append(a[0][0:4]+a[1][0:4])   # 4 first letters in first, then last name
        x.append(a[1][0:4]+a[0][0:4])   # 4 first letters in last, then first name
    elif len(a) == 3:
        x.append(a[0]+a[2])             # FirstnameLastname
        x.append(a[0]+'.'+a[2])         # Firstname.Lastname
        x.append(a[2]+''+a[0])          # LastnameFirstname
        x.append(a[2]+'.'+a[0])         # Lastname.Firstname
        x.append(a[0][0:3]+a[2][0:3])   # 3 first letters in first, then last name
        x.append(a[2][0:3]+a[0][0:3])   # 3 first letters in last, then first name
        x.append(a[0][0:2]+a[2][0:4])   # 2 first letters in first name, then 4 in last name
        x.append(a[2][0:2]+a[0][0:4])   # 2 first letters in last name, then 4 in first name
        x.append(a[0][0:4]+a[2][0:2])   # 4 first letters in first name, then 2 in last name
        x.append(a[2][0:4]+a[0][0:2])   # 4 first letters in last name, then 2 in first name
        x.append(a[0][0:3]+a[2][0:4])   # 3 first letters in first name, then 4 in last name
        x.append(a[2][0:3]+a[0][0:4])   # 3 first letters in last name, then 4 in first name
        x.append(a[0][0:4]+a[2][0:3])   # 4 first letters in first name, then 3 in last name
        x.append(a[2][0:4]+a[0][0:3])   # 4 first letters in last name, then 3 in first name
        x.append(a[0][0:4]+a[2][0:4])   # 4 first letters in first, then last name
        x.append(a[2][0:4]+a[0][0:4])   # 4 first letters in last, then first name
    else:
        print "[-] Unable to make username out of", name

f = open('usernames.txt', 'w+')
for l in x:
    f.write('%s\n' % l)
f.close()
print 'Check username.txt for generated login names'
