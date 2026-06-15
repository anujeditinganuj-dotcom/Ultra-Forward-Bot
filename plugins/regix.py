#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

import os
import sys 
import math
import time
import asyncio 
import logging
from .utils import STS
from database import db 
from .test import CLIENT , start_clone_bot
from . import ftm_engine
from config import Config, temp
from translation import Translation
from pyrogram import Client, filters 
#from pyropatch.utils import unpack_new_file_id
from pyrogram.errors import FloodWait, MessageNotModified, RPCError
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message 

CLIENT = CLIENT()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
TEXT = Translation.TEXT


def _parse_chat_id(chat_id):
    """Convert chat_id to correct type for Pyrogram.
    Private channel IDs are stored as negative ints like -1001234567890.
    Public channels may be stored as '@username' strings.
    This ensures int channels stay int, usernames stay string."""
    if chat_id is None:
        return chat_id
    try:
        return int(chat_id)
    except (ValueError, TypeError):
        return chat_id  # username string like '@channelname'


#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_callback_query(filters.regex(r'^start_public'))
async def pub_(bot, message):
    user = message.from_user.id
    temp.CANCEL[user] = False
    frwd_id = message.data.split("_")[2]
    if temp.lock.get(user) and str(temp.lock.get(user))=="True":
      return await message.answer("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟʟ ᴘʀᴇᴠɪᴏᴜs ᴛᴀsᴋ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.", show_alert=True)
    sts = STS(frwd_id)
    if not sts.verify():
      await message.answer("ʏᴏᴜ ᴀʀᴇ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴍʏ ᴏɴᴇ ᴏғ ᴏʟᴅ ʙᴜᴛᴛᴏɴ.", show_alert=True)
      return await message.message.delete()
    i = sts.get(full=True)
    if i.TO in temp.IS_FRWD_CHAT:
      return await message.answer("ɪɴ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ ᴛᴀsᴋ ɪs ɪɴ ᴘʀᴏɢʀᴇss. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟʟ ᴘʀᴇᴠɪᴏᴜs ᴛᴀsᴋ ɪs ᴄᴏᴍᴘʟᴇᴛᴇᴅ.", show_alert=True)
    m = await msg_edit(message.message, "<i><b>vᴇʀɪғʏɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ.</b></i>")
    _bot, caption, forward_tag, data, protect, button = await sts.get_data(user)
    if not _bot:
      return await msg_edit(m, "<code>ʏᴏᴜ ᴅɪᴅ ɴᴏᴛ ᴀᴅᴅᴇᴅ ᴀɴʏ ʙᴏᴛ ʏᴇᴛ ᴜsᴇ /settings</code>", wait=True)
    try:
      client = await start_clone_bot(CLIENT.client(_bot))
    except Exception as e:  
      return await m.edit(str(e))
    await msg_edit(m, "<b>ᴘʀᴏᴄᴇssɪɴɢ..</b>")
    # ── Source access check ──────────────────────────────────────
    # Try fetching one message to verify access. For private channels
    # this may fail if the client is a plain bot (not admin).
    # In that case we do NOT abort — iter_messages will fail loudly
    # during the actual forward loop if access is truly denied.
    _source_accessible = False
    try:
       await client.get_messages(sts.get("FROM"), sts.get("limit"))
       _source_accessible = True
    except Exception as _e:
       logger.warning(f"Source pre-check failed (may be private channel, will try anyway): {_e}")
       # For private channels the userbot/bot needs to be a member.
       # We attempt iter_messages anyway — if that also fails, the loop
       # catches it and shows the error there.
    # is_bot=True  → bot token (needs admin in private source)
    # is_bot=False → userbot — phone login OR string session (needs membership)
    # Either way: do NOT hard-stop here. Let iter_messages attempt access.
    # _send_by_type will download via the same client that fetches messages,
    # so if the client has access (admin/member), all media types will work.
    if not _source_accessible:
        logger.info(f"Source pre-check failed for {'bot' if _bot.get('is_bot') else 'userbot'} — will attempt iter_messages anyway")
    # ─────────────────────────────────────────────────────────────
    try:
       k = await client.send_message(i.TO, "Testing")
       await k.delete()
    except Exception as _target_err:
       logger.warning(f"Target channel write test failed: {_target_err}")
       await msg_edit(m, f"**ᴘʟᴇᴀsᴇ [ᴜsᴇʀʙᴏᴛ / ʙᴏᴛ](t.me/{_bot['username']}) ᴀᴅᴍɪɴ ɪɴ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ.**", retry_btn(frwd_id), True)
       return await stop(client, user)
    temp.forwardings += 1
    await db.add_frwd(user)
    await send(client, user, "<b>🚥 ғᴏʀᴡᴀʀᴅɪɴɢ sᴛᴀʀᴛᴇᴅ</b>")
    sts.add(time=True)
    sleep = 1 if _bot.get('is_bot', True) else 10  # userbot (phone/session) = 10s, bot = 1s
    await msg_edit(m, "<code>ᴘʀᴏᴄᴇssɪɴɢ ...</code>") 
    temp.IS_FRWD_CHAT.append(i.TO)
    temp.lock[user] = locked = True

    configs = await db.get_configs(user)
    ftm_config = configs.get('ftm', {})
    # Reset auto-numbering counter to its configured start at the beginning of each run
    if ftm_config.get('auto_numbering'):
        ftm_config['auto_number_current'] = ftm_config.get('auto_number_start', 1)
    # forward_tag (raw forward_messages) bypasses caption editing entirely,
    # so disable it whenever any FTM transformation is enabled.
    ftm_active = any([
        ftm_config.get('delta'), ftm_config.get('alpha'), ftm_config.get('gamma'),
        ftm_config.get('theta'), ftm_config.get('watermark'), ftm_config.get('pi'),
        ftm_config.get('replacer'), ftm_config.get('remover'), ftm_config.get('link_remover'),
        ftm_config.get('course_sellers'), ftm_config.get('text_only'),
        ftm_config.get('auto_numbering'), ftm_config.get('bullets'),
    ])
    if ftm_active:
        forward_tag = False

    if locked:
        try:
          MSG = []
          pling=0
          await edit(m, 'ᴘʀᴏɢʀᴇssɪɴɢ', 10, sts)
          logger.info(f"Starting Forwarding Process... From:{sts.get('FROM')} To:{sts.get('TO')} Total:{sts.get('limit')} Skip:{sts.get('skip')}")
          async for message in client.iter_messages(
            chat_id=sts.get('FROM'), 
            limit=int(sts.get('limit')), 
            offset=int(sts.get('skip')) if sts.get('skip') else 0
            ):
                if await is_cancelled(client, user, m, sts):
                   return
                if pling %20 == 0: 
                   await edit(m, 'ᴘʀᴏɢʀᴇssɪɴɢ', 10, sts)
                pling += 1
                sts.add('fetched')
                if message == "DUPLICATE":
                   sts.add('duplicate')
                   continue 
                elif message == "FILTERED":
                   sts.add('filtered')
                   continue 
                if message.empty or message.service:
                   sts.add('deleted')
                   continue
                if should_filter_message(message, data):
                   sts.add('filtered')
                   continue
                if forward_tag:
                   MSG.append(message.id)
                   notcompleted = len(MSG)
                   completed = sts.get('total') - sts.get('fetched')
                   if ( notcompleted >= 100 
                        or completed <= 100): 
                      await forward(client, MSG, m, sts, protect)
                      sts.add('total_files', notcompleted)
                      await asyncio.sleep(10)
                      MSG = []
                else:
                   # FTM Unequify: skip files we've already forwarded before (by file_unique_id)
                   if ftm_config.get('unequify') and message.media:
                      media_obj = getattr(message, message.media.value, None)
                      file_unique_id = getattr(media_obj, 'file_unique_id', None) if media_obj else None
                      if file_unique_id:
                         if await db.is_duplicate_file(user, file_unique_id):
                            sts.add('duplicate')
                            continue
                         await db.mark_file_seen(user, file_unique_id)

                   new_caption = custom_caption(message, caption, ftm_config)

                   if ftm_engine.should_send_text_only(ftm_config):
                      # FTM Text Only Mode: send caption/text as plain text, skip media
                      text_to_send = new_caption or (message.text.html if message.text else None)
                      if text_to_send:
                         try:
                            await client.send_message(
                                chat_id=sts.get('TO'),
                                text=text_to_send,
                                reply_markup=button
                            )
                            sts.add('total_files')
                         except FloodWait as e:
                            await asyncio.sleep(e.value)
                         except Exception as e:
                            logger.warning(f"text_only send failed: {e}")
                            sts.add('deleted')
                      else:
                         sts.add('deleted')
                   else:
                      is_plain_text = bool(message.text and not message.media)
                      if is_plain_text and new_caption == (message.text.html if message.text else None):
                         # No FTM transform changed anything -> use normal copy_message path
                         new_caption = None
                         is_plain_text = False
                      details = {"msg_id": message.id, "media": media(message), "caption": new_caption, 'button': button, "protect": protect, "is_text": is_plain_text, "raw_msg": message}
                      await copy(client, details, m, sts)
                      sts.add('total_files')
                      if ftm_config.get('blast') and ftm_config.get('blast_targets'):
                         await blast_copy(client, details, m, sts, ftm_config)

                   if ftm_config.get('auto_numbering'):
                      ftm_config['auto_number_current'] = ftm_config.get('auto_number_current', 1) + 1

                   await asyncio.sleep(sleep) 
        except Exception as e:
            await msg_edit(m, f'<b>ERROR:</b>\n<code>{e}</code>', wait=True)
            if sts.TO in temp.IS_FRWD_CHAT:
                temp.IS_FRWD_CHAT.remove(sts.TO)
            return await stop(client, user)
        if sts.TO in temp.IS_FRWD_CHAT:
            temp.IS_FRWD_CHAT.remove(sts.TO)
        if ftm_config.get('auto_numbering'):
            await db.update_ftm_config(user, 'auto_number_current', ftm_config.get('auto_number_current', 1))
        await send(client, user, "<b>🎉 ғᴏʀᴡᴀᴅɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</b>")
        await edit(m, 'ᴄᴏᴍᴘʟᴇᴛᴇᴅ', "ᴄᴏᴍᴘʟᴇᴛᴇᴅ", sts) 
        await stop(client, user)
        
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def _send_by_type(bot, raw_msg, chat_id, caption, button, protect):
    """Download file from raw_msg (via userbot client that fetched it) and re-upload using bot.
    Supports: photo, video, document, audio, voice, animation, sticker, video_note."""
    tmp_path = None
    try:
        # Download using the same client that fetched the message (userbot can access private)
        tmp_path = await raw_msg._client.download_media(raw_msg)
        if tmp_path is None:
            return False

        kwargs = dict(
            chat_id=chat_id,
            caption=caption or "",
            reply_markup=button,
            protect_content=protect,
        )

        mtype = raw_msg.media.value if raw_msg.media else None

        if mtype == "photo":
            await bot.send_photo(photo=tmp_path, **kwargs)
        elif mtype == "video":
            thumb = None
            if raw_msg.video and raw_msg.video.thumbs:
                try:
                    thumb = await raw_msg._client.download_media(raw_msg.video.thumbs[0].file_id)
                except Exception:
                    pass
            await bot.send_video(
                video=tmp_path,
                duration=raw_msg.video.duration if raw_msg.video else 0,
                width=raw_msg.video.width if raw_msg.video else 0,
                height=raw_msg.video.height if raw_msg.video else 0,
                thumb=thumb,
                supports_streaming=True,
                **kwargs,
            )
            if thumb and os.path.exists(thumb):
                os.remove(thumb)
        elif mtype == "document":
            thumb = None
            if raw_msg.document and raw_msg.document.thumbs:
                try:
                    thumb = await raw_msg._client.download_media(raw_msg.document.thumbs[0].file_id)
                except Exception:
                    pass
            await bot.send_document(
                document=tmp_path,
                file_name=raw_msg.document.file_name if raw_msg.document else None,
                thumb=thumb,
                **kwargs,
            )
            if thumb and os.path.exists(thumb):
                os.remove(thumb)
        elif mtype == "audio":
            await bot.send_audio(
                audio=tmp_path,
                duration=raw_msg.audio.duration if raw_msg.audio else 0,
                performer=raw_msg.audio.performer if raw_msg.audio else None,
                title=raw_msg.audio.title if raw_msg.audio else None,
                **kwargs,
            )
        elif mtype == "voice":
            await bot.send_voice(voice=tmp_path, **kwargs)
        elif mtype == "animation":
            await bot.send_animation(animation=tmp_path, **kwargs)
        elif mtype == "sticker":
            # Stickers don't support caption
            await bot.send_sticker(chat_id=chat_id, sticker=tmp_path, protect_content=protect)
        elif mtype == "video_note":
            await bot.send_video_note(video_note=tmp_path, chat_id=chat_id, protect_content=protect)
        else:
            # Fallback: send as document
            await bot.send_document(document=tmp_path, **kwargs)

        return True
    except Exception as e:
        logger.warning(f"_send_by_type failed ({mtype}): {e}")
        return False
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass


async def copy(bot, msg, m, sts, chat_id=None):
   chat_id = chat_id or sts.get('TO')
   caption  = msg.get("caption")
   button   = msg.get('button')
   protect  = msg.get("protect")
   raw_msg  = msg.get("raw_msg")   # original Message object fetched by client
   from_id  = _parse_chat_id(sts.get('FROM'))

   try:
     # ── Plain text (FTM-transformed or normal) ────────────────
     if not msg.get("media") and msg.get("is_text") and caption is not None:
        await bot.send_message(
              chat_id=chat_id,
              text=caption,
              reply_markup=button)
        return

     sent = False

     # ── Fast path: copy_message (works when bot/userbot has access) ──
     # copy_message works for:
     #   - Public channels (bot can always read public)
     #   - Private channels where bot is admin / userbot is member
     # We always try this first — it's zero-download and preserves quality.
     try:
        await bot.copy_message(
              chat_id=chat_id,
              from_chat_id=from_id,
              message_id=msg.get("msg_id"),
              caption=caption,
              reply_markup=button,
              protect_content=protect)
        sent = True
     except Exception as fast_err:
        logger.info(f"copy_message failed (msg={msg.get('msg_id')}): {fast_err} — trying download-reupload")

     # ── Fallback: download via client that fetched msg → re-upload via bot ──
     # Handles restricted/forwarding-disabled content from any channel type.
     if not sent and raw_msg is not None and raw_msg.media:
        sent = await _send_by_type(bot, raw_msg, chat_id, caption, button, protect)

     # ── Last resort for text-only messages ───────────────────
     if not sent and raw_msg is not None and raw_msg.text:
        try:
           await bot.send_message(
                 chat_id=chat_id,
                 text=caption or raw_msg.text.html,
                 reply_markup=button)
           sent = True
        except Exception as e:
           logger.warning(f"send_message fallback failed: {e}")

     if not sent:
        logger.warning(f"All methods failed for msg_id={msg.get('msg_id')}")
        if chat_id == sts.get('TO'):
           sts.add('deleted')

   except FloodWait as e:
     await edit(m, 'ᴘʀᴏɢʀᴇssɪɴɢ', e.value, sts)
     await asyncio.sleep(e.value)
     await edit(m, 'ᴘʀᴏɢʀᴇssɪɴɢ', 10, sts)
     await copy(bot, msg, m, sts, chat_id)
   except Exception as e:
     logger.warning(f"copy() unexpected error: {e}")
     if chat_id == sts.get('TO'):
        sts.add('deleted')

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def blast_copy(bot, msg, m, sts, ftm_config):
   """FTM Blast Mode: also send this message to each configured blast target chat."""
   targets = ftm_config.get('blast_targets') or []
   for target_chat in targets:
      if str(target_chat) == str(sts.get('TO')):
         continue
      await copy(bot, msg, m, sts, chat_id=target_chat)
      await asyncio.sleep(1)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def forward(bot, msg, m, sts, protect):
   try:                             
     await bot.forward_messages(
           chat_id=sts.get('TO'),
           from_chat_id=_parse_chat_id(sts.get('FROM')), 
           protect_content=protect,
           message_ids=msg)
   except FloodWait as e:
     await edit(m, 'ᴘʀᴏɢʀᴇssɪɴɢ', e.value, sts)
     await asyncio.sleep(e.value)
     await edit(m, 'ᴘʀᴏɢʀᴇssɪɴɢ', 10, sts)
     await forward(bot, msg, m, sts, protect)

PROGRESS = """
📈 ᴘᴇʀᴄᴇɴᴛᴀɢᴇ : {0} %

⭕ ғᴇᴛᴄʜᴇᴅ : {1}

⚙️ ғᴏʀᴡᴀʀᴅᴇᴅ : {2}

🗞️ ʀᴇᴍᴀɴɪɴɢ : {3}

♻️ sᴛᴀᴛᴜs : {4}

⏳️ ᴇᴛᴀ : {5}
"""

async def msg_edit(msg, text, button=None, wait=None):
    try:
        return await msg.edit(text, reply_markup=button)
    except MessageNotModified:
        pass 
    except FloodWait as e:
        if wait:
           await asyncio.sleep(e.value)
           return await msg_edit(msg, text, button, wait)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def edit(msg, title, status, sts):
   i = sts.get(full=True)
   status = 'ғᴏʀᴡᴀʀᴅɪɴɢ' if status == 10 else f"sʟᴇᴇᴘɪɴɢ {status} s" if str(status).isnumeric() else status
   percentage = "{:.0f}".format(float(i.fetched)*100/float(i.total))

   now = time.time()
   diff = int(now - i.start)
   speed = sts.divide(i.fetched, diff)
   elapsed_time = round(diff) * 1000
   time_to_completion = round(sts.divide(i.total - i.fetched, int(speed))) * 1000
   estimated_total_time = elapsed_time + time_to_completion  
   
   progress = "▰{0}{1}".format(
       ''.join(["▰" for i in range(math.floor(int(percentage) / 10))]),
       ''.join(["▱" for i in range(10 - math.floor(int(percentage) / 10))]))
   button =  [[InlineKeyboardButton(progress, f'fwrdstatus#{status}#{estimated_total_time}#{percentage}#{i.id}')]]
   estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
   estimated_total_time = estimated_total_time if estimated_total_time != '' else '0 s'

   text = TEXT.format(i.total, i.fetched, i.total_files, i.duplicate, i.deleted, i.skip, i.filtered, status, percentage, title)
   if status in ["ᴄᴀɴᴄᴇʟʟᴇᴅ", "ᴄᴏᴍᴘʟᴇᴛᴇᴅ"]:
      button.append(
         [InlineKeyboardButton('💟sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ💟', url='https://t.me/anujeditbyak')])
      button.append(
         [InlineKeyboardButton('💠ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ💠', url='https://t.me/anujeditbyak')]
         )
   else:
      button.append([InlineKeyboardButton('• ᴄᴀɴᴄᴇʟ', 'terminate_frwd')])
   await msg_edit(msg, text, InlineKeyboardMarkup(button))

async def is_cancelled(client, user, msg, sts):
   if temp.CANCEL.get(user)==True:
      if sts.TO in temp.IS_FRWD_CHAT:
          temp.IS_FRWD_CHAT.remove(sts.TO)
      await edit(msg, "ᴄᴀɴᴄᴇʟʟᴇᴅ", "ᴄᴏᴍᴘʟᴇᴛᴇᴅ", sts)
      await send(client, user, "<b>❌ ғᴏʀᴡᴀʀᴅɪɴɢ ᴄᴀɴᴄᴇʟʟᴇᴅ</b>")
      await stop(client, user)
      return True 
   return False 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def stop(client, user):
   try:
     await client.stop()
   except Exception:
     pass 
   await db.rmve_frwd(user)
   temp.forwardings -= 1
   temp.lock[user] = False 

async def send(bot, user, text):
   try:
      await bot.send_message(user, text=text)
   except Exception:
      pass 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 


def custom_caption(msg, caption, ftm_config=None):
  text = None
  if msg.media:
    if (msg.video or msg.document or msg.audio or msg.photo):
      media = getattr(msg, msg.media.value, None)
      if media:
        file_name = getattr(media, 'file_name', '')
        file_size = getattr(media, 'file_size', '')
        fcaption = getattr(msg, 'caption', '')
        if fcaption:
          fcaption = fcaption.html
        if caption:
          text = caption.format(filename=file_name, size=get_size(file_size), caption=fcaption)
        else:
          text = fcaption
  elif msg.text and ftm_config:
    # Plain text message: only build a transformed text if FTM transforms are active,
    # so copy_message's caption param carries the transformed text.
    text = msg.text.html
  if ftm_config:
     text = ftm_engine.apply_ftm_transformations(text, ftm_config)
  return text

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def get_size(size):
  units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
  size = float(size)
  i = 0
  while size >= 1024.0 and i < len(units):
     i += 1
     size /= 1024.0
  return "%.2f %s" % (size, units[i]) 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# Maps a message to the media-type key used in configs['filters']
MEDIA_TYPE_MAP = {
   "poll": "poll",
   "audio": "audio",
   "voice": "voice",
   "video": "video",
   "photo": "photo",
   "document": "document",
   "animation": "animation",
   "sticker": "sticker",
}

def message_type(msg):
   """Returns the filter-key for this message's content type, or 'text' for plain text."""
   if msg.media:
      key = msg.media.value
      return MEDIA_TYPE_MAP.get(key, key)
   if msg.text:
      return "text"
   return None

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def should_filter_message(msg, data):
   """
   Checks a message against the user's configured filters (media type filters,
   extensions, keywords, file size limit, secure/protected-content messages).

   `data` is the dict built by STS.get_data(): keys 'filters', 'extensions',
   'keywords', 'media_size'.

   Returns True if the message should be SKIPPED (filtered out).
   """
   filters_list = data.get('filters') or []

   # --- Media type filter (poll/text/audio/voice/video/photo/document/animation/sticker) ---
   mtype = message_type(msg)
   if mtype and mtype in filters_list:
      return True

   # --- Secure / protected content messages ---
   if getattr(msg, 'has_protected_content', False):
      return True

   media_obj = None
   if msg.media:
      media_obj = getattr(msg, msg.media.value, None)

   # --- Extension filter (skip files with these extensions) ---
   extensions = data.get('extensions')
   if extensions and media_obj:
      file_name = getattr(media_obj, 'file_name', '') or ''
      if '.' in file_name:
         ext = file_name.rsplit('.', 1)[-1].lower()
         if any(ext == e.lstrip('.').lower() for e in extensions):
            return True

   # --- Keyword filter (only forward files whose name contains a keyword) ---
   keywords = data.get('keywords')
   if keywords and media_obj:
      file_name = (getattr(media_obj, 'file_name', '') or '').lower()
      if not any(kw.lower() in file_name for kw in keywords):
         return True

   # --- File size limit ---
   media_size = data.get('media_size')
   if media_size and media_obj:
      limit_mb, direction = media_size
      file_size_mb = (getattr(media_obj, 'file_size', 0) or 0) / (1024 * 1024)
      if direction is True and file_size_mb < limit_mb:
         # "more than" limit_mb required
         return True
      if direction is False and file_size_mb > limit_mb:
         # "less than" limit_mb required
         return True

   return False

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def media(msg):
  if msg.media:
     media = getattr(msg, msg.media.value, None)
     if media:
        return getattr(media, 'file_id', None)
  return None 
  
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

def retry_btn(id):
    return InlineKeyboardMarkup([[InlineKeyboardButton('♻️ ʀᴇᴛʀʏ ♻️', f"start_public_{id}")]])

@Client.on_callback_query(filters.regex(r'^terminate_frwd$'))
async def terminate_frwding(bot, m):
    user_id = m.from_user.id 
    temp.lock[user_id] = False
    temp.CANCEL[user_id] = True 
    await m.answer("ғᴏʀᴡᴀʀᴅɪɴɢ ᴄᴀɴᴄᴇʟʟᴇᴅ !", show_alert=True)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_callback_query(filters.regex(r'^fwrdstatus'))
async def status_msg(bot, msg):
    _, status, est_time, percentage, frwd_id = msg.data.split("#")
    sts = STS(frwd_id)
    if not sts.verify():
       fetched = forwarded = remaining = skipped = 0
    else:
       total = sts.get('total')
       skipped = sts.get('skip')
       fetched, forwarded = sts.get('fetched'), sts.get('total_files')
       remaining = total - forwarded - skipped
    est_time = TimeFormatter(milliseconds=est_time)
    est_time = est_time if (est_time != '' or status not in ['completed', 'cancelled']) else '0 s'
    return await msg.answer(PROGRESS.format(percentage, fetched, forwarded, remaining, status, est_time), show_alert=True)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_message(filters.command(["stop", "cleartask"]))
async def stop_forwarding(bot, message):
    user_id = message.from_user.id
    if temp.lock.get(user_id):
        temp.lock[user_id] = False
        temp.CANCEL[user_id] = True
        await message.reply("🛑 ғᴏʀᴡᴀʀᴅɪɴɢ ᴄᴀɴᴄᴇʟʟᴇᴅ !", quote=True)
        # Optionally, notify the user in a more detailed way.
    else:
        await message.reply("❌ ɴᴏ ᴏɴɢᴏɪɴɢ ғᴏʀᴡᴀʀᴅɪɴɢ ᴘʀᴏᴄᴇss ᴛᴏ ᴄᴀɴᴄᴇʟ.", quote=True)

@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
    
 #Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
