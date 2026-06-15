import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = int(environ.get("API_ID", "34446649"))
    API_HASH = environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8779354652:AAEKi1dY-JkMz_WVWLSLD3qduSwIQcbyqrU") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Anujedit")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7892805795').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003475522251'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "anujeditbyak") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = int(environ.get('PORT', '8081'))
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
