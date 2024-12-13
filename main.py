import telebot
from yt_dlp import YoutubeDL

# توکن ربات که از BotFather دریافت کرده‌اید
BOT_TOKEN = "8155372096:AAFcqQTekIGfZ3SWsY1V0r9fXN5jWmECh1w"
bot = telebot.TeleBot(BOT_TOKEN)

# پیام خوش‌آمدگویی
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! لینک یوتیوب خود را ارسال کنید تا فایل صوتی یا ویدیویی را دریافت کنید.")

# هندلر برای دریافت لینک
@bot.message_handler(func=lambda message: True)
def download_youtube_video(message):
    url = message.text
    bot.reply_to(message, "لطفاً صبر کنید، در حال دانلود فایل...")
    
    # پیکربندی برای دانلود ویدیو
    ydl_opts = {
        'format': 'bestaudio/best',  # بهترین کیفیت صوتی/ویدیویی
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # مسیر ذخیره‌سازی
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)
        
        # ارسال فایل به کاربر
        with open(file_name, 'rb') as file:
            bot.send_document(message.chat.id, file)
    except Exception as e:
        bot.reply_to(message, f"خطایی رخ داد: {str(e)}")

# اجرای ربات
bot.infinity_polling()
