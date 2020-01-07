import pymysql

def crack_mysql():
    Password=["123456","root","admin"]
    user='hxh'
    for i in Password:
        try:
            conn = pymysql.connect(host='127.0.0.1',user=user,password=i,database="woaiqiukui",charset='utf8')
            if (conn):
                print("mysql连接成功，用户名是：{}      密码是：{}".format(user,i))
                conn.close()
        except Exception:
            print("mysql密码{}错误".format(i))