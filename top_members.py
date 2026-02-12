import json
import os

def load_stats():
    if os.path.exists('stats.json'):
        with open('stats.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def handle_top(bot, message):
    chat_id = str(message.chat.id)
    text = message.text

    if text in ["المتفاعلين", "التاق", "اكثر تفاعل"]:
        stats = load_stats()
        chat_stats = stats.get(chat_id, {})

        if not chat_stats:
            bot.reply_to(message, "⚠️ لسه ما فيه تفاعل بالجروب، ورونا همتكم!")
            return

        # ترتيب المستخدمين حسب عدد الرسائل (من الأكبر للأصغر)
        # نأخذ أول 10 فقط
        sorted_users = sorted(chat_stats.items(), key=lambda x: x[1], reverse=True)[:10]

        reply_text = "🏆 **قائمة أكثر المتفاعلين في الجروب:**\n\n"
        
        icons = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        
        for index, (uid, count) in enumerate(sorted_users):
            try:
                # محاولة جلب اسم الشخص من التليجرام
                user_info = bot.get_chat_member(chat_id, int(uid)).user
                name = user_info.first_name
            except:
                name = f"مستخدم ({uid})"
            
            reply_text += f"{icons[index]} {name} ← `{count}` رسالة\n"
        
        reply_text += "\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\استمروا 🌸🎀 !"
        bot.send_message(message.chat.id, reply_text, parse_mode="Markdown")
      
