# coding=utf-8
import requests
import json

##orige---requs
from taskmessage import taskmessage
from requesttask import requesttask
from jsgfopen import jsgfopen
class tasktest:
    f = open('logtask.csv', 'w')

    def maintest(self):
        for item in taskmessage().reques()[0:10]:
            print " "
            print "------------------------------------------------------------------------------------"
            print item['id']
            print "---  ---  ----  ----   ---------  ---------  ----------  ------  ------  -----  ---- "
            for npc in item['npcs']:
                print "------------------------------------------------------------------------------------"
                print 'npc: '+npc['npc_name']
                print "---  ---  ----  ----   ---------  ---------  ----------  ------  ------  -----  ---- "
                self.itemtest(npc,item['id'])

    def itemtest(self,itemjson,classid):

        npc_name=itemjson['npc_name']
        requs = requesttask().reques(classid,npc_name)


        #orige_begin_video=itemjson['begin']['video']
        #print orige_begin_video
        #requs_data0_content_video=requs['data'][0]['content']['video']
        #print requs_data0_content_video
        # if orige_begin_video==requs_data0_content_video:
        #     print "requs:  "+requs_data0_content_video+"      orige:  "+orige_begin_video
        #
        # else:
        #     print "not matching!!!!          requs:  " + requs_data0_content_video + "      orige:  " + orige_begin_video
        for  smallitem in itemjson['topic']:
            if smallitem==itemjson['topic'][0] :   ##第一次回复
                if(len(requs['data'])==2):
                    if requs['data'][0]['content']['audio']==itemjson['begin']['audio'] and requs['data'][1]['content']['cn_translation']==itemjson['topic'][0]['begin']['cn_translation']:
                        print ""
                        print classid+" orige begin not null , first matching"
                        self.smallitemlext1(itemjson['topic'][0]['contents'],classid,npc_name)
                    else:
                        print classid + "wrong! orige begin not null , first not matching!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                elif(len(requs['data'])==1):
                    if requs['data'][0]['content']['audio']==itemjson['topic'][0]['begin']['audio'] and requs['data'][0]['content']['cn_translation']==itemjson['topic'][0]['begin']['cn_translation']:
                        print ""
                        print classid + " orige begin is null , first matching"
                        self.smallitemlext1(itemjson['topic'][0]['contents'], classid,npc_name)
                    else:
                        print classid + " wrong! orige begin is null , first not matching!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                else:
                    print"wrong! 未知错误"
            elif smallitem==itemjson['topic'][1]:  ##第二次回复
                requs1_result=requesttask().reques(classid,npc_name) ##初始化
                #requs2_result_data=requestscene().reques(requs1_result['data'][-1]['help']['help_en'])['data']

                requs2_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][0]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改

                if len(requs2_result_data)==2:
                    print ""
                    print classid + " orige begin not null , second matching"
                    self.smallitemlext2(itemjson['topic'][1]['contents'],classid,itemjson,npc_name)
                elif len(requs2_result_data)==1:
                    print ""
                    print classid + "2 end!!!!"
                    # self.smallitemlext2(itemjson['topic'][1]['contents'], classid, itemjson, npc_name)

                else:
                    print 'requs2_result_data  wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'



                #???requs = requestscene().reques(itemjson['topic'][0])
            elif smallitem == itemjson['topic'][2]:  ##第三次回复
                requs1_result=requesttask().reques(classid,npc_name) ##初始化

                # requs2_result_data=requestscene().reques(requs1_result['data'][-1]['help']['help_en'])['data']
                # requs3_result_data = requestscene().reques(requs2_result_data[-1]['help']['help_en'])['data']

                requs2_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][0]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改
                requs3_result_data =requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][1]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改





                if len(requs3_result_data)==2:
                     print ""
                     print classid + "orige begin not null, third matching"
                     self.smallitemlext3(itemjson['topic'][2]['contents'], classid,itemjson,npc_name)
                elif len(requs3_result_data)==1:
                    print ""
                    print classid + "3__end!!!"
                else:
                    print 'requs3_result_data  wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
            elif smallitem == itemjson['topic'][3]:    ##第四次回复
                requs1_result = requesttask().reques(classid, npc_name)
                requs2_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][0]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改
                requs3_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][1]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改
                requs4_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][3]['contents'][0]['pattern']}),npc_name)['data']

                if len(requs4_result_data)==2:
                    self.smallitemlext4(itemjson['topic'][3]['contents'], classid, itemjson,npc_name)


            else:
                print "wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


    def smallitemlext1(self,orige_itemjson_topic_contents,classid,npc_name):
        for item in orige_itemjson_topic_contents:
            print "_______________________"


            jsgf=item['pattern']

            if jsgf!='*':
                sgf_requs_list = jsgfopen().requslist({'jsgf':jsgf})
            else:
                sgf_requs_list=["*"]


            for sgf_requs in  sgf_requs_list:
            ####################循环体###################################################
                orige_itemjson_topic_contents_level = item['feedback'][0]['level']

                requs = requesttask().reques(classid,npc_name)

                print 'tip : ' + requs['data'][-1]['help']['help_cn']
                print 'answer   : ' + sgf_requs

                smallitem_requs=requesttask().reques(sgf_requs,npc_name)
                requs_data_content_level=smallitem_requs['data'][0]['content']['level']
                print 'orige_itemjson_topic_contents_level: '+orige_itemjson_topic_contents_level
                print 'requs_data_content_level: '+requs_data_content_level
                if orige_itemjson_topic_contents_level!=requs_data_content_level:
                    print classid+"   first item not matching!!!!!!!!!!!!!!!!!!!!!!"
                    self.f.write(classid + "\t"+npc_name+"\t" + "1" +  "\t" + sgf_requs + "\t" + orige_itemjson_topic_contents_level + "\t" + requs_data_content_level + "\t" + "\n")

    ####################################################################################
                if orige_itemjson_topic_contents_level!='A+' and orige_itemjson_topic_contents_level!='A' and orige_itemjson_topic_contents_level!='B' and orige_itemjson_topic_contents_level!='C' and orige_itemjson_topic_contents_level!='D':
                    smallitem_requs = requesttask().reques(sgf_requs,npc_name)
                    requs_data_content_level = smallitem_requs['data'][0]['content']['level']
                    orige_itemjson_topic_contents_level = item['feedback'][1]['level']
                    print 'second orige_itemjson_topic_contents_level: ' + orige_itemjson_topic_contents_level
                    print 'second requs_data_content_level: ' + requs_data_content_level
                    if orige_itemjson_topic_contents_level != requs_data_content_level:
                        print classid + "   first2 item not matching!!!!!!!!!!!!!!!!!!!!!!"
                        self.f.write(
                            classid + "\t"+npc_name+"\t" + "1" + "\t" + sgf_requs+" secondtimes" + "\t" + orige_itemjson_topic_contents_level+ "\t" + requs_data_content_level + "\t" + "\n")

    def smallitemlext2(self,orige_itemjson_topic_contents,classid,itemjson,npc_name):
        for item in orige_itemjson_topic_contents:
            print "_______________________"

            jsgf = item['pattern']

            if jsgf != '*':
                sgf_requs_list = jsgfopen().requslist({'jsgf': jsgf})
            else:
                sgf_requs_list = ["*"]

            for sgf_requs in sgf_requs_list:
                #############################循环体###########################################
                orige_itemjson_topic_contents_level = item['feedback'][0]['level']
                requs1_result = requesttask().reques(classid,npc_name)  ##初始化
                requs2_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][0]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改

                print 'tip : ' + requs2_result_data[-1]['help']['help_cn']
                print 'answer   : ' + sgf_requs

                smallitem_requs = requesttask().reques(sgf_requs,npc_name)
                requs_data_content_level = smallitem_requs['data'][0]['content']['level']
                print 'orige_itemjson_topic_contents_level: ' + orige_itemjson_topic_contents_level
                print 'requs_data_content_level: ' + requs_data_content_level

                if orige_itemjson_topic_contents_level!=requs_data_content_level:
                    print classid+"   second item not matching!!!!!!!!!!!!!!!!!!!!!!"
                    self.f.write(classid +"\t"+npc_name+"\t"+"2"+"\t"+sgf_requs+"\t"+orige_itemjson_topic_contents_level+"\t"+requs_data_content_level+"\t"+"\n")
    ##############################################################################################################
                if orige_itemjson_topic_contents_level!='A+' and orige_itemjson_topic_contents_level!='A' and orige_itemjson_topic_contents_level!='B' and orige_itemjson_topic_contents_level!='C' and orige_itemjson_topic_contents_level!='D':
                    smallitem_requs = requesttask().reques(sgf_requs,npc_name)
                    requs_data_content_level = smallitem_requs['data'][0]['content']['level']
                    orige_itemjson_topic_contents_level = item['feedback'][1]['level']
                    print 'second orige_itemjson_topic_contents_level: ' + orige_itemjson_topic_contents_level
                    print 'second requs_data_content_level: ' + requs_data_content_level
                    if orige_itemjson_topic_contents_level != requs_data_content_level:
                        print classid + "   second2 item not matching!!!!!!!!!!!!!!!!!!!!!!"
                        self.f.write(
                            classid + "\t"+npc_name+"\t" + "2" + "\t" + sgf_requs+" secondtimes" + "\t" + orige_itemjson_topic_contents_level+ "\t" + requs_data_content_level + "\t" + "\n")


    def smallitemlext3(self,orige_itemjson_topic_contents,classid,itemjson,npc_name):
        for item in orige_itemjson_topic_contents:
            print ""
            print "_______________________"

            jsgf = item['pattern']

            if jsgf != '*':
                sgf_requs_list = jsgfopen().requslist({'jsgf': jsgf})
            else:
                sgf_requs_list = ["*"]

            for sgf_requs in sgf_requs_list:
                #####################循环体####################################################
                orige_itemjson_topic_contents_level = item['feedback'][0]['level']
                requs1_result = requesttask().reques(classid,npc_name)  ##初始化
                requs2_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][0]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改
                requs3_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][1]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改

                print 'tip : ' + requs3_result_data[-1]['help']['help_cn']
                print 'answer   : ' + sgf_requs

                smallitem_requs = requesttask().reques(sgf_requs,npc_name)
                requs_data_content_level = smallitem_requs['data'][0]['content']['level']
                print 'orige_itemjson_topic_contents_level: ' + orige_itemjson_topic_contents_level
                print 'requs_data_content_level: ' + requs_data_content_level

                if orige_itemjson_topic_contents_level!=requs_data_content_level:
                    print classid+"   third item not matching!!!!!!!!!!!!!!!!!!!!!!"
                    self.f.write(classid + "\t"+npc_name+"\t" + "3" + "\t" + sgf_requs + "\t" + orige_itemjson_topic_contents_level + "\t" + requs_data_content_level + "\t" + "\n")
    ####################################################################################################
                if orige_itemjson_topic_contents_level!='A+' and orige_itemjson_topic_contents_level!='A' and orige_itemjson_topic_contents_level!='B' and orige_itemjson_topic_contents_level!='C' and orige_itemjson_topic_contents_level!='D':
                    smallitem_requs = requesttask().reques(sgf_requs,npc_name)
                    requs_data_content_level = smallitem_requs['data'][0]['content']['level']
                    orige_itemjson_topic_contents_level = item['feedback'][1]['level']
                    print 'second orige_itemjson_topic_contents_level: ' + orige_itemjson_topic_contents_level
                    print 'second requs_data_content_level: ' + requs_data_content_level
                    if orige_itemjson_topic_contents_level != requs_data_content_level:
                        print classid + " third2  item not matching!!!!!!!!!!!!!!!!!!!!!!"
                        self.f.write(
                            classid + "\t"+npc_name+"\t" + "3" + "\t" + sgf_requs+" secondtimes" + "\t" + orige_itemjson_topic_contents_level+ "\t" + requs_data_content_level + "\t" + "\n")
    def smallitemlext4(self,orige_itemjson_topic_contents,classid,itemjson,npc_name):
        for item in orige_itemjson_topic_contents:
            print ""
            print "_______________________"

            jsgf = item['pattern']

            if jsgf != '*':
                sgf_requs_list = jsgfopen().requslist({'jsgf': jsgf})
            else:
                sgf_requs_list = ["*"]

            for sgf_requs in sgf_requs_list:
                #####################循环体####################################################
                orige_itemjson_topic_contents_level = item['feedback'][0]['level']
                requs1_result = requesttask().reques(classid,npc_name)  ##初始化
                requs2_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][0]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改
                requs3_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][1]['contents'][0]['pattern']}),npc_name)['data']  ##2018-8-8更改
                requs4_result_data = requesttask().reques(jsgfopen().requs({'jsgf': itemjson['topic'][2]['contents'][0]['pattern']}),npc_name)['data']
                print 'tip : ' + requs4_result_data[-1]['help']['help_cn']
                print 'answer   : ' + sgf_requs

                smallitem_requs = requesttask().reques(sgf_requs,npc_name)
                requs_data_content_level = smallitem_requs['data'][0]['content']['level']
                print 'orige_itemjson_topic_contents_level: ' + orige_itemjson_topic_contents_level
                print 'requs_data_content_level: ' + requs_data_content_level

                if orige_itemjson_topic_contents_level!=requs_data_content_level:
                    print classid+"   fourth item not matching!!!!!!!!!!!!!!!!!!!!!!"
                    self.f.write(classid + "\t"+npc_name+"\t" + "4" + "\t" + sgf_requs + "\t" + orige_itemjson_topic_contents_level + "\t" + requs_data_content_level + "\t" + "\n")
    ####################################################################################################
                if orige_itemjson_topic_contents_level!='A+' and orige_itemjson_topic_contents_level!='A' and orige_itemjson_topic_contents_level!='B' and orige_itemjson_topic_contents_level!='C' and orige_itemjson_topic_contents_level!='D':
                    smallitem_requs = requesttask().reques(sgf_requs,npc_name)
                    requs_data_content_level = smallitem_requs['data'][0]['content']['level']
                    orige_itemjson_topic_contents_level = item['feedback'][1]['level']
                    print 'second orige_itemjson_topic_contents_level: ' + orige_itemjson_topic_contents_level
                    print 'second requs_data_content_level: ' + requs_data_content_level
                    if orige_itemjson_topic_contents_level != requs_data_content_level:
                        print classid + " fourth2  item not matching!!!!!!!!!!!!!!!!!!!!!!"
                        self.f.write(
                            classid + "\t"+npc_name+"\t" + "4" + "\t" + sgf_requs+" secondtimes" + "\t" + orige_itemjson_topic_contents_level+ "\t" + requs_data_content_level + "\t" + "\n")




if __name__ == '__main__':
    tasktest().maintest()