import os
import re
from fn_file import *
from fn_folder import *

def install_package():
    opinion = input("Would you like to install httpd for web (y/n): ")
    if opinion == 'y':
        os.system('sudo yum install httpd -y')
    else:
        print('Dont need httpd !')

def is_domain(domain_name='google.com'):
    # Kiểm tra domain hợp lệ bằng regex
    if not domain_name:
        return False
    regex = r"^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return re.match(regex, domain_name)
    
    
def create_web_directory(domain_name):
    set_permission_folder('/var/www/', 777)
    web_content = f'<p>Xin chào đây là trang web : {domain_name} </p>'
    web_folder_path = f'/var/www/{domain_name}/src'
    create_folder(web_folder_path)
    write_content_to_file(f'{web_folder_path}/index.html', web_content)
    set_permission_folder(web_folder_path, 777)
    set_permission_file(f'{web_folder_path}/index.html', 777)
    
def create_configuration_web_file(domain_name):
    handle_path = f'/etc/httpd/conf.d/{domain_name}.conf'
    file_content = f"""
    <VirtualHost *:80>
        ServerAdmin admin@{domain_name}
        DocumentRoot /var/www/{domain_name}/src
        ServerName {domain_name}
        ServerAlias www.{domain_name}

        ErrorLog /var/log/httpd/{domain_name}_error.log
        CustomLog /var/log/httpd/{domain_name}_access.log combined
    </VirtualHost>
    """
    write_content_to_file(handle_path,file_content)
    set_permission_file(handle_path, 777)
    
        
    
def restart_service():
    command = [
        f'sudo systemctl enable httpd',
        f'sudo systemctl restart httpd',
    ]
    for cmd in command:
        os.system(cmd)

install_package()
domain_name  = input("Enter domain name for website (domain name must have dns config in your laptop): ")
if not is_domain(domain_name):
    print('domain is unvalid !')
    exit()
create_web_directory(domain_name)
create_configuration_web_file(domain_name)
restart_service()


