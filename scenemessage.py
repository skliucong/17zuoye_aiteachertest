# coding=utf-8
import requests
import json
class scenemessage:
    def reques(self):
        headers = {
            "Content-Type": "application/json",
        }
        url = "http://10.6.3.241:1889/?group=alps-hydra-production&service=com.voxlearning.utopia.service.ai.api.DPAiService&method=loadAllAiDialogueLesson&version=20180411"
        datas ={"paramValues":[]}

        res = requests.post(url, data=json.dumps(datas), headers=headers).text
        res = json.loads(res)
        return res




if __name__ == '__main__':
    # for item in scenemessage().reques():
    #     print item
    print json.dumps(scenemessage().reques()[0]['topic'][0]['contents'][0]['pattern'])

