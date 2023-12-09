# Write a program containing the following functions

# Function 1: 
# - accept a name, return True if it is valid or False otherwise. A name is valid
#   if it has 6-15 characters of all letters or digits only. The first character
#   must be a letter. 
def read_name(name):
  name_valid = False
  if name[0].isalpha() and 6 <= len(name) <= 15:
    name_valid = True
  return name_valid

# Function 2: accept a password, return True if it is valid or False otherwise. 
# - a password is valid if it has 6-15 characters. The first character must be
#   a letter or a digit. A password must have at least one lower letter, one upper
#   letter, one digit, one special character. The password must has no space nor comma.
def read_password(password):
  if len(password) < 6 or len(password) > 15: return False 
  if ' ' in password or ',' in password: return False 
  if not password[0].isalnum(): return False
  cond1, cond2, cond3, cond4 = False, False, False, False 
  for ch in password:
    if ch.islower(): cond1 = True 
    if ch.isupper(): cond2 = True 
    if ch.isdigit(): cond3 = True 
    if not ch.isalnum(): cond4 = True 
  return cond1 and cond2 and cond3 and cond4
# by Pro.Sun

# Function 3: 
# - accept a file name, return no value. The function keeps on reading new name 
#   and password, write them to a file of the given name in csv format. That is,
#   one line for a pair of name and password, comma seperated. Repeat reading name 
#   if name is invalid or name already exists. Repeat reading password if it is invalid. 
def create_file(file_name):
  with open (file_name, 'w+') as file:
    name = input('Enter your name:')
    while True:
      if name == 's': break
      if read_name(name) == False or file.read().find(name) != -1:
        print('Name is invalid.')
        name = input('Enter your name:')
        continue
      password = input('Enter your password:')
      while password != '':
        if read_password(password) == False:
          print('Password is invalid.')
          password = input('Enter your password:')
          continue
        else: break
      file.write(f'{name},{password}\n')
      name = input('Enter your name:')


# Function 4:
# - accept a file name. Assume the file contains names and passwords in CSV format.
#   Read from the file all names and passwords, add them into two parallel lists.
#   Return the two lists.
import re
def split_file(file_name):
  with open (file_name, 'r') as file:
    str = file.read().rstrip('\n')
    lst = re.split(',|\n', str)
  return lst[::2], lst[1::2]

# Function 5: 
# - accept two parallel lists for all names and all passwords, and the maximum 
#   number of allowed attemps. Read name and password from the user until a match
#   is found in the two lists, or the maximum attempts have been reached.
def find_name_password(name, password, max = 2):
  #here i want the max try is 3 times, i set max here by 2, because before the for loop, i already have one input,i only need maximum 2 more input in the loop. so i set the max num is 2 and run the loop 3 times to reach the elif statement.
  user_name = input('Your user name:')
  for t in range(max+1):
    if user_name in name: break
    elif t < max:
      print('Try again!')
      user_name = input('Your user name:')
      continue
    elif t >= max:
      print('Reach the maximum number of attempts.')
      return
  user_password = input('Your pin:')
  for n in range(max+1):
    if user_password in password:
      print('Login successfully!')
      break
    elif n < max:
      print('Try again!')
      user_name = input('Your pin:')
      continue
    elif n >= max:
      print('Reach the maximum number of attempts.')
      return


# Write the main() to test all functions above.
def main():
  FILE_NAME = 'users-infor.txt'
  create_file(FILE_NAME)
  name, password= split_file(FILE_NAME)
  print(name, password)
  find_name_password(name, password)
main()