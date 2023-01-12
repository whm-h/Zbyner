import zipfile
# jungle_zip = zipfile.ZipFile('./hello', 'w')

# jungle_zip.write('1.pdf', compress_type=zipfile.ZIP_DEFLATED)

# jungle_zip.close()


# class encrypt:
#     def Fragmented(value):
#         pass
#     def encrypted():
#         pass
class Zbyner:
    def Lockbyner(name,new_name):
        qp = open(f'.\\Data\\Unlocks\\{name}.zip','rb')
        a = qp.read()
        q = a.replace(b'PK', b'~&*')
        qw = open(f'.\\Data\\Locks\\{new_name}.zip','wb')
        qw.write(q)
    def Unlockbyner(name,new_name):
        qp = open(f'.\\Data\\Locks\\{name}.zip','rb')
        a = qp.read()
        q = a.replace(b'~&*', b'PK')
        qw = open(f'.\\Data\\Unlocks\\{new_name}.zip','wb')
        qw.write(q)

#with open("4.pdf", "ab") as f:
#Zbyner.Lockbyner('VPN Full Version', '7')
Zbyner.Unlockbyner('U1', 'U1')