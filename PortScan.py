from queue import Queue
import socket
from threading import Thread
import time
import requests
import IPy
import sys
import re
import mysqlcrack
import ftpcrack
import optparse

def confirm_ip_port():
    address=Queue(-1)
    ip = list((IPy.IP(sys.argv[1])))            #使用argv来传参
    port = '445,22,80,3306,21'                          
    port=port.split(',')
    for i in ip:
        for j in port:
            temp = (str(i),int(str(j)))
            address.put(temp)
    return address

def port_scan(address_queue):
    while not address_queue.empty():
        socket.setdefaulttimeout(0.01)      #设置超时时间
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        address = address_queue.get()
        try :
            s.connect(address)
            print('[+] IP:{} open : {}\n'.format(address[0],address[1]))
            if (address[1] == 80):                  #如果开放80端口则打印出其服务
                get_service(address[0])
            elif (address[1] == 3306):
                mysqlcrack.crack_mysql()
            elif (address[1] == 21):
                ftpcrack.crack_ftp()
        except Exception as e:
            s.close()
            time.sleep(0.8)
            print('[-] IP:{} close : {} or {}\n'.format(address[0],address[1],e))
        s.close()

def get_service(link):
    try:
        res = requests.get(url="http://"+link)
        res.encoding = ('utf-8')
        title = re.findall(r'<title>(.*)</title>',res.text)
        print("web站点的标题是："+"".join(title)+"\n")
    except Exception as e:
        print("error:{}".format(e))


if __name__ == "__main__":
    usage = "python %prog <targer IP> -t <threads num>"     #打印帮助信息
    parser = optparse.OptionParser(usage)                   #实例化对象
    parser.add_option('-t',dest='thread_num',type='int',help='threads nums')
    (options,args) = parser.parse_args()
    address = confirm_ip_port()
    thread = []
    for i in range(options.thread_num):                     #通过optparse来传参
        t= Thread(target=port_scan,args=(address,))
        t.start()
        thread.append(t)
    for i in thread:                        #子线程阻塞
        i.join()
    print ("扫描结束")

