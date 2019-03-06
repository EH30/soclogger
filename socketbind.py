import time
import datetime
import getpass
import os
import sys
import socket

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

class BindListener:
    def __init__(self, host, port):
        global conn, clock

        Time = time.time()
        clock = datetime.datetime.fromtimestamp(Time).strftime("%Y-%m-%d %H_%M_%S")

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind((host, port))
        self.soc.listen(0)
        conn, addr = self.soc.accept()
        print ("Connected ", addr)

    def socket_bind_listener(self):
        while True:
            try:
                data = conn.recv(3000)
                data = data.strip()
                if data == "login":
                    pwd = getpass.getpass("Login: ")
                    conn.send(pwd)
                else:
                    print (data)
                    opnr = open(clock, "a+")
                    input_line = data + "\n"
                    opnr.write(input_line)
                    opnr.close()
                    #socket_bind_listener()
            except socket.error as E:
                print (E)
