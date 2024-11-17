import os
from fn_folder import *

def stop_service():
    os.system('sudo systemctl stop vsftpd')
    print('Service vsftpd stopped successfully!')

def delete_user_folder(username):
    userdir = f'/home/{username}/ftp'
    delete_folder(userdir)    

def reset_ftp():
    stop_service()
    ftp_user = input("Enter ftp user that you want delete folder ftp: ")
    if not ftp_user:
        print('Skipping delete folder user delete')
        exit()
    delete_user_folder(ftp_user)
    print('delete ftp user successfull !')

# Thực thi reset FTP
reset_ftp()
print('reset ftp successfull')
