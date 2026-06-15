#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

import re
import asyncio
import logging
from database import db
from . import ftm_engine
from .test import CLIENT, start_clone_bot
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

CLIENT_FACTORY = CLIENT()
LINK_REGEX = re.compile(r"(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)?")

GAMMA_POLL_INTERVAL = 60  # seconds between auto-forward checks
GAMMA_BATCH_LIMIT = 20    # max messages forwarded per cycle per user

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def parse_chat_ref(text):
    """Parse a chat reference: t.me link, @username, or numeric chat id."""
    text = text.strip().replace("?single", "")
    match = LINK_REGEX.match(text)
    if match:
        chat = match.group(4)
        if chat.isnumeric():
            return int("-100" + chat)
        return chat
    if text.startswith("@"):
        return text
    try:
        return int(text)
    except ValueError:
        return text

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_message(filters.private & filters.command(['gamma']))
async def gamma_setup_cmd(client, message):
    user_id = message.from_user.id

    if not await db.has_feature(user_id, "gamma"):
        return await message.reply_text(
            "<b>🔒 ꜰᴛᴍ ɢᴀᴍᴍᴀ ᴍᴏᴅᴇ (ᴀᴜᴛᴏ-ғᴏʀᴡᴀʀᴅ) ʀᴇQᴜɪʀᴇs ᴩʀᴏ ᴩʟᴀɴ ᴏʀ ᴀʙᴏᴠᴇ.</b>\n\nᴜsᴇ /plans ᴛᴏ ᴜᴩɢʀᴀᴅᴇ."
        )

    _bot = await db.get_bot(user_id)
    if not _bot:
        return await message.reply_text("<b>❌ ᴩʟᴇᴀsᴇ ᴀᴅᴅ ᴀ ʙᴏᴛ/ᴜsᴇʀʙᴏᴛ ғɪʀsᴛ ᴜsɪɴɢ /settings.</b>")

    from_msg = await client.ask(
        user_id,
        "📥 <b>sᴇɴᴅ sᴏᴜʀᴄᴇ ᴄʜᴀɴɴᴇʟ</b> (ᴜsᴇʀɴᴀᴍᴇ, ᴄʜᴀᴛ ɪᴅ, ᴏʀ ᴛ.ᴍᴇ ʟɪɴᴋ)\n\n/cancel - ᴄᴀɴᴄᴇʟ"
    )
    if from_msg.text and from_msg.text.strip() == "/cancel":
        return await from_msg.reply_text("<b>ᴄᴀɴᴄᴇʟʟᴇᴅ.</b>")
    from_chat = parse_chat_ref(from_msg.text)

    to_msg = await client.ask(
        user_id,
        "📤 <b>sᴇɴᴅ ᴅᴇsᴛɪɴᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ</b> (ᴜsᴇʀɴᴀᴍᴇ, ᴄʜᴀᴛ ɪᴅ, ᴏʀ ᴛ.ᴍᴇ ʟɪɴᴋ)\n\n/cancel - ᴄᴀɴᴄᴇʟ"
    )
    if to_msg.text and to_msg.text.strip() == "/cancel":
        return await to_msg.reply_text("<b>ᴄᴀɴᴄᴇʟʟᴇᴅ.</b>")
    to_chat = parse_chat_ref(to_msg.text)

    sts = await to_msg.reply_text("<code>ᴛᴇsᴛɪɴɢ ᴀᴄᴄᴇss...</code>")
    try:
        client_bot = await start_clone_bot(CLIENT_FACTORY.client(_bot))
    except Exception as e:
        return await sts.edit(f"<b>❌ ᴄᴏᴜʟᴅɴ'ᴛ sᴛᴀʀᴛ ᴄʟᴏɴᴇ ʙᴏᴛ:</b>\n<code>{e}</code>")

    try:
        last_msg = None
        async for msg in client_bot.get_chat_history(from_chat, limit=1):
            last_msg = msg
        await client_bot.get_chat(to_chat)
    except Exception as e:
        await client_bot.stop()
        return await sts.edit(
            f"<b>❌ ᴀᴄᴄᴇss ᴄʜᴇᴄᴋ ғᴀɪʟᴇᴅ:</b>\n<code>{e}</code>\n\n"
            "ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ ʙᴏᴛ/ᴜsᴇʀʙᴏᴛ ɪs ᴀ ᴍᴇᴍʙᴇʀ/ᴀᴅᴍɪɴ ɪɴ ʙᴏᴛʜ ᴄʜᴀᴛs."
        )

    last_msg_id = last_msg.id if last_msg else 0
    await client_bot.stop()

    configs = await db.get_configs(user_id)
    configs['ftm']['gamma'] = True
    configs['ftm']['gamma_from'] = from_chat
    configs['ftm']['gamma_to'] = to_chat
    configs['ftm']['gamma_last_msg_id'] = last_msg_id
    await db.update_configs(user_id, configs)

    await sts.edit(
        f"<b>✅ ꜰᴛᴍ ɢᴀᴍᴍᴀ ᴍᴏᴅᴇ ᴇɴᴀʙʟᴇᴅ!</b>\n\n"
        f"📥 ꜰʀᴏᴍ: <code>{from_chat}</code>\n"
        f"📤 ᴛᴏ: <code>{to_chat}</code>\n\n"
        f"ɴᴇᴡ ᴍᴇssᴀɢᴇs ᴩᴏsᴛᴇᴅ ɪɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ғᴏʀᴡᴀʀᴅᴇᴅ ᴇᴠᴇʀʏ ~{GAMMA_POLL_INTERVAL}s.\n\n"
        f"ᴜsᴇ /gammaoff ᴛᴏ ᴅɪsᴀʙʟᴇ."
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_message(filters.private & filters.command(['gammaoff']))
async def gamma_off_cmd(client, message):
    user_id = message.from_user.id
    configs = await db.get_configs(user_id)
    if not configs['ftm'].get('gamma'):
        return await message.reply_text("<b>ꜰᴛᴍ ɢᴀᴍᴍᴀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴏғғ.</b>")
    configs['ftm']['gamma'] = False
    await db.update_configs(user_id, configs)
    await message.reply_text("<b>✅ ꜰᴛᴍ ɢᴀᴍᴍᴀ ᴍᴏᴅᴇ ᴅɪsᴀʙʟᴇᴅ.</b>")

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def gamma_poll_loop(app):
    """Background task: periodically checks gamma-enabled users for new messages
    in their source channel and auto-forwards them (with FTM transformations applied)
    to the destination channel."""
    await asyncio.sleep(15)  # let the bot fully start first
    while True:
        try:
            users = await db.get_gamma_users()
            for user in users:
                user_id = user['id']
                try:
                    await _process_gamma_user(user_id)
                except Exception as e:
                    logging.error(f"Gamma mode error for user {user_id}: {e}")
        except Exception as e:
            logging.error(f"Gamma poll loop error: {e}")
        await asyncio.sleep(GAMMA_POLL_INTERVAL)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def _process_gamma_user(user_id):
    if not await db.has_feature(user_id, "gamma"):
        return

    configs = await db.get_configs(user_id)
    ftm_config = configs.get('ftm', {})
    from_chat = ftm_config.get('gamma_from')
    to_chat = ftm_config.get('gamma_to')
    last_msg_id = ftm_config.get('gamma_last_msg_id', 0)

    if not from_chat or not to_chat:
        return

    _bot = await db.get_bot(user_id)
    if not _bot:
        return

    try:
        client_bot = await start_clone_bot(CLIENT_FACTORY.client(_bot))
    except Exception as e:
        logging.error(f"Gamma: couldn't start client for {user_id}: {e}")
        return

    try:
        new_messages = []
        async for msg in client_bot.get_chat_history(from_chat, limit=GAMMA_BATCH_LIMIT):
            if msg.id <= last_msg_id:
                break
            if msg.empty or msg.service:
                continue
            new_messages.append(msg)

        new_messages.reverse()  # oldest first

        max_id_seen = last_msg_id
        for msg in new_messages:
            try:
                await _gamma_forward_one(client_bot, msg, to_chat, ftm_config, from_chat)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await _gamma_forward_one(client_bot, msg, to_chat, ftm_config, from_chat)
            except Exception as e:
                logging.error(f"Gamma forward error for user {user_id}, msg {msg.id}: {e}")
            max_id_seen = max(max_id_seen, msg.id)
            await asyncio.sleep(1)

        if max_id_seen != last_msg_id:
            await db.update_ftm_config(user_id, 'gamma_last_msg_id', max_id_seen)

    finally:
        await client_bot.stop()

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def _gamma_forward_one(client_bot, msg, to_chat, ftm_config, from_chat):
    """Apply FTM transformations and send a single message to the gamma destination."""
    caption = None
    if msg.caption:
        caption = msg.caption.html
    elif msg.text:
        caption = msg.text.html

    transformed = ftm_engine.apply_ftm_transformations(caption, ftm_config)

    if ftm_engine.should_send_text_only(ftm_config):
        if transformed:
            await client_bot.send_message(chat_id=to_chat, text=transformed)
        return

    if msg.media:
        await client_bot.copy_message(
            chat_id=to_chat,
            from_chat_id=from_chat,
            message_id=msg.id,
            caption=transformed
        )
    elif msg.text:
        await client_bot.send_message(chat_id=to_chat, text=transformed)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
