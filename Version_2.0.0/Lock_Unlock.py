import time
import os
class zbyner:

    def lizer(timer,name,pasword,file):
        if timer == 1:
            zbyner.lock(name, pasword, file)
        else:
            zbyner.unlock(name, pasword, file)
    def lock(name,pasword,file):
        a = file.read()
        place = open(f".\\files\\{name}.zip","bw")
        place.write(a)
        pas = open("password.py","w")
        pas.write("print(12)\n")
        pas.write(f"a = open(\".\\\\files\\\\{name}.zip\",\"br\")\n")
        pas.write("qr = a.read()\n")
        pas.write(f"qw = qr.replace(b'PK', b\"{pasword}\")\n")
        pas.write(f"b = open(\".\\\\files\\\\{name}.zip\",\"bw\")\n")
        pas.write("b.write(qw)")
        time.sleep(.2)
        os.startfile(".\\password.py")


    def unlock(name,pasword,file):
        a = file.read()
        place = open(f"files\\{name}.zip","bw")
        place.write(a)
        pas = open("password.py","w")
        pas.write("print(102)\n")
        pas.write(f"a = open(\".\\\\files\\\\{name}.zip\",\"br\")\n")
        pas.write("qr = a.read()\n")
        pas.write(f"qw = qr.replace(b'{pasword}', b\"PK\")\n")
        pas.write(f"b = open(\".\\\\files\\\\{name}.zip\",\"bw\")\n")
        pas.write("b.write(qw)")
        time.sleep(.2)
        os.startfile(".\\password.py")
        os.stat(".\\password.py")


# zbyner.lock("ali", "mhd", 3)