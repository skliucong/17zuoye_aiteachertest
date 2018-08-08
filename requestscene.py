# coding=utf-8
import requests
import json
class requestscene:
    def reques(self,classid):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        url = "http://10.7.13.75:31001/aiteacher/scene"
        datas ={"input": classid, "userid": "liucongtest"}

        session = requests.session()
        requ = session.post(url, data=datas, headers=headers)
        res = requ.text
        #print(res)
        res = json.loads(res)
        return res




if __name__ == '__main__':
    #data={"input": "BKC_10300227078457", "userid": "liucongtest"}
    print requestscene().reques('BKC_10300227078457')






