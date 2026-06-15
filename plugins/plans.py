#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

import string
import random
import datetime
from database import db, PLANS, ALL_FEATURES
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ HELPERS ============

def feature_checklist(plan_key):
    plan = PLANS.get(plan_key, PLANS["free"])
    lines = []
    for key, label in ALL_FEATURES:
        mark = "✅" if key in plan["features"] else "❌"
        lines.append(f"{mark} {label.upper()}")
    return "\n".join(lines)

def feature_list_only(plan_key):
    plan = PLANS.get(plan_key, PLANS["free"])
    lines = []
    for key, label in ALL_FEATURES:
        if key in plan["features"]:
            lines.append(f"✅ {label.upper()}")
    if not lines:
        lines.append("❌ ɴᴏ ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs")
    return "\n".join(lines)

def main_subscription_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton('📊 ᴍʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ', callback_data='plan#myplan')],
        [InlineKeyboardButton('⭐ ᴘʟᴜs', callback_data='plan#detail_plus'),
         InlineKeyboardButton('💎 ᴘʀᴏ', callback_data='plan#detail_pro')],
        [InlineKeyboardButton('♾️ ɪɴғɪɴɪᴛʏ', callback_data='plan#detail_infinity'),
         InlineKeyboardButton('🚀 ᴜʟᴛʀᴀ', callback_data='plan#detail_ultra')],
        [InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='back')]
    ])

def plan_detail_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton('📞 ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ', url='https://t.me/anujeditbyak')],
        [InlineKeyboardButton('◀ ʙᴀᴄᴋ', callback_data='plan#subscription')]
    ])

async def render_subscription_list():
    text = ""
    for key in ["free", "plus", "pro", "infinity", "ultra"]:
        plan = PLANS[key]
        emoji = Translation.PLAN_EMOJIS[key]
        desc = Translation.PLAN_DESCRIPTIONS[key]
        price_txt = "ғʀᴇᴇ" if plan["price"] == 0 else f"{plan['price']} ғᴏʀ {plan['days']} ᴅᴀʏs"
        text += f"\n{emoji} <b>{plan['name']}</b>\n{desc}\n💰 {price_txt}\n"
    return Translation.SUBSCRIPTION_TXT.format(text)

async def safe_edit_or_reply(message, text, reply_markup=None, **kwargs):
    """Edit message text if possible, otherwise (e.g. photo captions) send a new message."""
    try:
        return await message.edit_text(text, reply_markup=reply_markup, **kwargs)
    except Exception:
        return await message.reply_text(text, reply_markup=reply_markup, **kwargs)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /myplan ============

async def myplan_text(user):
    plan_key, expiry = await db.get_plan(user.id)
    plan = PLANS.get(plan_key, PLANS["free"])
    plan_name = f"{Translation.PLAN_EMOJIS[plan_key]} {plan['name']}"
    plan_type = "ғʀᴇᴇ" if plan_key == "free" else "ᴘʀᴇᴍɪᴜᴍ"

    db_user = await db.get_user(user.id)
    reg_date = "N/A"
    if db_user and db_user.get('registered_at'):
        reg = db_user['registered_at']
        if isinstance(reg, str):
            reg = datetime.datetime.fromisoformat(reg)
        reg_date = reg.strftime("%d-%m-%Y")

    if plan_key == "free" or not expiry:
        expiry_txt = "N/A"
    else:
        expiry_txt = expiry.strftime("%d-%m-%Y %H:%M:%S UTC")

    return Translation.MY_PLAN_TXT.format(
        user.mention,
        user.id,
        plan_name,
        plan_type,
        reg_date,
        expiry_txt,
        feature_checklist(plan_key)
    )

@Client.on_message(filters.private & filters.command(['myplan']))
async def myplan_cmd(client, message):
    text = await myplan_text(message.from_user)
    await message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('◀ ʙᴀᴄᴋ', callback_data='plan#subscription')]])
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /plans /subscription ============

@Client.on_message(filters.private & filters.command(['plans', 'subscription', 'plan']))
async def plans_cmd(client, message):
    text = await render_subscription_list()
    await message.reply_text(text, reply_markup=main_subscription_buttons(), disable_web_page_preview=True)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_callback_query(filters.regex(r'^plan#'))
async def plan_callback(bot, query):
    data = query.data.split("#")[1]
    user = query.from_user

    if data == "subscription":
        text = await render_subscription_list()
        await safe_edit_or_reply(query.message, text, reply_markup=main_subscription_buttons(), disable_web_page_preview=True)

    elif data == "myplan":
        text = await myplan_text(user)
        await safe_edit_or_reply(
            query.message,
            text,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('◀ ʙᴀᴄᴋ', callback_data='plan#subscription')]])
        )

    elif data.startswith("detail_"):
        plan_key = data.split("_")[1]
        plan = PLANS.get(plan_key)
        if not plan:
            return await query.answer("Invalid plan", show_alert=True)
        emoji = Translation.PLAN_EMOJIS[plan_key]
        text = Translation.PLAN_DETAIL_TXT.format(
            emoji=emoji,
            name=plan['name'],
            description=Translation.PLAN_DESCRIPTIONS[plan_key],
            price=plan['price'],
            days=plan['days'],
            features=feature_list_only(plan_key)
        )
        await safe_edit_or_reply(query.message, text, reply_markup=plan_detail_buttons())

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /referral ============

def generate_referral_code(user_id):
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"ftmbotzx{suffix}"

@Client.on_message(filters.private & filters.command(['referral']))
async def referral_cmd(client, message):
    user = message.from_user
    db_user = await db.get_user(user.id)
    code = db_user.get('referral_code') if db_user else None
    if not code:
        code = generate_referral_code(user.id)
        await db.set_referral_code(user.id, code)

    me = await client.get_me()
    link = f"https://t.me/{me.username}?start=refer_{code}"
    ftmbucks = await db.get_ftmbucks(user.id)
    total_refs = await db.get_total_referrals(user.id)

    await message.reply_text(
        Translation.REFERRAL_TXT.format(ftmbucks, total_refs, link),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('👥 ᴠɪᴇᴡ ʀᴇғᴇʀʀᴇᴅ ᴜsᴇʀs', callback_data='referral#list')],
            [InlineKeyboardButton('💰 ʀᴇᴅᴇᴇᴍ ғᴛᴍʙᴜᴄᴋs', callback_data='referral#redeem')],
            [InlineKeyboardButton('🔄 ʀᴇғʀᴇsʜ', callback_data='referral#refresh')],
            [InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='back')]
        ]),
        disable_web_page_preview=True
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

REDEEM_TIERS = [
    (5000, "infinity", 30),
    (2000, "pro", 30),
    (1000, "plus", 30),
]

@Client.on_callback_query(filters.regex(r'^referral#'))
async def referral_callback(bot, query):
    data = query.data.split("#")[1]
    user = query.from_user

    if data == "refresh":
        db_user = await db.get_user(user.id)
        code = db_user.get('referral_code') if db_user else None
        if not code:
            code = generate_referral_code(user.id)
            await db.set_referral_code(user.id, code)
        me = await bot.get_me()
        link = f"https://t.me/{me.username}?start=refer_{code}"
        ftmbucks = await db.get_ftmbucks(user.id)
        total_refs = await db.get_total_referrals(user.id)
        await safe_edit_or_reply(
            query.message,
            Translation.REFERRAL_TXT.format(ftmbucks, total_refs, link),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('👥 ᴠɪᴇᴡ ʀᴇғᴇʀʀᴇᴅ ᴜsᴇʀs', callback_data='referral#list')],
                [InlineKeyboardButton('💰 ʀᴇᴅᴇᴇᴍ ғᴛᴍʙᴜᴄᴋs', callback_data='referral#redeem')],
                [InlineKeyboardButton('🔄 ʀᴇғʀᴇsʜ', callback_data='referral#refresh')],
                [InlineKeyboardButton('• ʙᴀᴄᴋ', callback_data='back')]
            ]),
            disable_web_page_preview=True
        )

    elif data == "list":
        referred = await db.get_referred_users(user.id)
        if not referred:
            text = "<b>ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ʀᴇғᴇʀʀᴇᴅ ᴀɴʏᴏɴᴇ ʏᴇᴛ.</b>"
        else:
            lines = [f"• {u.get('name', u['id'])}" for u in referred]
            text = "<b>👥 ʏᴏᴜʀ ʀᴇғᴇʀʀᴇᴅ ᴜsᴇʀs:</b>\n\n" + "\n".join(lines)
        await safe_edit_or_reply(
            query.message,
            text,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('◀ ʙᴀᴄᴋ', callback_data='referral#refresh')]])
        )

    elif data == "redeem":
        ftmbucks = await db.get_ftmbucks(user.id)
        for cost, plan_key, days in REDEEM_TIERS:
            if ftmbucks >= cost:
                await db.deduct_ftmbucks(user.id, cost)
                new_expiry = await db.add_premium_time(user.id, plan_key, days)
                plan_name = PLANS[plan_key]['name']
                await safe_edit_or_reply(
                    query.message,
                    f"<b>🎉 sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴅᴇᴇᴍᴇᴅ!</b>\n\n"
                    f"💎 ᴘʟᴀɴ: {plan_name}\n"
                    f"⏰ ᴠᴀʟɪᴅ ᴜɴᴛɪʟ: {new_expiry.strftime('%d-%m-%Y %H:%M:%S UTC')}\n"
                    f"💰 ᴄᴏsᴛ: {cost} ғᴛᴍʙᴜᴄᴋs",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('◀ ʙᴀᴄᴋ', callback_data='referral#refresh')]])
                )
                return
        await query.answer(
            f"ɴᴏᴛ ᴇɴᴏᴜɢʜ ғᴛᴍʙᴜᴄᴋs! ʏᴏᴜ ʜᴀᴠᴇ {ftmbucks}, ɴᴇᴇᴅ ᴀᴛ ʟᴇᴀsᴛ 1000.",
            show_alert=True
        )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /free ============

@Client.on_message(filters.private & filters.command(['free']))
async def free_trial_cmd(client, message):
    user = message.from_user

    if await db.has_used_free_trial(user.id):
        return await message.reply_text(
            "<b>⚠️ ʏᴏᴜ ʜᴀᴠᴇ ᴀʟʀᴇᴀᴅʏ ᴄʟᴀɪᴍᴇᴅ ʏᴏᴜʀ ғʀᴇᴇ ᴛʀɪᴀʟ.</b>\n\nᴜsᴇ /plans ᴛᴏ sᴇᴇ ᴜᴩɢʀᴀᴅᴇ ᴏᴩᴛɪᴏɴs ᴏʀ /referral ᴛᴏ ᴇᴀʀɴ ᴍᴏʀᴇ ᴛɪᴍᴇ."
        )

    plan_key, expiry = await db.get_plan(user.id)
    if plan_key != "free":
        return await message.reply_text(
            "<b>⚠️ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴ.</b>\n\nᴄʜᴇᴄᴋ /myplan ғᴏʀ ᴅᴇᴛᴀɪʟs."
        )

    new_expiry = await db.add_premium_time(user.id, "plus", days=(4 / 24))
    await db.mark_free_trial_used(user.id)

    await message.reply_text(
        "<b>🎉 ғʀᴇᴇ ᴩʟᴜs ᴩʟᴀɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ!</b>\n\n"
        f"⭐ ᴩʟᴀɴ: {PLANS['plus']['name']}\n"
        f"⏰ ᴠᴀʟɪᴅ ғᴏʀ: 4 ʜᴏᴜʀs\n"
        f"📅 ᴇxᴩɪʀᴇs: {new_expiry.strftime('%d-%m-%Y %H:%M:%S UTC')}\n\n"
        f"ᴜsᴇ /myplan ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴩʟᴀɴ."
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /transfer ============

@Client.on_message(filters.private & filters.command(['transfer']))
async def transfer_plan_cmd(client, message):
    user = message.from_user
    args = message.text.split()

    plan_key, expiry = await db.get_plan(user.id)
    if plan_key == "free" or not expiry:
        return await message.reply_text(
            "<b>❌ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ᴩʀᴇᴍɪᴜᴍ ᴩʟᴀɴ ᴛᴏ ᴛʀᴀɴsғᴇʀ.</b>"
        )

    target_id = None
    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id
    elif len(args) >= 2:
        try:
            target_id = int(args[1])
        except ValueError:
            try:
                chat = await client.get_users(args[1])
                target_id = chat.id
            except Exception:
                target_id = None

    if target_id is None:
        return await message.reply_text(
            "<b>ᴜsᴀɢᴇ:</b>\n<code>/transfer user_id</code>\n\nᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ'ѕ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ /transfer"
        )

    if target_id == user.id:
        return await message.reply_text("<b>❌ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴛʀᴀɴsғᴇʀ ᴛᴏ ʏᴏᴜʀsᴇʟғ.</b>")

    if not await db.is_user_exist(target_id):
        return await message.reply_text("<b>❌ ᴛʜᴀᴛ ᴜsᴇʀ ʜᴀs ɴᴇᴠᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.</b>")

    target_plan, _ = await db.get_plan(target_id)
    if target_plan != "free":
        return await message.reply_text("<b>❌ ᴛʜᴀᴛ ᴜsᴇʀ ᴀʟʀᴇᴀᴅʏ ʜᴀs ᴀɴ ᴀᴄᴛɪᴠᴇ ᴩʟᴀɴ.</b>")

    remaining = expiry - datetime.datetime.utcnow()
    remaining_days = remaining.total_seconds() / 86400
    if remaining_days <= 0:
        return await message.reply_text("<b>❌ ʏᴏᴜʀ ᴩʟᴀɴ ʜᴀs ᴇxᴩɪʀᴇᴅ.</b>")

    await message.reply_text(
        f"<b>⚠️ ᴄᴏɴғɪʀᴍ ᴛʀᴀɴsғᴇʀ</b>\n\n"
        f"ᴩʟᴀɴ: {PLANS[plan_key]['name']}\n"
        f"ʀᴇᴍᴀɪɴɪɴɢ: ~{remaining_days:.1f} ᴅᴀʏs\n"
        f"ᴛᴏ: <code>{target_id}</code>\n\n"
        f"ʏᴏᴜʀ ᴩʟᴀɴ ᴡɪʟʟ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀɴᴅ ᴍᴏᴠᴇᴅ ᴛᴏ ᴛʜɪs ᴜsᴇʀ. ᴛʜɪs ᴄᴀɴɴᴏᴛ ʙᴇ ᴜɴᴅᴏɴᴇ.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('✅ ᴄᴏɴғɪʀᴍ', callback_data=f'transfer#confirm_{target_id}'),
             InlineKeyboardButton('❌ ᴄᴀɴᴄᴇʟ', callback_data='transfer#cancel')]
        ])
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_callback_query(filters.regex(r'^transfer#'))
async def transfer_callback(bot, query):
    data = query.data.split("#", 1)[1]
    user = query.from_user

    if data == "cancel":
        return await query.message.edit_text("<b>❌ ᴛʀᴀɴsғᴇʀ ᴄᴀɴᴄᴇʟʟᴇᴅ.</b>")

    if data.startswith("confirm_"):
        target_id = int(data.split("_", 1)[1])

        plan_key, expiry = await db.get_plan(user.id)
        if plan_key == "free" or not expiry:
            return await query.message.edit_text("<b>❌ ʏᴏᴜ ɴᴏ ʟᴏɴɢᴇʀ ʜᴀᴠᴇ ᴀɴ ᴀᴄᴛɪᴠᴇ ᴩʟᴀɴ ᴛᴏ ᴛʀᴀɴsғᴇʀ.</b>")

        target_plan, _ = await db.get_plan(target_id)
        if target_plan != "free":
            return await query.message.edit_text("<b>❌ ᴛᴀʀɢᴇᴛ ᴜsᴇʀ ᴀʟʀᴇᴀᴅʏ ʜᴀs ᴀɴ ᴀᴄᴛɪᴠᴇ ᴩʟᴀɴ.</b>")

        remaining = expiry - datetime.datetime.utcnow()
        remaining_days = remaining.total_seconds() / 86400
        if remaining_days <= 0:
            return await query.message.edit_text("<b>❌ ʏᴏᴜʀ ᴩʟᴀɴ ʜᴀs ᴇxᴩɪʀᴇᴅ.</b>")

        await db.remove_premium(user.id)
        new_expiry = await db.add_premium_time(target_id, plan_key, days=remaining_days)

        await query.message.edit_text(
            f"<b>✅ ᴩʟᴀɴ ᴛʀᴀɴsғᴇʀʀᴇᴅ!</b>\n\n"
            f"💎 {PLANS[plan_key]['name']} ᴩʟᴀɴ (~{remaining_days:.1f} ᴅᴀʏs) sᴇɴᴛ ᴛᴏ <code>{target_id}</code>."
        )
        try:
            await bot.send_message(
                target_id,
                f"<b>🎉 ʏᴏᴜ ʀᴇᴄᴇɪᴠᴇᴅ ᴀ ᴩʟᴀɴ ᴛʀᴀɴsғᴇʀ!</b>\n\n"
                f"💎 ᴩʟᴀɴ: {PLANS[plan_key]['name']}\n"
                f"⏰ ᴇxᴩɪʀᴇs: {new_expiry.strftime('%d-%m-%Y %H:%M:%S UTC')}\n\n"
                f"ᴜsᴇ /myplan ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴩʟᴀɴ."
            )
        except Exception:
            pass

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ /referral_list ============

@Client.on_message(filters.private & filters.command(['referral_list']))
async def referral_list_cmd(client, message):
    user = message.from_user
    referred = await db.get_referred_users(user.id)
    if not referred:
        text = "<b>ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ʀᴇғᴇʀʀᴇᴅ ᴀɴʏᴏɴᴇ ʏᴇᴛ.</b>\n\nsʜᴀʀᴇ ʏᴏᴜʀ ʟɪɴᴋ ᴜsɪɴɢ /referral"
    else:
        lines = [f"• {u.get('name', u['id'])}" for u in referred]
        text = "<b>👥 ʏᴏᴜʀ ʀᴇғᴇʀʀᴇᴅ ᴜsᴇʀs:</b>\n\n" + "\n".join(lines)
    await message.reply_text(text)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
