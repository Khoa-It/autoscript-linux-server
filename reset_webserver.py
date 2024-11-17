import os
from fn_folder import *
from fn_file import *


def stop_service():
    os.system('sudo systemctl stop httpd')
    print("Web server stopped successfully.")

def delete_web_directory(domain_name=''):
    directory = f'/var/www/{domain_name}'
    other_directory = domain_name.split('.')[0]
    delete_folder(directory)
    delete_folder(other_directory)

def delete_web_configuration_file(domain_name):
    config_path = f'/etc/httpd/conf.d/{domain_name}.conf'
    delete_file(config_path)

def delete_logs(domain_name):
    error_log = f'/var/log/httpd/{domain_name}_error.log'
    access_log = f'/var/log/httpd/{domain_name}_access.log'
    for log_file in [error_log, access_log]:
        delete_file(log_file)

def restart_service():
    os.system('sudo systemctl start httpd')
    print("Web server restarted successfully.")

def reset_webserver(domain_name):
    stop_service()  # Tắt dịch vụ Apache trước khi thực hiện reset
    os.system(f'umount -l {domain_name}')
    delete_web_directory(domain_name)
    delete_web_configuration_file(domain_name)
    delete_logs(domain_name)

# Thực thi script reset web server
domain_name = input("Enter the domain name to reset (delete domain and web file): ")
if not domain_name:
    print('domain name null')
    exit()
reset_webserver(domain_name)
