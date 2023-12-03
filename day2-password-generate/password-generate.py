# Yingtong Lin
# Class: PROG12583-Programming Foundations-Python 1239-44137 FALL 2023
# Assignment: Assignment #4
# Program: assignment4_lin.py
# Description: Read name from user and generate a remdom password, creat lists for name and password.

import random 

def valid_name(name):
    #by using len() and .isalpha to identify if the name is at least 3 letters and if they are all letters.
   return True if len(name) >= 3 and name.isalpha() else False

def generate_password(name):
    #  use chr() convert index to character and make a list
    remdom_char = []
    for ch in range(33,123):
        char = chr(ch)
        remdom_char += char
    remdom_str = ''. join(random.sample(remdom_char, k=6))
     #  convert a list to string, or use for loop to convert every item in the list one by one
    password = str(name[0]) + str(len(name)) + remdom_str
    return password

def sign_up():
    names, passwords = [], []
    name = str(input("Enter name('S' to Stop):"))
    while name != 'S':
        if valid_name(name) == False: #eliminate the invalid name
            print('Name is invalid.')
            name = str(input("Enter name('S' to Stop):"))
            continue
        elif name not in names: # valid name
            password = generate_password(name)
            print(f'Hello {name}, your password is {password}')
            names.append(name)
            passwords.append(password)
        else: print('Name already exists.') 
        #eliminate the name that already exists
        name = str(input("Enter name('S' to Stop):"))
    return names, passwords

def get_password(name, names, passwords):
# by using the index of the name in "names list" to search the possword in "posswords list"
    if name in names:
        return passwords[names.index(name)]
    else: return 'None'

# DO NOT MODIFY ANY CODE BELOW THIS LINE
def main(): 
    names, passwords = sign_up()
    print('== Names:', names)
    print('== Passwords: ', passwords)
    if (n := len(names)) > 0:
        print(names[0], ':', get_password(names[0], names, passwords))
        print(names[n-1], ':', get_password(names[n-1], names, passwords)) 
        print('ProfSun', ':', get_password('ProfSun', names, passwords))     

if __name__ == '__main__':
    main()