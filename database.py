#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

from os import environ 
import datetime
from config import Config
import motor.motor_asyncio
from pymongo import MongoClient

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

# ============ PLAN DEFINITIONS ============
# Central place that defines what each plan unlocks.
# "ultra" plan unlocks everything (superset of all other plans).

PLANS = {
    "free": {
        "name": "Free",
        "price": 0,
        "days": 0,
        "features": []
    },
    "plus": {
        "name": "Plus",
        "price": 99,
        "days": 30,
        "features": ["forwarding"]
    },
    "pro": {
        "name": "Pro",
        "price": 199,
        "days": 30,
        "features": ["forwarding", "gamma", "watermark", "text_only"]
    },
    "infinity": {
        "name": "Infinity",
        "price": 299,
        "days": 30,
        "features": [
            "forwarding", "gamma", "watermark", "text_only",
            "replacer", "remover", "link_remover", "alpha",
            "course_sellers", "unequify", "auto_numbering", "bullets"
        ]
    },
    "ultra": {
        "name": "Ultra",
        "price": 500,
        "days": 30,
        "features": [
            "forwarding", "gamma", "watermark", "text_only",
            "replacer", "remover", "link_remover", "alpha",
            "course_sellers", "unequify", "auto_numbering", "bullets",
            "delta", "theta", "pi", "blast"
        ]
    },
}

# All known feature flags (used by /myplan to render the checklist)
ALL_FEATURES = [
    ("forwarding", "Forwarding"),
    ("delta", "FTM Delta Mode"),
    ("watermark", "FTM Watermark"),
    ("replacer", "FTM Replacer"),
    ("remover", "FTM Remover"),
    ("link_remover", "FTM Link Remover"),
    ("gamma", "FTM Gamma Mode"),
    ("unequify", "Unequify"),
    ("theta", "FTM Theta Mode"),
    ("pi", "FTM Pi Mode"),
    ("alpha", "FTM Alpha Mode"),
    ("course_sellers", "FTM Course Sellers Mode"),
    ("text_only", "FTM Text Only Mode"),
    ("blast", "FTM Blast Mode"),
    ("auto_numbering", "FTM Auto Numbering"),
    ("bullets", "FTM Bullets"),
]

async def mongodb_version():
    x = MongoClient(Config.DATABASE_URI)
    mongodb_version = x.server_info()['version']
    return mongodb_version

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def _deep_merge_defaults(default, stored):
    """Recursively fill missing keys in `stored` with values from `default`.
    Returns a new dict; does not mutate inputs."""
    if not isinstance(stored, dict):
        return stored
    merged = dict(stored)
    for key, value in default.items():
        if key not in merged:
            merged[key] = value
        elif isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge_defaults(value, merged[key])
    return merged

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.bot = self.db.bots
        self.col = self.db.users
        self.nfy = self.db.notify
        self.chl = self.db.channels 
        
    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
            ban_status=dict(
                is_banned=False,
                ban_reason="",
            ),
            plan="free",
            plan_expiry=None,
            registered_at=datetime.datetime.utcnow(),
            is_admin=False,
            ftmbucks=0,
            referred_by=None,
            referral_code=None,
            total_referrals=0,
            free_trial_used=False,
        )
 
 #Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz      
                
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return bool(user)
    
    async def total_users_bots_count(self):
        bcount = await self.bot.count_documents({})
        count = await self.col.count_documents({})
        return count, bcount

    async def total_channels(self):
        count = await self.chl.count_documents({})
        return count
    
    async def remove_ban(self, id):
        ban_status = dict(
            is_banned=False,
            ban_reason=''
        )
        await self.col.update_one({'id': id}, {'$set': {'ban_status': ban_status}})
    
    async def ban_user(self, user_id, ban_reason="No Reason"):
        ban_status = dict(
            is_banned=True,
            ban_reason=ban_reason
        )
        await self.col.update_one({'id': user_id}, {'$set': {'ban_status': ban_status}})

    async def get_ban_status(self, id):
        default = dict(
            is_banned=False,
            ban_reason=''
        )
        user = await self.col.find_one({'id':int(id)})
        if not user:
            return default
        return user.get('ban_status', default)

    async def get_all_users(self):
        return self.col.find({})
    
    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})
 
    async def get_banned(self):
        users = self.col.find({'ban_status.is_banned': True})
        b_users = [user['id'] async for user in users]
        return b_users

    async def update_configs(self, id, configs):
        await self.col.update_one({'id': int(id)}, {'$set': {'configs': configs}})

    async def update_ftm_config(self, user_id, key, value):
        configs = await self.get_configs(user_id)
        configs['ftm'][key] = value
        await self.update_configs(user_id, configs)
        return configs
         
    async def get_configs(self, id):
        default = {
            'caption': None,
            'duplicate': True,
            'forward_tag': False,
            'file_size': 0,
            'size_limit': None,
            'extension': None,
            'keywords': None,
            'protect': None,
            'button': None,
            'db_uri': None,
            'filters': {
               'poll': True,
               'text': True,
               'audio': True,
               'voice': True,
               'video': True,
               'photo': True,
               'document': True,
               'animation': True,
               'sticker': True
            },
            'ftm': {
               'delta': False,
               'alpha': False,
               'gamma': False,
               'gamma_from': None,
               'gamma_to': None,
               'gamma_last_msg_id': 0,
               'theta': False,
               'watermark': False,
               'pi': False,
               'replacer': {},
               'remover': [],
               'link_remover': False,
               'course_sellers': False,
               'text_only': False,
               'unequify': False,
               'auto_numbering': False,
               'bullets': False,
               'blast': False,
               'blast_targets': [],
               'watermark_text': '',
               'watermark_position': 'suffix',
               'auto_number_start': 1,
               'auto_number_current': 1,
            }
        }
        user = await self.col.find_one({'id':int(id)})
        if user:
            stored = user.get('configs', default)
            return _deep_merge_defaults(default, stored)
        return default 
       
    async def add_bot(self, datas):
       await self.bot.update_one(
          {'user_id': datas['user_id']},
          {'$set': datas},
          upsert=True
       )
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz     
    async def remove_bot(self, user_id):
       await self.bot.delete_many({'user_id': int(user_id)})
      
    async def get_bot(self, user_id: int):
       bot = await self.bot.find_one({'user_id': user_id})
       return bot if bot else None
                                          
    async def is_bot_exist(self, user_id):
       bot = await self.bot.find_one({'user_id': user_id})
       return bool(bot)
                                          
    async def in_channel(self, user_id: int, chat_id: int) -> bool:
       channel = await self.chl.find_one({"user_id": int(user_id), "chat_id": int(chat_id)})
       return bool(channel)
    
    async def add_channel(self, user_id: int, chat_id: int, title, username):
       channel = await self.in_channel(user_id, chat_id)
       if channel:
         return False
       return await self.chl.insert_one({"user_id": user_id, "chat_id": chat_id, "title": title, "username": username})
    
    async def remove_channel(self, user_id: int, chat_id: int):
       channel = await self.in_channel(user_id, chat_id )
       if not channel:
         return False
       return await self.chl.delete_many({"user_id": int(user_id), "chat_id": int(chat_id)})
    
    async def get_channel_details(self, user_id: int, chat_id: int):
       return await self.chl.find_one({"user_id": int(user_id), "chat_id": int(chat_id)})
       
    async def get_user_channels(self, user_id: int):
       channels = self.chl.find({"user_id": int(user_id)})
       return [channel async for channel in channels]
     
    async def get_filters(self, user_id):
       filters = []
       filter = (await self.get_configs(user_id))['filters']
       for k, v in filter.items():
          if v == False:
            filters.append(str(k))
       return filters
              
    async def add_frwd(self, user_id):
       return await self.nfy.insert_one({'user_id': int(user_id)})
    
    async def rmve_frwd(self, user_id=0, all=False):
       data = {} if all else {'user_id': int(user_id)}
       return await self.nfy.delete_many(data)
    
    async def get_all_frwd(self):
       return self.nfy.find({})

    # ============ PLAN / PREMIUM METHODS ============

    async def get_user(self, user_id):
       return await self.col.find_one({'id': int(user_id)})

    async def get_plan(self, user_id):
       """Returns (plan_key, expiry_datetime_or_None). Auto-downgrades to free if expired."""
       user = await self.get_user(user_id)
       if not user:
          return "free", None
       plan = user.get('plan', 'free')
       expiry = user.get('plan_expiry')
       if plan != "free" and expiry:
          if isinstance(expiry, str):
             expiry = datetime.datetime.fromisoformat(expiry)
          if expiry < datetime.datetime.utcnow():
             # expired -> downgrade
             await self.col.update_one(
                 {'id': int(user_id)},
                 {'$set': {'plan': 'free', 'plan_expiry': None}}
             )
             return "free", None
       return plan, expiry

    async def set_plan(self, user_id, plan_key, days=None):
       """Set a user's plan. days=None means permanent (no expiry). days=0 removes plan (free)."""
       plan_key = plan_key.lower()
       if plan_key not in PLANS:
          raise ValueError(f"Unknown plan: {plan_key}")
       if plan_key == "free" or days == 0:
          await self.col.update_one(
              {'id': int(user_id)},
              {'$set': {'plan': 'free', 'plan_expiry': None}}
          )
          return None
       expiry = None
       if days is not None:
          expiry = datetime.datetime.utcnow() + datetime.timedelta(days=float(days))
       await self.col.update_one(
           {'id': int(user_id)},
           {'$set': {'plan': plan_key, 'plan_expiry': expiry}}
       )
       return expiry

    async def add_premium_time(self, user_id, plan_key, days):
       """Add `days` to a user's current plan expiry (extend), or set fresh if none/expired/different plan."""
       plan_key = plan_key.lower()
       if plan_key not in PLANS:
          raise ValueError(f"Unknown plan: {plan_key}")
       current_plan, current_expiry = await self.get_plan(user_id)
       now = datetime.datetime.utcnow()
       if current_plan == plan_key and current_expiry and current_expiry > now:
          new_expiry = current_expiry + datetime.timedelta(days=float(days))
       else:
          new_expiry = now + datetime.timedelta(days=float(days))
       await self.col.update_one(
           {'id': int(user_id)},
           {'$set': {'plan': plan_key, 'plan_expiry': new_expiry}}
       )
       return new_expiry

    async def remove_premium(self, user_id):
       await self.col.update_one(
           {'id': int(user_id)},
           {'$set': {'plan': 'free', 'plan_expiry': None}}
       )

    async def has_feature(self, user_id, feature_key):
       plan, _ = await self.get_plan(user_id)
       return feature_key in PLANS.get(plan, PLANS["free"])["features"]

    async def get_premium_users(self):
       users = self.col.find({'plan': {'$ne': 'free'}})
       return [user async for user in users]

    async def get_premium_count(self):
       return await self.col.count_documents({'plan': {'$ne': 'free'}})

    # ============ ADMIN METHODS ============

    async def is_admin(self, user_id):
       if int(user_id) in Config.BOT_OWNER_ID:
          return True
       user = await self.get_user(user_id)
       if not user:
          return False
       return bool(user.get('is_admin', False))

    async def add_admin(self, user_id):
       await self.col.update_one({'id': int(user_id)}, {'$set': {'is_admin': True}})

    async def remove_admin(self, user_id):
       await self.col.update_one({'id': int(user_id)}, {'$set': {'is_admin': False}})

    async def get_admins(self):
       users = self.col.find({'is_admin': True})
       return [user async for user in users]

    # ============ FTMBUCKS / REFERRAL METHODS ============

    async def set_referral_code(self, user_id, code):
       await self.col.update_one({'id': int(user_id)}, {'$set': {'referral_code': code}})

    async def get_by_referral_code(self, code):
       return await self.col.find_one({'referral_code': code})

    async def set_referred_by(self, user_id, referrer_id):
       await self.col.update_one({'id': int(user_id)}, {'$set': {'referred_by': int(referrer_id)}})

    async def add_ftmbucks(self, user_id, amount):
       await self.col.update_one({'id': int(user_id)}, {'$inc': {'ftmbucks': int(amount)}})

    async def get_ftmbucks(self, user_id):
       user = await self.get_user(user_id)
       if not user:
          return 0
       return user.get('ftmbucks', 0)

    async def deduct_ftmbucks(self, user_id, amount):
       await self.col.update_one({'id': int(user_id)}, {'$inc': {'ftmbucks': -int(amount)}})

    async def increment_referrals(self, user_id):
       await self.col.update_one({'id': int(user_id)}, {'$inc': {'total_referrals': 1}})

    async def get_total_referrals(self, user_id):
       user = await self.get_user(user_id)
       if not user:
          return 0
       return user.get('total_referrals', 0)

    async def get_referred_users(self, user_id):
       users = self.col.find({'referred_by': int(user_id)})
       return [user async for user in users]

    # ============ UNEQUIFY (DUPLICATE FILE TRACKING) ============

    async def is_duplicate_file(self, user_id, file_unique_id):
       doc = await self.db.unequify.find_one({'user_id': int(user_id), 'file_unique_id': file_unique_id})
       return doc is not None

    async def mark_file_seen(self, user_id, file_unique_id):
       await self.db.unequify.update_one(
           {'user_id': int(user_id), 'file_unique_id': file_unique_id},
           {'$set': {'user_id': int(user_id), 'file_unique_id': file_unique_id}},
           upsert=True
       )

    async def clear_seen_files(self, user_id):
       await self.db.unequify.delete_many({'user_id': int(user_id)})

    # ============ GAMMA MODE (AUTO-FORWARD) ============

    async def get_gamma_users(self):
       users = self.col.find({'configs.ftm.gamma': True})
       return [user async for user in users]

    # ============ FREE TRIAL ============

    async def has_used_free_trial(self, user_id):
       user = await self.get_user(user_id)
       if not user:
          return False
       return bool(user.get('free_trial_used', False))

    async def mark_free_trial_used(self, user_id):
       await self.col.update_one({'id': int(user_id)}, {'$set': {'free_trial_used': True}})

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
    
db = Database(Config.DATABASE_URI, Config.DATABASE_NAME)
