import os

def read_file(file_path):
    required_file = open(file_path, "r", encoding = 'utf-8')
    file_list = required_file.readlines()
    required_file.close()
    return file_list

def write_in_file(file_path, string):
    required_file = open(file_path, "a", encoding = 'utf-8')
    required_file.write(string)
    required_file.close()


def search_in_file(file_path, string):
    required_file = open(file_path, "r", encoding = 'utf-8')
    file_list = required_file.readlines()
    solution_list = list()
    list_two = list()
    for file_string in file_list:
        list_two = file_string.split()
        for file_string_2 in list_two:
            if file_string_2 == string:
                solution_list.append(file_string)
                break
    required_file.close()
    return solution_list

def string_in_list():
    string = str()
    a = input("Фамилия ")
    string = string + a + " "
    a = input("Имя ")
    string = string + a + " "
    a = input("Номер телефона ")
    string = string + a + " "
    return string

def remove_from_file(file_path, index):
    required_file = open(file_path, "r", encoding = 'utf-8')
    file_list = required_file.readlines()
    file_list.pop(index)
    required_file.close()
    required_file = open(file_path, "w", encoding = 'utf-8')
    for string in file_list:
        required_file.write(string)
    required_file.close()
    
def show_file(file_path):
    required_file = open(file_path, "r", encoding = 'utf_8')
    file_list = required_file.readlines()
    for string in file_list:
        print(string)
    required_file.close()

def save_data_in_file(file_path):
    string = string_in_list()
    write_in_file(file_path,"\n" + string)

def push_from_file_to_file(file_path1, file_path2, index):
    file_1_list = read_file(file_path1)
    write_in_file(file_path2, file_1_list[index])

def remove_from_file_by_string(file_path, string):
    required_file = open(file_path, "r", encoding = 'utf-8')
    file_list = required_file.readlines()
    file_list.remove(string)
    required_file.close()
    required_file = open(file_path, "w", encoding = 'utf-8')
    for string_new in file_list:
        required_file.write(string_new)
    required_file.close()

def rewrite_string_in_file(file_path, string):
    required_list = search_in_file(file_path, string)
    for string_index in required_list:
        remove_from_file_by_string(file_path, string_index)
    for string_index in required_list:
        replace_string = string_in_list()
        write_in_file(file_path,"\n" + replace_string)

def main():
    file_path = "Phone_book.txt"
    if  os.path.isfile(file_path) == False:
        required_file = open("Phone_book.txt", "w+")
        required_file.close() 
    else:
        pass
    flag = True
    while flag == True:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - изменить данные')
        print('5 - удалить запись')
        print('6 - перенести запись в другой файл')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data_in_file(file_path)
        elif answer == '2':
            show_file(file_path)
        elif answer == '3':
            string = input('Введите запрос на поиск: ')
            print(*search_in_file(file_path, string))
        elif answer == '4':
            string = input('Введите искомый параметр: ')
            rewrite_string_in_file(file_path, string)
        elif answer == '5':
            string = input('Введите искомый параметр: ')
            solution_list = search_in_file(file_path, string)
            for temp_string in solution_list:
                remove_from_file_by_string(file_path, temp_string)
        elif answer == '6':
            file_two = input('Введите файл, куда перенести данные')
            index = int(input('Введите номер строки'))
            push_from_file_to_file(file_path, file_two, index)
        else:
            pass

main()