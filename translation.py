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

<u>**📚 Available Commands:**</u>

<b>⏣ __/start - Check I'm alive__ 
⏣ __/forward - Forward messages__
⏣ __/unequify - Delete duplicate messages in channels__
⏣ __/settings - Configure your settings__
⏣ __/reset - Reset your settings__
⏣ __/donate - Donate to developer__
⏣ __/stop - Cancel your ongoing forwarding__</b>

<b><u>💢 Features:</b></u>
<b>► __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission__
► __Forward message from private channel to your channel by using userbot(user must be member in there)__
► __Custom caption__
► __Custom button__
► __Support restricted chats__
► __Skip duplicate messages__
► __Filter type of messages__
► __Skip messages based on extensions & keywords & size__</b>
"""
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
<b>► __add a bot or userbot__
► __add atleast one to channel__ `(your bot/userbot must be admin in there)`
► __You can add chats or bots by using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
► __Then use /forward to forward messages__</b>"""

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
      "free": "Only configuration options available",
      "plus": "Only forwarding, no FTM Manager feature",
      "pro": "Gamma mode, watermark, text only + all features of Plus plan",
      "infinity": "All features of Pro plan & all features of bot including FTM Manager except Delta, Theta, and Pi mode and all new upcoming features",
      "ultra": "All features of Infinity + Delta, Theta & Pi mode exclusive + Blast Mode",
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
