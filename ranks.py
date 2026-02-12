import telebot
import json
import os

# ملف تخزين الرتب
RANKS_FILE = 'ranks_data.json'

def load_ranks():
    if os.path.exists(RANKS_FILE):
        with open(RANKS_FILE, 'r', encoding='utf-8') as f:
            try: return json.load(f)
            except: return {}
    return {}

def save_ranks(data):
    with open(RANKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_user_rank(chat_id, user_id):
    ranks = load_ranks()
    chat_id, user_id = str(chat_id), str(user_id)
    if chat_id in ranks and user_id in ranks[chat_id]:
        return ranks[chat_id][user_id]
    return "عضو"

def handle_ranks(bot, message):
    chat_id = str(message.chat.id)
    user_id = str(message.from_user.id)
    text = message.text

    # أمر رفع مطور (للمطور الأساسي فقط)
    if text == "رفع مطور" and message.reply_to_message:
        target_id = str(message.reply_to_message.from_user.id)
        if int(user_id) == 8436415733: # ايديكِ أنتِ
            ranks = load_ranks()
            if chat_id not in ranks: ranks[chat_id] = {}
            ranks[chat_id][target_id] = "مطور"
            save_ranks(ranks)
            bot.reply_to(message, f"✅ تم رفع {message.reply_to_message.from_user.first_name} مطور في البوت.")
        else:
            bot.reply_to(message, "❌ هذا الأمر للمطور الأساسي فقط.")

    # أمر تنزيل رتبة
    if text == "تنزيل" and message.reply_to_message:
        target_id = str(message.reply_to_message.from_user.id)
        ranks = load_ranks()
        if chat_id in ranks and target_id in ranks[chat_id]:
            del ranks[chat_id][target_id]
            save_ranks(ranks)
            bot.reply_to(message, "✅ تم تنزيل المستخدم من رتبته.")

    # أمر عرض رتبتي
    if text == "رتبتي":
        rank = get_user_rank(chat_id, user_id)
        bot.reply_to(message, f"👤 رتبتك هي: **{rank}**")
          
