import os

message = input("your message for commit : ")
if not message:
    print("your message is unvalid")
    exit()

os.system("git branch -M main")
os.system("git add .")
os.system(f'git commit -m \"{message}\" ')
os.system('git push origin main')