import os
from fn_user import *


os.system('clear')
print('=======user script==========')
print('1. create user')
print('2. delete user')
print('3. check user')
print('=========')
choice = input("Enter your choice: ")
if not choice:
    print("your choice is unvalid")
    exit()
if choice == "1" :
    username = input("Enter username: ")
    create_user(username)
    exit()
if choice == "2" :
    username = input("Enter username: ")
    delete_user(username)
    exit()
if choice == "3" :
    username = input("Enter username: ")
    check_user(username)
    exit()
print('your choice is unvalid - ')