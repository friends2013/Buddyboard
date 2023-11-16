# text "database"
# made for TARDNET, a yggdrasil peer with DNS
db = open("/media/ezra/DATA/Dingle/list.txt", "r")

def query(name):
    for num, line in enumerate(db, 1):
        if name in line:
            return line.split(';')[1]

def queryIp(ip):
    for num, line in enumerate(db, 1):
        if ip in line:
            return line.split(';')[0] # So intersting

