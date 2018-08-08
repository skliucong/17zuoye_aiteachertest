# coding=utf-8
import requests
import json
class jsgfopen:

    def requs(self,jsgf):
        #print(jsgf)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        url = "http://10.7.13.75:9090/jsgf/expand"
        datas=jsgf
        session = requests.session()
        requ = session.post(url, data=datas, headers=headers)
        res = requ.text
        #print res
        res=json.loads(res)

        return res['data'][0]
    def requslist(self,jsgf):
        #print(jsgf)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        url = "http://10.7.13.75:9090/jsgf/expand"
        datas=jsgf
        session = requests.session()
        requ = session.post(url, data=datas, headers=headers)
        res = requ.text
        #print res
        res=json.loads(res)

        return res['data']

if __name__ == '__main__':
    datas = {
        "jsgf": ""}

    print jsgfopen().requslist(datas)