'''

Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 

=================


1. create_new_file(name_list, address_list, phone_list) --> 30% 
Get the names, addresses, phone of 10 different people as a list and write it to a file called 'contacts.txt' 

Input:
name_list = ['Joe', 'Max' ...]
address_list = ['Addr 1', 'Addr 2' ..]
phone_list = ['4041234567', '6161234567'..]

Output:
contacts.txt file

]

------------------------------------------------

2. compile_poem(file_list) --> 40%
 
Write a function that reads the 4 different paragraphs of road not taken, and combine it into a single file called 'road_not_taken.txt'. 

Input:
file_list = ['two_roads_1.txt', 'two_roads_2.txt', 'two_roads_3.txt', 'two_roads_4.txt']
Output:
road_not_taken.txt

----------------------------------------------------------------

3. write_custom_parser(file_name) --> 30% 

You're using a tool that outputs final grade of student in the format given in 'parsed_file.txt'.
Write a file parser that parses this document and gives output in format below.

Input:
file_name = 'parsed_file.txt'
Output:
result_list = [
    {
        'student': 'John,
        'year': 2019,
        'grade': B+
    }, ....
]


'''
import csv 
#1 

def create_new_file(name_list, address_list, phone_list):
    result_list = [{'name': name, 'address': address, 'phone': phone} 
    for name,address,phone in zip(name_list,address_list,phone_list)]

    keys = result_list[0].keys()

    output_file = open('contacts.csv', 'w')
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(result_list)

    output_file.close()

if __name__ == "__main__":
    name_list = ['Joe', 'Max', 'Nichole', 'Ruby', 'Sofia', 'Noah', 'Anna', 'Jared', 'Eric', 'Martin']
    address_list = ['Addr 1', 'Addr 2', 'Addr 3', 'Addr 4', 'Addr 5', 'Addr 6', 'Addr 7', 'Addr 8', 'Addr 9', 'Addr 10']
    phone_list = ['7354758876', '883628034', '6338569903', '1237984773', '3898376273', '386258826', '93252734', '383763793', '8375268373', '7254163474' ]

    create_new_file(name_list, address_list, phone_list)
   

#2 

def compile_poem(file_list):
    with open('roads_not_taken.txt', 'w') as outputfile:
        for names in file_list:
            with open(names) as inputfile: 
                outputfile.write(inputfile.read())
            outputfile.write("\n")


if __name__ == "__main__":
    file_list = ['tow_roads_1.txt', 'two_road_2.txt', 'two_roads_3.txt', 'two_roads_4.txt']
    compile_poem(file_list)


#3

def write_custom_parser(file_name):
    csv_fd = open(file_name, 'r')
    csv_reader = csv.reader(csv_fd)
    
    count = 0
    list_from_dicts = []
    int_dict = {}
    for row in csv_reader:
        row = row[0]
        if 'Student' in row:
            row = row.split()
            int_dict['student'] = row[1]
        if 'Year' in row:
            row = row.split()
            int_dict['year'] = row[1]
        if 'Grade' in row:
            row = row.split()
            int_dict['grade'] = row[1]
        count += 1 
        if count % 4 == 0:
            list_from_dicts.append(int_dict)
            int_dict = {}    

    return list_from_dicts

if __name__ == "__main__":
    file_name = 'parsed_file.txt'
    result = write_custom_parser(file_name)
    print(result)
