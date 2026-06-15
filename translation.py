#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

import os
from config import Config

class Translation(object):

  PHOTO_URL = "https://image.zaw-myo.workers.dev/image/4ff61456-0c62-4b38-a92e-919e70bda978"
  
  START_TXT = """<b>ʜɪ {}

➻ ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
➻ ɪ ᴄᴀɴ ꜰᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ꜰʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ

➻ ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ</b>

<b>Bᴏᴛ Iꜱ Mᴀᴅᴇ Bʏ <a href='https://t.me/anujedits76'>Aɴᴜᴊ Kᴜᴍᴀʀ</a></b>"""


  DONATE_TXT = """<b><i>If you liked me ❤️. consider make a donation to support my developer 👦

UPI ID - </i></b><code>971916880@ybl</code>"""

  HELP_TXT = """<b><u>🔆 ʜᴇʟᴘ</b></u>

<u>**📚 ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:**</u>

<b>
⏣ __/start - ᴄʜᴇᴄᴋ ɪ'ᴍ ᴀʟɪᴠᴇ__  
⏣ __/forward - ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇs__  
⏣ __/unequify - ᴅᴇʟᴇᴛᴇ ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇssᴀɢᴇs ɪɴ ᴄʜᴀɴɴᴇʟs__  
⏣ __/settings - ᴄᴏɴғɪɢᴜʀᴇ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs__  
⏣ __/reset - ʀᴇsᴇᴛ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs__  
⏣ __/donate - ᴅᴏɴᴀᴛᴇ ᴛᴏ ᴅᴇᴠᴇʟᴏᴘᴇʀ__  
⏣ __/stop - ᴄᴀɴᴄᴇʟ ʏᴏᴜʀ ᴏɴɢᴏɪɴɢ ғᴏʀᴡᴀʀᴅɪɴɢ__
</b>

<b><u>💢 ғᴇᴀᴛᴜʀᴇs:</u></b>

<b>
► __ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴘᴜʙʟɪᴄ ᴄʜᴀɴɴᴇʟ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ. ɪғ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ɪs ᴘʀɪᴠᴀᴛᴇ, ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ__
► __ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ʙʏ ᴜsɪɴɢ ᴜsᴇʀʙᴏᴛ (ᴜsᴇʀ ᴍᴜsᴛ ʙᴇ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜᴇʀᴇ)__
► __ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ__
► __ᴄᴜsᴛᴏᴍ ʙᴜᴛᴛᴏɴ__
► __sᴜᴘᴘᴏʀᴛ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴄʜᴀᴛs__
► __sᴋɪᴘ ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇssᴀɢᴇs__
► __ғɪʟᴛᴇʀ ᴛʏᴘᴇ ᴏғ ᴍᴇssᴀɢᴇs__
► __sᴋɪᴘ ᴍᴇssᴀɢᴇs ʙᴀsᴇᴅ ᴏɴ ᴇxᴛᴇɴsɪᴏɴs & ᴋᴇʏᴡᴏʀᴅs & sɪᴢᴇ__
</b>
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz
  
  HOW_USE_TXT = """<b><u>⚠️ ʙᴇғᴏʀᴇ ғᴏʀᴡᴀʀᴅɪɴɢ:</u></b>

<b>► __ᴀᴅᴅ ᴀ ʙᴏᴛ ᴏʀ ᴜsᴇʀʙᴏᴛ__
► __ᴀᴅᴅ ᴀᴛ ʟᴇᴀsᴛ ᴏɴᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ__ `(ʏᴏᴜʀ ʙᴏᴛ/ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇʀᴇ)`
► __ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄʜᴀᴛs ᴏʀ ʙᴏᴛs ʙʏ ᴜsɪɴɢ /settings__
► __ɪғ ᴛʜᴇ **ғʀᴏᴍ ᴄʜᴀɴɴᴇʟ** ɪs ᴘʀɪᴠᴀᴛᴇ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴛʜᴇʀᴇ ᴏʀ ʏᴏᴜʀ ʙᴏᴛ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ ɪɴ ᴛʜᴇʀᴇ ᴀs ᴡᴇʟʟ__
► __ᴛʜᴇɴ ᴜsᴇ /forward ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇs__</b>"""

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
  
  ABOUT_TXT = """<b>
╔════❰ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : ғᴏʀᴡᴀʀᴅ ʙᴏᴛ
║┣⪼👦ᴄʀᴇᴀᴛᴏʀ : ᴀɴᴜᴊ ᴋᴜᴍᴀʀ
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 1.0.6
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
  
  STATUS_TXT = """<b>
╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs  ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼👱 ᴛᴏᴛᴀʟ  ᴜsᴇʀs : <code>{}</code>
║┃
║┣⪼🤖 ᴛᴏᴛᴀʟ ʙᴏᴛ : <code>{}</code>
║┃
║┣⪼🔃 ғᴏʀᴡᴀʀᴅɪɴɢs : <code>{}</code>
║┃
║┣⪼🔍 ᴜɴᴇǫᴜɪꜰʏɪɴɢs: <code>0</code>
║┃
║┣⪼📢 ᴛᴏᴛᴀʟ ᴄʜᴀɴɴᴇʟs: <code>{}</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>""" 

  SERVER_TXT = """<b>
╔════❰ sᴇʀᴠᴇʀ sᴛᴀᴛs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ ᴛᴏᴛᴀʟ ᴅɪsᴋ sᴘᴀᴄᴇ: <code>38 GB</code>
║┣⪼ ᴜsᴇᴅ: <code>1.54 GB</code>
║┣⪼ ꜰʀᴇᴇ: <code>36.46 GB</code>
║┣⪼ ᴄᴘᴜ: <code>{}%</code>
║┣⪼ ʀᴀᴍ: <code>{}%</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪</b>"""
  
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"

  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"

  SKIP_MSG = "<b><u>sᴇᴛ ɴᴏ. ᴏғ ᴍᴇssᴀɢᴇs ᴛᴏ sᴋɪᴘ 📃</u></b>\n\n<b>You can skip a certain number of messages and forward the rest.\n\nDefault Skip Number = 0</b>\n\n<b><i>Example: If you enter 0, no messages will be skipped.\nIf you enter 5, the first 5 messages will be skipped.</i></b>\n/cancel <b>- cancel this process</b>"

  CANCEL = "<b>Process Cancelled Succefully !</b>"

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"

  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """<b>╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs  ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼<b>𖨠 ᴛᴏᴛᴀʟ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ғᴇᴄʜᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ғᴏʀᴡᴀʀᴅᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴅᴇʟᴇᴛᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 sᴋɪᴘᴘᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ғɪʟᴛᴇʀᴇᴅ ᴍᴇssᴀɢᴇs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs: </b> <code>{}</code>
║┃
║┣⪼<b>𖨠 ᴘᴇʀᴄᴇɴᴛᴀɢᴇ: </b> <code>{}</code>%
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ <b>{}</b> ❱══❍⊱❁"""

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
  DOUBLE_CHECK = """<b><u>ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋɪɴɢ 📋</b></u>

<b>ʙᴇꜰᴏʀᴇ ꜰᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ ᴍᴇssᴀɢᴇs ᴄʟɪᴄᴋ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴏɴʟʏ ᴀꜰᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ</b>


<b>★ ʏᴏᴜʀ ʙᴏᴛ: {botname}</b>
<b>★ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ: {from_chat}</b>
<b>★ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ: {to_chat}</b>
<b>★ sᴋɪᴘ ᴍᴇssᴀɢᴇs: {skip}</b>

<i><b>° {botname} ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ</i> ({to_chat})</b>
<i><b>° ɪꜰ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ ɪs ᴘʀɪᴠᴀᴛᴇ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴍᴇᴍʙᴇʀ ᴏʀ ʏᴏᴜʀ ʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇʀᴇ ᴀʟsᴏ</b></i>

<b>ɪꜰ ᴛʜᴇ ᴀʙᴏᴠᴇ ɪs ᴄʜᴇᴄᴋᴇᴅ ᴛʜᴇɴ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴄᴀɴ ʙᴇ ᴄʟɪᴄᴋᴇᴅ</b>"""


#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

  # ============ PLAN / PREMIUM TEXTS ============

  MY_PLAN_TXT = """💎🎫 <b>ᴍʏ ᴘʟᴀɴ</b> 🎫💎

👤 <b>ᴜsᴇʀ :</b> {}
⚡ <b>ᴜsᴇʀ ɪᴅ :</b> <code>{}</code>
💎 <b>ᴘʟᴀɴ :</b> {}
📊 <b>ᴘʟᴀɴ ᴛʏᴘᴇ :</b> {}
📅 <b>ʀᴇɢɪsᴛʀᴀᴛɪᴏɴ ᴅᴀᴛᴇ :</b> {}
⏰ <b>ᴇxᴘɪʀʏ :</b> {}

✨ <b>ғᴇᴀᴛᴜʀᴇs ᴜɴʟᴏᴄᴋᴇᴅ :</b>

{}

💡 <i>ᴛɪᴘ: ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴜɴʟᴏᴄᴋ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs!</i>"""

  PLAN_DETAIL_TXT = """{emoji} <b>{name} ᴘʟᴀɴ</b> {emoji}

📝 <b>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:</b>
{description}

💰 <b>ᴘʀɪᴄᴇ:</b> {price} ғᴏʀ {days} ᴅᴀʏs

✨ <b>ғᴇᴀᴛᴜʀᴇs ɪɴᴄʟᴜᴅᴇᴅ:</b>
{features}

💡 <b>ᴡᴀɴᴛ ᴛᴏ ᴜᴘɢʀᴀᴅᴇ?</b>
ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴘᴜʀᴄʜᴀsᴇ ᴛʜɪs ᴘʟᴀɴ"""

  SUBSCRIPTION_TXT = """💳 <b>sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>

ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴘᴇʀғᴇᴄᴛ ᴘʟᴀɴ ғᴏʀ ʏᴏᴜʀ ɴᴇᴇᴅs

{}"""

  PLAN_DESCRIPTIONS = {
    "ғʀᴇᴇ": "ᴏɴʟʏ ᴄᴏɴғɪɢᴜʀᴀᴛɪᴏɴ ᴏᴘᴛɪᴏɴs ᴀᴠᴀɪʟᴀʙʟᴇ",
    
    "ᴘʟᴜs": "ᴏɴʟʏ ғᴏʀᴡᴀʀᴅɪɴɢ, ɴᴏ ғᴛᴍ ᴍᴀɴᴀɢᴇʀ ғᴇᴀᴛᴜʀᴇ",
    
    "ᴘʀᴏ": "ɢᴀᴍᴍᴀ ᴍᴏᴅᴇ, ᴡᴀᴛᴇʀᴍᴀʀᴋ, ᴛᴇxᴛ ᴏɴʟʏ + ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴘʟᴜs ᴘʟᴀɴ",
    
    "ɪɴғɪɴɪᴛʏ": "ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴘʀᴏ ᴘʟᴀɴ & ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴀᴋʙᴜᴄᴋs ɪɴᴄʟᴜᴅɪɴɢ ғᴛᴍ ᴍᴀɴᴀɢᴇʀ ᴇxᴄᴇᴘᴛ ᴅᴇʟᴛᴀ, ᴛʜᴇᴛᴀ, ᴀɴᴅ ᴘɪ ᴍᴏᴅᴇ ᴀɴᴅ ᴀʟʟ ɴᴇᴡ ᴜᴘᴄᴏᴍɪɴɢ ғᴇᴀᴛᴜʀᴇs",
    
    "ᴜʟᴛʀᴀ": "ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ᴏғ ɪɴғɪɴɪᴛʏ + ᴅᴇʟᴛᴀ, ᴛʜᴇᴛᴀ & ᴘɪ ᴍᴏᴅᴇ ᴇxᴄʟᴜsɪᴠᴇ + ʙʟᴀsᴛ ᴍᴏᴅᴇ",
}

  PLAN_EMOJIS = {
      "free": "💎",
      "plus": "⭐",
      "pro": "💎",
      "infinity": "♾️",
      "ultra": "🚀",
  }

  REFERRAL_TXT = """🎁 <b>ʀᴇғᴇʀʀᴀʟ ᴘʀᴏɢʀᴀᴍ</b>

💰 <b>ᴀᴋʙᴜᴄᴋs ʙᴀʟᴀɴᴄᴇ:</b> {}
👥 <b>ᴛᴏᴛᴀʟ ʀᴇғᴇʀʀᴀʟs:</b> {}

🔗 <b>ʏᴏᴜʀ ʀᴇғᴇʀʀᴀʟ ʟɪɴᴋ:</b>
{}

<b>ʜᴏᴡ ɪᴛ ᴡᴏʀᴋs:</b>
• sʜᴀʀᴇ ʏᴏᴜʀ ʀᴇғᴇʀʀᴀʟ ʟɪɴᴋ
• ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ ᴊᴏɪɴs, ʏᴏᴜ ɢᴇᴛ <b>+100 ᴀᴋʙᴜᴄᴋs</b>
• ᴛʜᴇʏ ɢᴇᴛ <b>2-ʜᴏᴜʀ ᴘʟᴜs ᴘʟᴀɴ</b> ᴛʀɪᴀʟ

<b>ʀᴇᴅᴇᴇᴍ ʀᴇᴡᴀʀᴅs:</b>
• 1000 ᴀᴋʙᴜᴄᴋs → 30-ᴅᴀʏ ᴘʟᴜs ᴘʟᴀɴ
• 2000 ᴀᴋʙᴜᴄᴋs → 30-ᴅᴀʏ ᴘʀᴏ ᴘʟᴀɴ
• 5000 ᴀᴋʙᴜᴄᴋs → 30-ᴅᴀʏ ɪɴғɪɴɪᴛʏ ᴘʟᴀɴ"""
