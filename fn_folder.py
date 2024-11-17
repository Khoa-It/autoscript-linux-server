import os

def create_folder(my_path):
    if os.path.exists(my_path):
        print('Folder is already existed !')
    else:
        os.makedirs(my_path, exist_ok = True)
        print('Create folder successfull !')

def set_folder_owner(username, folder_path):
    if not os.path.exists(folder_path):
        print('Folder not exists.')
        return
    os.system(f'sudo chown -R {username}:{username} {folder_path}')
    print('set owner for folder successfull')
    
def set_permission_folder( folder_path, permission):
    if not os.path.exists(folder_path):
        print('Folder not exists.')
        return
    os.system(f'sudo chmod -R {permission} {folder_path}')
    print('set permission successfull')
    
def delete_folder(folder_path):
    if not os.path.exists(folder_path):
        print('No found folder path to delete')
        return
    os.system(f'sudo rm -rf {folder_path}')
    print('deleted folder successfull')

        
