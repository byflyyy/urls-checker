import requests
import time
t1 = 1649833628  #网页起始Unix时间戳 进行时效计算
url = "http://"  #测试网页地址
#r=requests.get(url)  #success 200   failure 403
#t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
if "200" in str(requests.get(url)):
    a = 0
    n = 60     #发包测试间隔(s)
    n1 = 5     #无响应重试次数
    n2 = 5     #无响应重试间隔
    while a < n1:  
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        r = requests.get(url)
        if "200" in str(r):
            print(t,"success")
            time.sleep(n)
        else:
            a = a + 1
            print(t,"error",str(r))
            time.sleep(n2)
    t2 = time.time()
    print("Totally:",t2-t1-n1*n2,"s")
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"Failed!")
else:
    print("Failed!",requests.get(url))