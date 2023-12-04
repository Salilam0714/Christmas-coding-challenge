# Write a Python program that has the following functions:

# - Read name(string), strength(float), can fly or not(boolean) about superheros 
#   from the user, until name is 's', write data to a file with each on one line like:
#     spiderman
#     8.2
#     True
#     superman
#     9.3
#     False
#     ...

def read_from_users(file_name):
  my_file = open(file_name, 'w')
  while True:
    name = str(input('Enter your name:'))
    if name == 's':
      break
    strength = float(input('Enter your strength(0.0 - 10.0):'))
    fly = str(input('Can fly or not(y/n):'))
    if fly == 'y':
      fly = True
    else:
      fly = False
    my_file.write(f'{name}\n{strength}\n{fly}\n')
  my_file.close()

# - Given a file name, read all data from the file into a list, remove new line from names, 
#   convert strength to number, convert can_fly to boolean, the returned list is like:
#     ['spiderman', 8.2, True, 'superman', 9.3, False, ...]

def read_remove_convert(file_name):
  lst = []
  with open(file_name, 'r') as file:
    name = file.readline().rstrip('\n')
    while name != '':
      lst.append(name)
      strength = float(file.readline().rstrip('\n'))
      fly = file.readline().rstrip('\n')
      name = file.readline().rstrip('\n')
      lst.append(strength)
      lst.append(fly)
  print(lst)
  return lst

# - Given a superhero list and a file name, increment all strength by 0.1, write all data in 
#   the list to the file with one data on one line

def increment(lst, file_name):
  for i in range(1, len(lst), 3):
    lst[i] += 0.1
  with open(file_name, 'w') as file:
    for item in lst:
      file.write("%s\n" %item)
  print(lst)

# - Given a superhero list, split the list to three parallel lists for name, strength,
#   can_fly, return them 

def split(lst):
 #version1
  # name, strength, can_fly = [], [], []
  # for i in range(0, len(lst), 3):
  #   name.append(lst[i])
  #   strength.append(lst[i + 1])
  #   can_fly.append(lst[i + 2])
  # print(name, strength, can_fly)
  # return name, strength,can_fly
 #version2
  return lst[::3], lst[1::3], lst[2::3]

# - Given three parallel lists, sort the three lists by name

def sort_by_name(name, strength, can_fly):
  pass

# - Given name and can_fly lists, split the name list to two: the names who can fly, 
#   the names who can't fly, return the two new lists 

def split_by_can_fly(name, can_fly):
  return [name[i] for i in range(len(can_fly)) if can_fly[i]], \
  [name[i] for i in range(len(can_fly)) if not can_fly[i]]


# - Given name and strength lists, split the name list to two: the names whose strength 
#   are over average, the names whose strength are below average, return the two new lists 
def split_by_strength(name, strength):
  big, small = [], []
  average = sum(strength)/len(strength)
  for i in strength:
    if i > average: big.append(name[i])
    else: small.append(name[i])
  return big, small



# - Write the main function to test all functions above
def main():
  FILE_NAME = 'superhero.txt'
  read_from_users(FILE_NAME)
  LIST = read_remove_convert(FILE_NAME)
  increment(LIST, FILE_NAME)
  name, strength, can_fly = split(LIST)
  # sort_by_name(name, strength, can_fly)
  split_by_can_fly(name, can_fly)
  split_by_strength(name, strength)
main()
