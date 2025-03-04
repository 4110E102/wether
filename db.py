import pymysql
import weather
#資料庫的設定
db_settings={
    "host":"127.0.0.1",
    "port":3306,
    "user":"training",
    "password":"Aa123456",
    "db":"training",
    "charset":"utf8"
}

try:
    #建立Connection物件
    conn = pymysql.connect(**db_settings)
    
    #建立Cursor物件
    with conn.cursor() as cursor:
        #資料庫相關的操作
        #新增料SQL語法
        command = "insert into weather(locationName,elementName,startTime,endTime,parameter)values(%s,%s,%s,%s,%s)"
        #取得天氣資料
        weather_data = weather.get_weather()
        
        for weather in weather_data:
            for items in weather["weatherElement"]:
                startTime= ""
                endTime= ""
                parameterName=""
                if(items["elementName"]=="WX"):
                    for times in items["time"]:
                        startTime=times["startTime"]
                        endTime=times["endTime"]
                        parameterName=times["parameter"]["parameterName"]
                        cursor.execute(
                            command,(weather["locationName"],items["elementName"],startTime,endTime,parameterName))
                        #儲存變更
                        conn.commit()
                        
except Exception as ex:
    conn.rollback()
    print(ex)




conn=pymysql.connect(**db_settings)

with conn.cursor() as cursor:
    
    command = "select * from weather where locationName=%s"
    cursor.excute(command,("嘉義縣"))
    
    result = cursor.fetchall()
    
    for row in result:
        locationName=row[0]
        elementName=row[1]
        startTime=row[2]
        endTime=row[3]
        parameterName=row[4]
        
        print("locationName=%s,elementName=%s,startTime=%s,endTime=%s,parameterName=%s"%
            (locationName,elementName,startTime,endTime,parameterName))
        
#%%%
conn=pymysql.connect(**db_settings)

with conn.cursor() as cursor:
    
    command = "update weather set locationName= %s where locationName=%s"
    cursor.execute(command,("嘉義縣edit","嘉義縣"))
    
    conn.commit()
    
#%%%
conn=pymysql.connect(**db_settings)

with conn.cursor() as cursor:
    
    command = "delete from weather where locationName=%s"
    cursor.execute(command,("嘉義縣edit"))
    
    conn.commit()

#%%%

conn=pymysql.connect(**db_settings)

with conn.cursor() as cursor:
    
    cursor.execute("drop table if exists weather")
    
    conn.commit()
