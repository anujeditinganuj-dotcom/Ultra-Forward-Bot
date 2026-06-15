import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = int(environ.get("API_ID", "37476811"))
    API_HASH = environ.get("API_HASH", "7aa60670b871050820086c6267371ee6")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8760503947:AAHelwW2hXYNEQXZAKVKPPZV-DQMVU8f_mQ") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Anujedit")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8730393744').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003824246703'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "log_ak_bots") 
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
