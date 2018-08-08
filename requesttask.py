# coding=utf-8
import requests
import json
class requesttask:
    def reques(self,classid,npc_name):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        url = "http://10.7.13.75:31001/aiteacher/task"
        datas ={"input": classid, "userid": "liucongtest","name":npc_name}

        session = requests.session()
        requ = session.post(url, data=datas, headers=headers)
        res = requ.text
        #print(res)
        res = json.loads(res)
        return res




if __name__ == '__main__':
    #data={"input": "BKC_10300227078457", "userid": "liucongtest"}
    print requesttask().reques('BKC_10300227063341','Eric')






