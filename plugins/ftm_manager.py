#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

from database import db, PLANS
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# Each entry: (ftm config key, label, required feature/plan, page number)
FTM_MODES = [
    ("delta",          "ꜰᴛᴍ ᴅᴇʟᴛᴀ ᴍᴏᴅᴇ",          "delta",          1),
    ("alpha",          "ꜰᴛᴍ ᴀʟᴘʜᴀ ᴍᴏᴅᴇ",          "alpha",          1),
    ("gamma",          "ꜰᴛᴍ ɢᴀᴍᴍᴀ ᴍᴏᴅᴇ",          "gamma",          1),
    ("theta",          "ꜰᴛᴍ ᴛʜᴇᴛᴀ ᴍᴏᴅᴇ",          "theta",          1),
    ("watermark",      "ꜰᴛᴍ ᴡᴀᴛᴇʀᴍᴀʀᴋ",            "watermark",      1),
    ("pi",             "ꜰᴛᴍ ᴩɪ ᴍᴏᴅᴇ",              "pi",             1),
    ("blast",          "ꜰᴛᴍ ʙʟᴀsᴛ ᴍᴏᴅᴇ",           "blast",          2),
    ("replacer",       "ꜰᴛᴍ ʀᴇᴩʟᴀᴄᴇʀ",             "replacer",       2),
    ("remover",        "ꜰᴛᴍ ʀᴇᴍᴏᴠᴇʀ",              "remover",        2),
    ("auto_numbering", "ꜰᴛᴍ ᴀᴜᴛᴏ ɴᴜᴍʙᴇʀɪɴɢ",       "auto_numbering", 2),
    ("bullets",        "ꜰᴛᴍ ʙᴜʟʟᴇᴛs",              "bullets",        2),
    ("course_sellers", "ꜰᴛᴍ ᴄᴏᴜʀsᴇ sᴇʟʟᴇʀs ᴍᴏᴅᴇ",  "course_sellers", 2),
    ("link_remover",   "ꜰᴛᴍ ʟɪɴᴋ ʀᴇᴍᴏᴠᴇʀ",         "link_remover",   3),
    ("text_only",      "ꜰᴛᴍ ᴛᴇxᴛ ᴏɴʟʏ ᴍᴏᴅᴇ",       "text_only",      3),
    ("unequify",       "ᴜɴᴇQᴜɪғʏ (ʀᴇᴍᴏᴠᴇ ᴅᴜᴘʟɪᴄᴀᴛᴇs)", "unequify",    3),
]

TOTAL_PAGES = 3

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# Map feature -> minimum plan name (for the lock label, e.g. "(INFINITY)")
FEATURE_PLAN_LABEL = {}
for plan_key, plan_data in PLANS.items():
    for feat in plan_data["features"]:
        if feat not in FEATURE_PLAN_LABEL:
            FEATURE_PLAN_LABEL[feat] = plan_key

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

async def build_ftm_menu(user_id, page):
    plan_key, _ = await db.get_plan(user_id)
    user_features = set(PLANS.get(plan_key, PLANS["free"])["features"])
    configs = await db.get_configs(user_id)
    ftm_config = configs.get("ftm", {})

    buttons = []
    for key, label, feature, mode_page in FTM_MODES:
        if mode_page != page:
            continue
        if feature not in user_features:
            required_plan = FEATURE_PLAN_LABEL.get(feature, "ultra")
            required_name = PLANS[required_plan]["name"].upper()
            buttons.append([InlineKeyboardButton(f"🔒 {label} ({required_name})", callback_data=f"ftm#locked_{feature}")])
        else:
            enabled = ftm_config.get(key, False)
            status = "✅" if enabled else "❌"
            buttons.append([InlineKeyboardButton(f"{status} {label}", callback_data=f"ftm#toggle_{key}_{page}")])

    nav_row = []
    if page > 1:
        nav_row.append(InlineKeyboardButton("◀ ᴩʀᴇᴠ", callback_data=f"ftm#page_{page-1}"))
    nav_row.append(InlineKeyboardButton(f"📄 {page} / {TOTAL_PAGES}", callback_data="ftm#noop"))
    if page < TOTAL_PAGES:
        nav_row.append(InlineKeyboardButton("ɴᴇxᴛ ▶", callback_data=f"ftm#page_{page+1}"))
    buttons.append(nav_row)

    # Extra config buttons relevant to this page
    if page == 1:
        buttons.append([InlineKeyboardButton("✏️ sᴇᴛ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ", callback_data="ftm#set_watermark")])
    if page == 2:
        buttons.append([InlineKeyboardButton("✏️ sᴇᴛ ʀᴇᴩʟᴀᴄᴇʀ ᴡᴏʀᴅs", callback_data="ftm#set_replacer")])
        buttons.append([InlineKeyboardButton("✏️ sᴇᴛ ʀᴇᴍᴏᴠᴇʀ ᴡᴏʀᴅs", callback_data="ftm#set_remover")])
        buttons.append([InlineKeyboardButton("✏️ sᴇᴛ ʙʟᴀsᴛ ᴛᴀʀɢᴇᴛs", callback_data="ftm#set_blast")])

    buttons.append([InlineKeyboardButton("• ʙᴀᴄᴋ", callback_data="settings#main")])

    plan_name = PLANS.get(plan_key, PLANS["free"])["name"]
    text = (
        "🚀 <b>ꜰᴛᴍ ᴍᴀɴᴀɢᴇʀ</b> 🚀\n\n"
        f"ʏᴏᴜʀ ᴩʟᴀɴ: <b>{plan_name}</b>\n\n"
        "ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ғᴏʀᴡᴀʀᴅɪɴɢ ᴛʀᴀɴsғᴏʀᴍᴀᴛɪᴏɴ ᴍᴏᴅᴇs.\n"
        "ᴛᴀᴩ ᴀ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴛʜᴀᴛ ᴍᴏᴅᴇ."
    )
    return text, InlineKeyboardMarkup(buttons)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_callback_query(filters.regex(r'^ftm#'))
async def ftm_manager_callback(bot, query):
    user_id = query.from_user.id
    data = query.data.split("#", 1)[1]

    if data == "noop":
        return await query.answer()

    if data.startswith("page_"):
        page = int(data.split("_")[1])
        text, markup = await build_ftm_menu(user_id, page)
        await query.message.edit_text(text, reply_markup=markup)
        return

    if data.startswith("locked_"):
        feature = data.split("_", 1)[1]
        required_plan = FEATURE_PLAN_LABEL.get(feature, "ultra")
        plan_name = PLANS[required_plan]["name"]
        await query.answer(
            f"🔒 ᴛʜɪs ᴍᴏᴅᴇ ʀᴇQᴜɪʀᴇs {plan_name.upper()} ᴩʟᴀɴ ᴏʀ ᴀʙᴏᴠᴇ.\nᴜsᴇ /plans ᴛᴏ ᴜᴩɢʀᴀᴅᴇ.",
            show_alert=True
        )
        return

    if data.startswith("toggle_"):
        # Use rsplit to correctly handle keys with underscores (e.g. auto_numbering, link_remover)
        # format: "toggle_<key>_<page>" where key itself may contain underscores
        rest = data.split("_")
        page = int(rest[-1])
        key = "_".join(rest[1:-1])

        plan_key, _ = await db.get_plan(user_id)
        user_features = set(PLANS.get(plan_key, PLANS["free"])["features"])

        feature_required = None
        for k, _, feature, _ in FTM_MODES:
            if k == key:
                feature_required = feature
                break

        if feature_required and feature_required not in user_features:
            required_plan = FEATURE_PLAN_LABEL.get(feature_required, "ultra")
            await query.answer(
                f"🔒 ʏᴏᴜ ɴᴇᴇᴅ {PLANS[required_plan]['name'].upper()} ᴩʟᴀɴ ᴏʀ ᴀʙᴏᴠᴇ ᴛᴏ ᴜsᴇ ᴛʜɪs.",
                show_alert=True
            )
            return

        configs = await db.get_configs(user_id)
        ftm_config = configs.get("ftm", {})
        current = ftm_config.get(key, False)

        # Special handling for modes that require extra setup before enabling
        if key == "watermark" and not current and not ftm_config.get("watermark_text"):
            await query.answer(
                "⚠️ sᴇᴛ ʏᴏᴜʀ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ ғɪʀsᴛ ᴜsɪɴɢ 'sᴇᴛ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ' ʙᴜᴛᴛᴏɴ.",
                show_alert=True
            )
            return
        if key == "replacer" and not current and not ftm_config.get("replacer"):
            await query.answer(
                "⚠️ sᴇᴛ ʏᴏᴜʀ ʀᴇᴩʟᴀᴄᴇʀ ᴡᴏʀᴅs ғɪʀsᴛ ᴜsɪɴɢ 'sᴇᴛ ʀᴇᴩʟᴀᴄᴇʀ ᴡᴏʀᴅs' ʙᴜᴛᴛᴏɴ.",
                show_alert=True
            )
            return
        if key == "remover" and not current and not ftm_config.get("remover"):
            await query.answer(
                "⚠️ sᴇᴛ ʏᴏᴜʀ ʀᴇᴍᴏᴠᴇʀ ᴡᴏʀᴅs ғɪʀsᴛ ᴜsɪɴɢ 'sᴇᴛ ʀᴇᴍᴏᴠᴇʀ ᴡᴏʀᴅs' ʙᴜᴛᴛᴏɴ.",
                show_alert=True
            )
            return
        if key == "blast" and not current and not ftm_config.get("blast_targets"):
            await query.answer(
                "⚠️ sᴇᴛ ʏᴏᴜʀ ʙʟᴀsᴛ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟs ғɪʀsᴛ ᴜsɪɴɢ 'sᴇᴛ ʙʟᴀsᴛ ᴛᴀʀɢᴇᴛs' ʙᴜᴛᴛᴏɴ.",
                show_alert=True
            )
            return

        # Replacer/remover are enabled simply by having non-empty data.
        # Toggling "off" clears the stored data (and "on" requires data to already exist,
        # which is enforced by the checks above).
        if key == "replacer":
            if current:
                await db.update_ftm_config(user_id, "replacer", {})
            # else: already validated non-empty above, nothing to do
        elif key == "remover":
            if current:
                await db.update_ftm_config(user_id, "remover", [])
        else:
            await db.update_ftm_config(user_id, key, not current)

        text, markup = await build_ftm_menu(user_id, page)
        await query.message.edit_text(text, reply_markup=markup)
        return

    if data == "set_watermark":
        await query.message.delete()
        msg = await bot.ask(
            chat_id=user_id,
            text="✏️ <b>sᴇɴᴅ ʏᴏᴜʀ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ</b>\n\n"
                 "ᴛʜɪs ᴛᴇxᴛ ᴡɪʟʟ ʙᴇ ᴀᴅᴅᴇᴅ ᴀs ᴀ ᴩʀᴇғɪx/sᴜғғɪx ᴛᴏ ᴄᴀᴩᴛɪᴏɴs.\n\n"
                 "/cancel - ᴄᴀɴᴄᴇʟ"
        )
        if msg.text and msg.text.strip() == "/cancel":
            await msg.reply_text("<b>ᴄᴀɴᴄᴇʟʟᴇᴅ.</b>")
        else:
            await db.update_ftm_config(user_id, "watermark_text", msg.text.html if msg.text else "")
            await msg.reply_text("<b>✅ ᴡᴀᴛᴇʀᴍᴀʀᴋ ᴛᴇxᴛ sᴇᴛ.</b>")
        text, markup = await build_ftm_menu(user_id, 1)
        await bot.send_message(user_id, text, reply_markup=markup)
        return

    if data == "set_replacer":
        await query.message.delete()
        msg = await bot.ask(
            chat_id=user_id,
            text="✏️ <b>sᴇɴᴅ ʀᴇᴩʟᴀᴄᴇ ᴩᴀɪʀs</b>\n\n"
                 "ғᴏʀᴍᴀᴛ (ᴏɴᴇ ᴩᴇʀ ʟɪɴᴇ):\n"
                 "<code>old_word=new_word</code>\n\n"
                 "ᴇxᴀᴍᴩʟᴇ:\n"
                 "<code>@oldchannel=@newchannel\nfree=premium</code>\n\n"
                 "/cancel - ᴄᴀɴᴄᴇʟ"
        )
        if msg.text and msg.text.strip() == "/cancel":
            await msg.reply_text("<b>ᴄᴀɴᴄᴇʟʟᴇᴅ.</b>")
        else:
            replacer_map = {}
            for line in (msg.text or "").split("\n"):
                if "=" in line:
                    old, new = line.split("=", 1)
                    old, new = old.strip(), new.strip()
                    if old:
                        replacer_map[old] = new
            if replacer_map:
                configs = await db.get_configs(user_id)
                configs["ftm"]["replacer"] = replacer_map
                await db.update_configs(user_id, configs)
                await msg.reply_text(f"<b>✅ {len(replacer_map)} ʀᴇᴩʟᴀᴄᴇ ᴩᴀɪʀ(s) sᴀᴠᴇᴅ.</b>")
            else:
                await msg.reply_text("<b>❌ ɴᴏ ᴠᴀʟɪᴅ ᴩᴀɪʀs ғᴏᴜɴᴅ. ᴜsᴇ ғᴏʀᴍᴀᴛ: old=new</b>")
        text, markup = await build_ftm_menu(user_id, 2)
        await bot.send_message(user_id, text, reply_markup=markup)
        return

    if data == "set_blast":
        await query.message.delete()
        msg = await bot.ask(
            chat_id=user_id,
            text="✏️ <b>sᴇɴᴅ ʙʟᴀsᴛ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ ɪᴅs</b>\n\n"
                 "ᴏɴᴇ ᴄʜᴀᴛ ɪᴅ ᴩᴇʀ ʟɪɴᴇ (ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ/ʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴀʟʟ ᴏғ ᴛʜᴇᴍ).\n"
                 "ᴇᴀᴄʜ ғᴏʀᴡᴀʀᴅᴇᴅ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ᴀʟsᴏ ʙᴇ sᴇɴᴛ ᴛᴏ ᴛʜᴇsᴇ ᴄʜᴀᴛs.\n\n"
                 "ᴇxᴀᴍᴩʟᴇ:\n"
                 "<code>-1001234567890\n-1009876543210</code>\n\n"
                 "/cancel - ᴄᴀɴᴄᴇʟ"
        )
        if msg.text and msg.text.strip() == "/cancel":
            await msg.reply_text("<b>ᴄᴀɴᴄᴇʟʟᴇᴅ.</b>")
        else:
            targets = []
            for line in (msg.text or "").split("\n"):
                line = line.strip()
                if not line:
                    continue
                try:
                    targets.append(int(line))
                except ValueError:
                    pass
            if targets:
                await db.update_ftm_config(user_id, "blast_targets", targets)
                await msg.reply_text(f"<b>✅ {len(targets)} ʙʟᴀsᴛ ᴛᴀʀɢᴇᴛ(s) sᴀᴠᴇᴅ.</b>")
            else:
                await msg.reply_text("<b>❌ ɴᴏ ᴠᴀʟɪᴅ ᴄʜᴀᴛ ɪᴅs ᴩʀᴏᴠɪᴅᴇᴅ.</b>")
        text, markup = await build_ftm_menu(user_id, 2)
        await bot.send_message(user_id, text, reply_markup=markup)
        return

    if data == "set_remover":
        await query.message.delete()
        msg = await bot.ask(
            chat_id=user_id,
            text="✏️ <b>sᴇɴᴅ ᴡᴏʀᴅs/ᴩʜʀᴀsᴇs ᴛᴏ ʀᴇᴍᴏᴠᴇ</b>\n\n"
                 "ᴏɴᴇ ᴩᴇʀ ʟɪɴᴇ.\n\n"
                 "ᴇxᴀᴍᴩʟᴇ:\n"
                 "<code>@spamchannel\nClick here</code>\n\n"
                 "/cancel - ᴄᴀɴᴄᴇʟ"
        )
        if msg.text and msg.text.strip() == "/cancel":
            await msg.reply_text("<b>ᴄᴀɴᴄᴇʟʟᴇᴅ.</b>")
        else:
            words = [line.strip() for line in (msg.text or "").split("\n") if line.strip()]
            if words:
                configs = await db.get_configs(user_id)
                configs["ftm"]["remover"] = words
                await db.update_configs(user_id, configs)
                await msg.reply_text(f"<b>✅ {len(words)} ᴩʜʀᴀsᴇ(s) sᴀᴠᴇᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇʀ.</b>")
            else:
                await msg.reply_text("<b>❌ ɴᴏ ᴩʜʀᴀsᴇs ᴩʀᴏᴠɪᴅᴇᴅ.</b>")
        text, markup = await build_ftm_menu(user_id, 2)
        await bot.send_message(user_id, text, reply_markup=markup)
        return

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

@Client.on_message(filters.private & filters.command(['alpha']))
async def alpha_info_cmd(client, message):
    await message.reply_text(
        "🧪 <b>ꜰᴛᴍ ᴀʟᴩʜᴀ ᴍᴏᴅᴇ</b>\n\n"
        "ᴡʜᴇɴ ᴇɴᴀʙʟᴇᴅ, ᴀʟʟ ᴇᴍᴏᴊɪs ᴀʀᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴄᴀᴩᴛɪᴏɴs/ᴛᴇxᴛ ᴅᴜʀɪɴɢ ғᴏʀᴡᴀʀᴅɪɴɢ.\n\n"
        "ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ɪᴛ ᴠɪᴀ <code>/settings → 🚀 FTM Manager 🚀</code>."
    )

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
