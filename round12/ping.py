import subprocess
import time

while True:
    #result = subprocess.check_output(['tracert', 'google.com'])
    result = subprocess.check_output(['tracert','google.com'])
    myfile = open("new.txt", "a")
    a = result.decode()
    myfile.write(a)
    time.sleep(3600)
    print(time.time())