import getpass
import os
def cred(filename):
    path = "./login/"
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        g = open(path + filename + ".txt", "r+")
    except FileNotFoundError:
        g = open(path + filename + ".txt", "w+")
    if not g.read(1):
        email = input("Username/Email/Phone : ")
        pwd = getpass.getpass("Password : ")
        print("Do you want EVA to save your username and password for " + filename + " ?")
        ask = input("Yes or No : ")
        if "Yes" in ask or "yes" in ask or "y" in ask or "Y" in ask: 
            for e in email:
                if e == '~':
                    g.write(e)
                else:
                    g.write(chr(ord(e)+2))
            g.write('\n')
            for p in pwd:
                if p == '~':
                    g.write(p)
                else:
                    g.write(chr(ord(p)+2))
    else:
        g.seek(0)
        print("Do you want EVA to automatically login for you?")
        ask = input("Yes or No : ")
        if "Yes" in ask or "yes" in ask or "y" in ask or "Y" in ask: 
            email = ''
            pwd = ''
            lines = g.read().splitlines()
            for e in lines[0]:
                if e == '~':
                    email += '~'
                else:
                    email += (chr(ord(e)-2))
            for p in lines[1]:
                if p == '~':
                    pwd += '~'
                else:
                    pwd += (chr(ord(p)-2))
                
        else:
            g.close()
            g = open("./login/" + filename + ".txt", "w+")
            email = input("Email(or phone) : ")
            pwd = getpass.getpass("Password : ")
            print("Do you want EVA to save your username and password for " + filename + " ?")
            ask = input("Yes or No : ")
            if "Yes" in ask or "yes" in ask or "y" in ask or "Y" in ask: 
                for e in email:
                    if e == '~':
                        g.write(e)
                    else:
                        g.write(chr(ord(e)+2))
                g.write('\n')
                for p in pwd:
                    if p == '~':
                        g.write(p)
                    else:
                        g.write(chr(ord(p)+2))
    g.close()
    return email, pwd