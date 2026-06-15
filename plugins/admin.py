#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

import asyncio
import datetime
from database import db, PLANS
from config import Config
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def is_authorized(user_id):
    return await db.is_admin(user_id)

async def resolve_user(client, identifier):
    """Resolve a user by mention/username/id/reply, returns (id, name) or (None, None)."""
    identifier = identifier.strip()
    if identifier.startswith("@"):
        try:
            chat = await client.get_users(identifier)
            return chat.id, chat.mention
        except Exception:
            return None, None
    try:
        uid = int(identifier)
        user = await db.get_user(uid)
        name = user.get('name', str(uid)) if user else str(uid)
        return uid, name
    except ValueError:
        return None, None

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /add_premium ============

@Client.on_message(filters.private & filters.command(['add_premium']))
async def add_premium_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    args = message.text.split()
    target = None

    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
        rest = args[1:]
    else:
        if len(args) < 2:
            return await message.reply_text(
                "<b>ᴜsᴀɢᴇ:</b>\n"
                "<code>/add_premium user_id plan days</code>\n\n"
                "<b>ᴇxᴀᴍᴘʟᴇ:</b>\n"
                "<code>/add_premium 123456789 ultra 30</code>\n\n"
                f"<b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs:</b> {', '.join(PLANS.keys())}"
            )
        uid, name = await resolve_user(client, args[1])
        if uid is None:
            return await message.reply_text("<b>❌ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ.</b>")
        target = uid
        rest = args[2:]

    plan_key = rest[0].lower() if len(rest) >= 1 else "ultra"
    days = int(rest[1]) if len(rest) >= 2 else 30

    if plan_key not in PLANS or plan_key == "free":
        return await message.reply_text(
            f"<b>❌ ɪɴᴠᴀʟɪᴅ ᴘʟᴀɴ.</b> ᴀᴠᴀɪʟᴀʙʟᴇ: {', '.join([p for p in PLANS if p != 'free'])}"
        )

    if not await db.is_user_exist(target):
        return await message.reply_text("<b>❌ ᴛʜɪs ᴜsᴇʀ ʜᴀs ɴᴇᴠᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.</b>")

    expiry = await db.add_premium_time(target, plan_key, days)

    await message.reply_text(
        f"<b>✅ ᴘʀᴇᴍɪᴜᴍ ᴀᴅᴅᴇᴅ!</b>\n\n"
        f"👤 ᴜsᴇʀ: <code>{target}</code>\n"
        f"💎 ᴘʟᴀɴ: {PLANS[plan_key]['name']}\n"
        f"📅 ᴅᴀʏs: {days}\n"
        f"⏰ ᴇxᴘɪʀʏ: {expiry.strftime('%d-%m-%Y %H:%M:%S UTC')}"
    )
    try:
        await client.send_message(
            target,
            f"<b>🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!</b>\n\n"
            f"ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ <b>{PLANS[plan_key]['name']}</b> ᴘʟᴀɴ ғᴏʀ {days} ᴅᴀʏs!\n"
            f"⏰ ᴇxᴘɪʀᴇs: {expiry.strftime('%d-%m-%Y %H:%M:%S UTC')}\n\n"
            f"ᴜsᴇ /myplan ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ."
        )
    except Exception:
        pass

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /remove_premium ============

@Client.on_message(filters.private & filters.command(['remove_premium']))
async def remove_premium_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    args = message.text.split()
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
    else:
        if len(args) < 2:
            return await message.reply_text(
                "<b>ᴜsᴀɢᴇ:</b>\n<code>/remove_premium user_id</code>"
            )
        uid, _ = await resolve_user(client, args[1])
        if uid is None:
            return await message.reply_text("<b>❌ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ.</b>")
        target = uid

    if not await db.is_user_exist(target):
        return await message.reply_text("<b>❌ ᴛʜɪs ᴜsᴇʀ ʜᴀs ɴᴇᴠᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.</b>")

    await db.remove_premium(target)
    await message.reply_text(f"<b>✅ ᴘʀᴇᴍɪᴜᴍ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ</b> <code>{target}</code>")
    try:
        await client.send_message(
            target,
            "<b>⚠️ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ᴀᴅᴍɪɴ.</b>\n\nʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴏɴ ᴛʜᴇ ғʀᴇᴇ ᴘʟᴀɴ."
        )
    except Exception:
        pass

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /users ============

@Client.on_message(filters.private & filters.command(['users']))
async def users_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    total, bots = await db.total_users_bots_count()
    premium_count = await db.get_premium_count()

    await message.reply_text(
        f"<b>👥 ᴜsᴇʀ sᴛᴀᴛɪsᴛɪᴄs</b>\n\n"
        f"📊 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{total}</code>\n"
        f"💎 ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: <code>{premium_count}</code>\n"
        f"🆓 ғʀᴇᴇ ᴜsᴇʀs: <code>{total - premium_count}</code>\n"
        f"🤖 ᴄᴏɴɴᴇᴄᴛᴇᴅ ʙᴏᴛs: <code>{bots}</code>"
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /pusers ============

@Client.on_message(filters.private & filters.command(['pusers']))
async def pusers_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    premium_users = await db.get_premium_users()
    if not premium_users:
        return await message.reply_text("<b>ɴᴏ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs ʏᴇᴛ.</b>")

    lines = []
    for u in premium_users:
        plan_key, expiry = await db.get_plan(u['id'])
        plan_name = PLANS.get(plan_key, PLANS['free'])['name']
        expiry_txt = expiry.strftime('%d-%m-%Y') if expiry else "Permanent"
        lines.append(f"• <code>{u['id']}</code> — {plan_name} (ᴜɴᴛɪʟ {expiry_txt})")

    text = "<b>💎 ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs:</b>\n\n" + "\n".join(lines)
    if len(text) > 4000:
        text = text[:4000] + "\n\n<i>...truncated</i>"
    await message.reply_text(text)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /makeadmin ============

@Client.on_message(filters.private & filters.command(['makeadmin']) & filters.user(Config.BOT_OWNER_ID))
async def makeadmin_cmd(client, message):
    args = message.text.split()
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
    else:
        if len(args) < 2:
            return await message.reply_text("<b>ᴜsᴀɢᴇ:</b>\n<code>/makeadmin user_id</code>")
        uid, _ = await resolve_user(client, args[1])
        if uid is None:
            return await message.reply_text("<b>❌ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ.</b>")
        target = uid

    if not await db.is_user_exist(target):
        return await message.reply_text("<b>❌ ᴛʜɪs ᴜsᴇʀ ʜᴀs ɴᴇᴠᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.</b>")

    await db.add_admin(target)
    await message.reply_text(f"<b>✅</b> <code>{target}</code> <b>ɪs ɴᴏᴡ ᴀɴ ᴀᴅᴍɪɴ.</b>")
    try:
        await client.send_message(target, "<b>🎉 ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴍᴀᴅᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏғ ᴛʜɪs ʙᴏᴛ!</b>")
    except Exception:
        pass

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /removeadmin ============

@Client.on_message(filters.private & filters.command(['removeadmin']) & filters.user(Config.BOT_OWNER_ID))
async def removeadmin_cmd(client, message):
    args = message.text.split()
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
    else:
        if len(args) < 2:
            return await message.reply_text("<b>ᴜsᴀɢᴇ:</b>\n<code>/removeadmin user_id</code>")
        uid, _ = await resolve_user(client, args[1])
        if uid is None:
            return await message.reply_text("<b>❌ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ.</b>")
        target = uid

    await db.remove_admin(target)
    await message.reply_text(f"<b>✅</b> <code>{target}</code> <b>ɪs ɴᴏ ʟᴏɴɢᴇʀ ᴀɴ ᴀᴅᴍɪɴ.</b>")

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /listadmins ============

@Client.on_message(filters.private & filters.command(['listadmins']))
async def listadmins_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    admins = await db.get_admins()
    lines = [f"• <code>{oid}</code> (ᴏᴡɴᴇʀ)" for oid in Config.BOT_OWNER_ID]
    for a in admins:
        lines.append(f"• <code>{a['id']}</code> — {a.get('name', '')}")

    await message.reply_text("<b>👮 ʙᴏᴛ ᴀᴅᴍɪɴs:</b>\n\n" + "\n".join(lines))

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /userstats ============

@Client.on_message(filters.private & filters.command(['userstats']))
async def userstats_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    total, bots = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    premium_count = await db.get_premium_count()

    plan_counts = {}
    for key in PLANS:
        plan_counts[key] = 0
    premium_users = await db.get_premium_users()
    for u in premium_users:
        plan_key, _ = await db.get_plan(u['id'])
        plan_counts[plan_key] = plan_counts.get(plan_key, 0) + 1
    plan_counts['free'] = total - premium_count

    plan_lines = "\n".join(
        [f"• {PLANS[k]['name']}: <code>{v}</code>" for k, v in plan_counts.items()]
    )

    await message.reply_text(
        f"<b>📊 ᴜsᴇʀ sᴛᴀᴛs</b>\n\n"
        f"👥 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{total}</code>\n"
        f"🤖 ᴄᴏɴɴᴇᴄᴛᴇᴅ ʙᴏᴛs: <code>{bots}</code>\n"
        f"🏷 ᴄʜᴀɴɴᴇʟs: <code>{total_channels}</code>\n\n"
        f"<b>ᴘʟᴀɴ ʙʀᴇᴀᴋᴅᴏᴡɴ:</b>\n{plan_lines}"
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /pnotify ============

@Client.on_message(filters.private & filters.command(['pnotify']) & filters.reply)
async def pnotify_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    premium_users = await db.get_premium_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text("<b>📣 ɴᴏᴛɪғʏɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs...</b>")

    success, failed = 0, 0
    for u in premium_users:
        try:
            await b_msg.copy(chat_id=u['id'])
            success += 1
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                await b_msg.copy(chat_id=u['id'])
                success += 1
            except Exception:
                failed += 1
        except Exception:
            failed += 1

    await sts.edit(
        f"<b>✅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ sᴇɴᴛ!</b>\n\n"
        f"ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: <code>{len(premium_users)}</code>\n"
        f"sᴜᴄᴄᴇss: <code>{success}</code>\n"
        f"ғᴀɪʟᴇᴅ: <code>{failed}</code>"
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /add_bal (FTMBucks) ============

@Client.on_message(filters.private & filters.command(['add_bal']))
async def add_bal_cmd(client, message):
    if not await is_authorized(message.from_user.id):
        return await message.reply_text("<b>⛔ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴅᴍɪɴ ᴏɴʟʏ.</b>")

    args = message.text.split()
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
        rest = args[1:]
    else:
        if len(args) < 3:
            return await message.reply_text(
                "<b>ᴜsᴀɢᴇ:</b>\n<code>/add_bal user_id amount</code>"
            )
        uid, _ = await resolve_user(client, args[1])
        if uid is None:
            return await message.reply_text("<b>❌ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ.</b>")
        target = uid
        rest = args[2:]

    if not rest:
        return await message.reply_text("<b>ᴜsᴀɢᴇ:</b>\n<code>/add_bal user_id amount</code>")

    try:
        amount = int(rest[0])
    except ValueError:
        return await message.reply_text("<b>❌ ᴀᴍᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɴᴜᴍʙᴇʀ.</b>")

    if not await db.is_user_exist(target):
        return await message.reply_text("<b>❌ ᴛʜɪs ᴜsᴇʀ ʜᴀs ɴᴇᴠᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.</b>")

    await db.add_ftmbucks(target, amount)
    new_balance = await db.get_ftmbucks(target)
    await message.reply_text(
        f"<b>✅ ʙᴀʟᴀɴᴄᴇ ᴜᴘᴅᴀᴛᴇᴅ!</b>\n\n"
        f"👤 ᴜsᴇʀ: <code>{target}</code>\n"
        f"➕ ᴀᴅᴅᴇᴅ: <code>{amount}</code>\n"
        f"💰 ɴᴇᴡ ʙᴀʟᴀɴᴄᴇ: <code>{new_balance}</code>"
    )
    try:
        await client.send_message(
            target,
            f"<b>💰 {amount} ғᴛᴍʙᴜᴄᴋs ʜᴀᴠᴇ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʙʏ ᴀᴅᴍɪɴ!</b>\n\n"
            f"ᴄᴜʀʀᴇɴᴛ ʙᴀʟᴀɴᴄᴇ: <code>{new_balance}</code>"
        )
    except Exception:
        pass

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /info ============

@Client.on_message(filters.private & filters.command(['info']))
async def info_cmd(client, message):
    args = message.text.split()
    target = message.from_user.id
    if len(args) > 1 and await is_authorized(message.from_user.id):
        uid, _ = await resolve_user(client, args[1])
        if uid:
            target = uid
    elif message.reply_to_message and await is_authorized(message.from_user.id):
        target = message.reply_to_message.from_user.id

    user = await db.get_user(target)
    if not user:
        return await message.reply_text("<b>❌ ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ.</b>")

    plan_key, expiry = await db.get_plan(target)
    plan_name = PLANS.get(plan_key, PLANS['free'])['name']
    expiry_txt = expiry.strftime('%d-%m-%Y %H:%M:%S UTC') if expiry else "N/A"
    is_admin = "✅" if await db.is_admin(target) else "❌"
    ftmbucks = await db.get_ftmbucks(target)
    total_refs = await db.get_total_referrals(target)

    reg = user.get('registered_at')
    reg_date = "N/A"
    if reg:
        if isinstance(reg, str):
            reg = datetime.datetime.fromisoformat(reg)
        reg_date = reg.strftime('%d-%m-%Y %H:%M:%S')

    await message.reply_text(
        f"<b>📄 ᴜsᴇʀ ɪɴғᴏ</b>\n\n"
        f"👤 ɴᴀᴍᴇ: {user.get('name', 'N/A')}\n"
        f"⚡ ɪᴅ: <code>{target}</code>\n"
        f"💎 ᴘʟᴀɴ: {plan_name}\n"
        f"⏰ ᴇxᴘɪʀʏ: {expiry_txt}\n"
        f"👮 ᴀᴅᴍɪɴ: {is_admin}\n"
        f"💰 ғᴛᴍʙᴜᴄᴋs: <code>{ftmbucks}</code>\n"
        f"👥 ʀᴇғᴇʀʀᴀʟs: <code>{total_refs}</code>\n"
        f"📅 ʀᴇɢɪsᴛᴇʀᴇᴅ: {reg_date}"
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ Admin Panel (inline menu) ============

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_callback_query(filters.regex(r'^adminpanel#'))
async def admin_panel_callback(bot, query):
    if not await is_authorized(query.from_user.id):
        return await query.answer("⛔ ᴀᴅᴍɪɴ ᴏɴʟʏ.", show_alert=True)

    text = (
        "<b>🎛 ᴀᴅᴍɪɴ ᴩᴀɴᴇʟ</b>\n\n"
        "<b>ᴄᴏᴍᴍᴀɴᴅs:</b>\n"
        "• <code>/add_premium user_id plan days</code>\n"
        "• <code>/remove_premium user_id</code>\n"
        "• <code>/add_bal user_id amount</code>\n"
        "• <code>/users</code> — ᴜsᴇʀ sᴛᴀᴛs\n"
        "• <code>/pusers</code> — ᴩʀᴇᴍɪᴜᴍ ᴜsᴇʀ ʟɪsᴛ\n"
        "• <code>/userstats</code> — ᴩʟᴀɴ ʙʀᴇᴀᴋᴅᴏᴡɴ\n"
        "• <code>/info [user_id]</code>\n"
        "• <code>/broadcast</code> (ʀᴇᴩʟʏ)\n"
        "• <code>/pnotify</code> (ʀᴇᴩʟʏ, ᴩʀᴇᴍɪᴜᴍ ᴏɴʟʏ)\n"
        "• <code>/makeadmin user_id</code> (ᴏᴡɴᴇʀ)\n"
        "• <code>/removeadmin user_id</code> (ᴏᴡɴᴇʀ)\n"
        "• <code>/listadmins</code>\n"
        "• <code>/restart</code> (ᴏᴡɴᴇʀ)"
    )
    try:
        await query.message.edit_text(text)
    except Exception:
        await query.message.reply_text(text)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
