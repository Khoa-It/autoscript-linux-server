import os
import subprocess

def user_exists(username):
    return os.system(f'id -u {username} > /dev/null 2>&1') == 0

def create_user(username):
    if not username:
        print('Username is unvalid !')
        return False
    else:
        if user_exists(username):
             print(f"User '{username}' already exists. Skipping user creation.")
             return True
        else:
            password = input("Enter the password: ")
            os.system(f'sudo adduser {username}')
            os.system(f'echo "{username}:{password}" | sudo chpasswd')
            print(f'User {username} created successfully!')
            return True

def delete_user(username):
    if not username:
        print('username is unvalid')
        return
    try:
        subprocess.run(["sudo", "userdel", username], check=True)
        print(f"User {username} deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete user {username}.")
        
def check_user(username):
    if not username:
        print('username is unvalid')
        return
    os.system(f'id {username}')