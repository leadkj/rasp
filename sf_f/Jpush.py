#coding:utf-8

import jpush



def Push_Message(title,message):
     app_key='eb53ff5f8cf6b231dcee511c'
     master_secret='895d74b79e04dfbc74d727fe'
      
     _jpush=jpush.JPush(app_key,master_secret)
     push=_jpush.create_push()
     _jpush.set_logging("DEBUG")
     push.audience=jpush.all_
     #android=jpush.android(alert="\n"+message,title="\n"+title+"\n",priority=1,style=2,alert_type=1,big_text="warning",extras={"k1":"v1"},inbox={"温度":"当前温度：{0:0.1f}*C,空气湿度：{1:0.1f}%".format(temperature,humidity),"i2":"v2"})
     android=jpush.android(alert="\n"+message,title="\n"+title+"\n",priority=1,style=1,alert_type=1,big_text="房间信息")
     
     push.notification=jpush.notification(alert="hello",android=android)
     push.platform=jpush.all_
     try:
          response=push.send()
     except common.Unauthorized:
         raise common.Unauthorized("unauth")
     except common.APIConnectionException:
         raise common.APIConnectionException("conn error")
     except common.JPushFailure:
         print("jpushfailure")
     except:
         print("exception")
