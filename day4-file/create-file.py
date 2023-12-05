# Description: Read names and marks from user and creat a file for the data,than display the file and show the count of name/mark pairs and the average mark

def write_data_to_file(file_name):#create file and read data from user
    total = 0
    my_file = open(file_name, 'w')
    while True:
        name = input("Enter name ('S' to Stop):")
        if name == 'S':
            break
        mark = input('Enter mark (0.0 to 10.0):')
        my_file.write(f'{name}\n{mark}\n')
        total += 1
    my_file.close()
    return total

def read_data_from_file(file_name):
    #read data from file and count the average mark
    with open(file_name, 'r') as file:
        count = 0
        total_mark = 0
        average = 0.0
        name = file.readline().rstrip('\n')
        while name != '':
            mark = float(file.readline().rstrip('\n'))
            print(f'{name:10}{mark:<5}')
            name = file.readline().rstrip('\n')
            count += 1
            total_mark += mark
            average = total_mark/count
    return count, average

def main(): 
    FILE_NAME = 'marks.txt'
    print('== Data written to file:', write_data_to_file(FILE_NAME))
    count, average = read_data_from_file(FILE_NAME)
    print(f'== Count: {count}, Average: {average:.2f}')

if __name__ == '__main__':
    main()
