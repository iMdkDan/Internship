import sys
import os
from pathlib import Path

location = "C:/Users/zaina/Desktop"
print("Basic Terminal APP")
while True:
    code = input("Enter your Operation >>> \n")
    if code == 'echo me':
        echo = input("Enter the text")
        print(echo)
    if code == 'ls':
        t = input('If you want to use default Path then press 0 else press any key\n')
        if t == '0':
            location = "C:/Users/zaina/Desktop"
        else:
            location = input("Enter the path \n")
        dir_list = os.listdir(location)
        print("Files and Directiries in ",location," : ")
        print(dir_list)
    if code == 'mkdir':
        directory = input("Enter the Directory name\n")
        t= input('If you want to use default Path then press 0 else press any key\n')
        if t == '0':
            location = "C:/Users/zaina/Desktop"
        else:
            location = input("Enter the path \n")
        path_dir = os.path.join(location, directory)
        os.mkdir(path_dir)
        print("Directory '%s' created" % directory)
    if code == 'rmdir':
        directory = input('Enter the directory name to be removed\n')
        location = "C:/Users/zaina/Desktop"
        path_dir = os.path.join(location, directory)
        os.rmdir(path_dir)
        print("% s has been removed successfully" % directory)
    if code == 'touch':
        t = input('If you want to use default Path then press 0 else press any key\n')
        if t != '0':
            location = input("Enter the path \n")
        file = input("Enter the name and type of file\n")
        Path(location,file).touch()
        print("File '%s' created" % file)
    if code =='cat':
        os.system("echo 'Hello! Python is the best programming language.' >> ~/file.txt")
        os.system('cat ~/file.txt')
    if code == 'exit':
        sys.exit("Bye")
