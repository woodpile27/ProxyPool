import requests
import time

class ProxyGetter(object):
    def get_raw_proxies(self):
        url = 'http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=db8a4ce4e60748e99297fdb1a3a82590&returnType=1&count=1'
        ip_list = requests.get(url).text.split()
        time.sleep(10)
        return ip_list
