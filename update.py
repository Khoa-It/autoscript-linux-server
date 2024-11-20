import os

os.system('cd ..')
os.system('rm -r autoscript-linux-server')
os.system('git clone https://github.com/Khoa-It/autoscript-linux-server.git')
os.system('chmod -R 777 autoscript-linux-server')
os.system('cd autoscript-linux-server/')