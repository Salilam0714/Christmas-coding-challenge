# Write a program containing the following functions

# Function 1: 
# - accept a name, return True if it is valid or False otherwise. A name is valid
#   if it has 6-15 characters of all letters or digits only. The first character
#   must be a letter. 
def read_name():
  name_valid =''
  while True:
    name = input('Enter your name(letter or digit only, first must be letter):')
    if name[0].isalpha() and 6 <= len(name) <= 15:
      name_valid = True
      break
    else: 
      name_valid = False
      print('Name is invalid')
      continue
  return name_valid

# Function 2: accept a password, return True if it is valid or False otherwise. 
# - a password is valid if it has 6-15 characters. The first character must be
#   a letter or a digit. A password must have at least one lower letter, one upper
#   letter, one digit, one special character. The password must has no space nor comma.
def read_password():
  password_valid =''
  while True:
    password = input('Enter your password:')
    if not password[0].isalnum or not 6 <= len(password) <= 15:
      print('password is invalid.')
      continue
     

  return password_valid


# Function 3: 
# - accept a file name, return no value. The function keeps on reading new name 
#   and password, write them to a file of the given name in csv format. That is,
#   one line for a pair of name and password, comma seperated. Repeat reading name 
#   if name is invalid or name already exists. Repeat reading password if it is invalid. 
def create_file(file_name):
  user_infor = open(file_name, 'w')
  while True:
    name = read_name()
    password = read_password()
    user_infor.write(f'{name},{password}\n')


# Function 4:
# - accept a file name. Assume the file contains names and passwords in CSV format.
#   Read from the file all names and passwords, add them into two parallel lists.
#   Return the two lists.




# Function 5: 
# - accept two parallel lists for all names and all passwords, and the maximum 
#   number of allowed attemps. Read name and password from the user until a match
#   is found in the two lists, or the maximum attempts have been reached.




# Write the main() to test all functions above.
def main():
  name = read_name()
  print(name)
  password = read_password()
  print(password)
  FILE_NAME = 'users-infor.txt'
  create_file(FILE_NAME)
main()