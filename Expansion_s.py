import os
import re

def get_all_file(suffix):
    #To get the file's suffix
    suffixx = ('\\' + re.search('.[a-zA-Z]$',suffix).group())
    #print(suffixx)

    path = os.getcwd()
    file_list = []

    #Recursive the folder to search the file
    for root, dirs, files in os.walk(path):
        for x in files:
            if (re.search(suffixx + '$', x)):
                file_path = os.path.join(root, x)
                file_list.append(file_path)

    #print(file_list)
    return file_list

if __name__ == '__main__':
    get_all_file('*.c')
