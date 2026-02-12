import random
from telebot import types

MASA_ANS = ["عيون ماسا", "سمي يعيوني", "تفضللل", "حبيتتتت قال ماسا", "لا يناديني حد بعدك يعمري", "احبك 👈🏻👉🏻", "يعمرييييييي"]
BOT_ANS = ["بوت وش؟", "م ا س ا وين الصعب؟!!", "اسمي ماسا يا عم", "بدعي عليك تصير بوت!!!", "لا تحكي وياي", "ترا بزعل!!", "عقوبال لك"]
SALAM_ANS = ["وعليكم السلام حياك الله", "وعليكم السلام يوههه طل القمر", "وعليكم السلام نورتنا", "وعليكم السلام يعيوني", "وعليكم السلام والله زمان عنك"]
LOVE_ANS = ["احبك الله في الذي احببتني فيه 🤍", "يعمرييي", "الله يديمكم لبعض 🌸", "حبيتتتتكمم"]

def handle_responses(bot, message):
    text = message.text
    chat_id = message.chat.id
    msg_id = message.message_id

    if text == "ماسا":
        bot.set_message_reaction(chat_id, msg_id, [types.ReactionTypeEmoji("🎉")])
        bot.reply_to(message, random.choice(MASA_ANS))
    elif text == "بوت":
        bot.reply_to(message, random.choice(BOT_ANS))
    elif text == "السلام عليكم":
        bot.set_message_reaction(chat_id, msg_id, [types.ReactionTypeEmoji("❤️")])
        bot.reply_to(message, random.choice(SALAM_ANS))
    elif text == "احبك":
        bot.set_message_reaction(chat_id, msg_id, [types.ReactionTypeEmoji("❤️")])
        bot.reply_to(message, random.choice(LOVE_ANS))
    elif text == "هاي":
        bot.reply_to(message, random.choice(["هايات يعيوني", "هايي", "وش هاي قول السلام عليكم"]))
    elif text == "احلف":
        bot.reply_to(message, random.choice(["والله", "تراه يكذب مافي داعي يحلف"]))
    elif text == "باي":
        bot.reply_to(message, random.choice(["لاءءء ضل معانا بالله", "ترا الملل بدونك", "وين رايح ارجع..."]))
    elif text == "الوان":
        bot.reply_to(message, "اح اسغفر الله وش قاعدين تقولو")
    elif text in ["اح", "احا"]:
        bot.reply_to(message, "احااتتت مش احا واحد")
