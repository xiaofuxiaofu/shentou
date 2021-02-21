# 引入 datetime 模块
import datetime

def getYesterday(): 
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday
# 输出
print(getYesterday())
