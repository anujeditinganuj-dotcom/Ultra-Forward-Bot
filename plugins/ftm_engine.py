#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

import re

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

URL_REGEX = re.compile(r'(https?://\S+|t\.me/\S+|@\w{4,32}\b)', re.IGNORECASE)

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002700-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\U00002600-\U000026FF"
    "\U0001F900-\U0001F9FF"
    "\U00002190-\U000021FF"
    "\U00002B00-\U00002BFF"
    "\U0000FE00-\U0000FE0F"
    "\U00010000-\U0010FFFF"
    "]+",
    flags=re.UNICODE
)

# Common promotional/contact patterns used by "course seller" spam captions
COURSE_SELLER_PATTERNS = [
    re.compile(r'(?im)^.*\b(contact|dm|whatsapp|whats app|telegram)\b.*$'),
    re.compile(r'(?im)^.*\b(buy now|purchase|paid course|premium course)\b.*$'),
    re.compile(r'\+?\d[\d\s-]{8,}\d'),  # phone numbers
]

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_replacer(text, replacer_map):
    """replacer_map: dict of {old: new}"""
    if not text or not replacer_map:
        return text
    for old, new in replacer_map.items():
        if old:
            text = re.sub(re.escape(old), new, text, flags=re.IGNORECASE)
    return text

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_remover(text, remove_list):
    """remove_list: list of words/phrases to strip out"""
    if not text or not remove_list:
        return text
    for word in remove_list:
        if word:
            text = re.sub(re.escape(word), '', text, flags=re.IGNORECASE)
    # Clean up resulting double-spaces / blank lines
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_link_remover(text):
    if not text:
        return text
    text = URL_REGEX.sub('', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_alpha_mode(text):
    """FTM Alpha Mode: strips all emojis from the text."""
    if not text:
        return text
    text = EMOJI_PATTERN.sub('', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text.strip()

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_course_sellers_mode(text):
    """Removes promo/contact-style lines & phone numbers commonly used by course-seller spam."""
    if not text:
        return text
    for pattern in COURSE_SELLER_PATTERNS:
        text = pattern.sub('', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_watermark(text, watermark_text, position='suffix'):
    """Adds custom watermark text as prefix or suffix to the caption."""
    if not watermark_text:
        return text
    text = text or ''
    if position == 'prefix':
        return f"{watermark_text}\n{text}".strip()
    return f"{text}\n{watermark_text}".strip()

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_auto_numbering(text, number):
    """Prefixes the caption with an incrementing number e.g. '01. '"""
    text = text or ''
    return f"{number:02d}. {text}".strip()

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_bullets(text):
    """Converts each non-empty line of the caption into a bullet point."""
    if not text:
        return text
    lines = text.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append(line)
            continue
        if stripped.startswith(('•', '-', '*', '◦')):
            result.append(line)
        else:
            result.append(f"• {stripped}")
    return '\n'.join(result)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_delta_mode(text):
    """FTM Delta Mode: alternating-case transformation (e.g. for stylized text)."""
    if not text:
        return text
    result = []
    idx = 0
    for ch in text:
        if ch.isalpha():
            result.append(ch.upper() if idx % 2 == 0 else ch.lower())
            idx += 1
        else:
            result.append(ch)
    return ''.join(result)

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_theta_mode(text):
    """FTM Theta Mode: wraps caption in special theta-styled brackets/markers."""
    if not text:
        return text
    return f"『 {text} 』"

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_pi_mode(text, ftm_config):
    """FTM Pi Mode: applies ALL transformation modes together (the 'everything' mode)."""
    text = apply_link_remover(text)
    text = apply_alpha_mode(text)
    text = apply_course_sellers_mode(text)
    text = apply_replacer(text, ftm_config.get('replacer', {}))
    text = apply_remover(text, ftm_config.get('remover', []))
    if ftm_config.get('bullets'):
        text = apply_bullets(text)
    if ftm_config.get('delta'):
        text = apply_delta_mode(text)
    if ftm_config.get('theta'):
        text = apply_theta_mode(text)
    if ftm_config.get('watermark'):
        text = apply_watermark(text, ftm_config.get('watermark_text', ''), ftm_config.get('watermark_position', 'suffix'))
    return text

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def apply_ftm_transformations(text, ftm_config):
    """
    Main entry point. Applies all enabled FTM Manager transformations to `text`
    (a message caption or text body) according to the user's `ftm_config` dict.

    Order of operations:
      1. Pi mode (if enabled) -> applies everything and returns early
      2. Link remover
      3. Alpha mode (emoji strip)
      4. Course sellers mode
      5. Replacer
      6. Remover
      7. Bullets
      8. Delta mode
      9. Theta mode
      10. Auto numbering
      11. Watermark (always last, so it isn't mangled by other transforms)
    """
    if text is None:
        return text

    if ftm_config.get('pi'):
        return apply_pi_mode(text, ftm_config)

    if ftm_config.get('link_remover'):
        text = apply_link_remover(text)

    if ftm_config.get('alpha'):
        text = apply_alpha_mode(text)

    if ftm_config.get('course_sellers'):
        text = apply_course_sellers_mode(text)

    if ftm_config.get('replacer'):
        text = apply_replacer(text, ftm_config['replacer'])

    if ftm_config.get('remover'):
        text = apply_remover(text, ftm_config['remover'])

    if ftm_config.get('bullets'):
        text = apply_bullets(text)

    if ftm_config.get('delta'):
        text = apply_delta_mode(text)

    if ftm_config.get('theta'):
        text = apply_theta_mode(text)

    if ftm_config.get('auto_numbering'):
        current = ftm_config.get('auto_number_current', ftm_config.get('auto_number_start', 1))
        text = apply_auto_numbering(text, current)

    if ftm_config.get('watermark'):
        text = apply_watermark(text, ftm_config.get('watermark_text', ''), ftm_config.get('watermark_position', 'suffix'))

    return text

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

def should_send_text_only(ftm_config):
    return bool(ftm_config.get('text_only'))
