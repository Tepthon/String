from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
اهلا {}

إذا كنت لا تثق بهذا الروبوت ،
1) لا تقرأ هذه الرسالة
2) حظر البوت أو حذف الدردشة

يعمل هذا الروبوت لمساعدتك في الحصول على استخراج الجلسة عبر Bot. توصيات إذا كنت تريد أن تأخذ استخراج استخدم حساب آخر ،
هذا البوت بواسطة @Tepthon
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🖥️|بدء استخراج الجلسة", callback_data="generate")],
        [InlineKeyboardButton(text="🏠|الصفحة الرئيسية", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🖥️|بدء استخراج الجلسة", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🖥️|بدء استخراج الجلسة", callback_data="generate")],
        [InlineKeyboardButton("قناة السورس", url="https://t.me/Tepthon")],
        [
            InlineKeyboardButton("كيف تستعملني ❓", callback_data="help"),
            InlineKeyboardButton("حول", callback_data="about")
      ],
        [InlineKeyboardButton("معلومات البوت الاخرى", url="https://t.me/Tepthon")],
    ]


    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - حول هذا البوت 
/help - لمساعدتك على استخدام البوت 
/start - بدء البوت 
/generate - ابدأ بتوليد الجلسة
/cancel - إلغاء 
/restart - إعادة تشغيل البوت 
"""

    # About Message
    ABOUT = """
**About This Bot** 

روبوت برقية لاسترداد جلسات سلسلة pyrograms و telethon بواسطة @ P17_12

Group Support : [Tepthon](https://t.me/Tepthon_Support)

برمجة البوت : [Pyrogram](docs.pyrogram.org)

لغة البوت : [Python](www.python.org)

Developer : @P17_12
    """
