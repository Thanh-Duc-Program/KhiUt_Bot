from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Thay thế YOUR_BOT_TOKEN bằng token của bot bạn
updater = Updater("6768783456:AAEeE-pp7dMwzAzDr5efU9KfQnC_zEjimfY")

# Biến global để lưu trữ tên ban đầu của nhóm
initial_topic = ""

# Biến global để theo dõi trạng thái icon
current_icon = "🦊"

def on_icon(update: Update, context: CallbackContext) -> None:
    global initial_topic
    global current_icon

    # Kiểm tra lệnh là /on hay /off
    command = update.message.text.split()[0]  # Lấy từ đầu đến khoảng trắng đầu tiên

    if command == '/on':
        # Nếu là lệnh /on, cập nhật trạng thái icon thành Cáo 🦊
        current_icon = "🦊"
    elif command == '/off':
        # Nếu là lệnh /off, cập nhật trạng thái icon thành Lười 🦥
        current_icon = "🦥"
    elif command == '/saveID':
        # Nếu là lệnh /saveID, lưu tên nhóm vào biến initial_topic
        initial_topic = update.message.chat.title
        update.message.reply_text(f"Group name saved: {initial_topic}")
        return
    else:
        # Nếu lệnh không hợp lệ, thông báo cho người dùng
        update.message.reply_text("Invalid command. Use /on, /off, or /saveID.")
        return

    # Gửi yêu cầu cập nhật tên topic lên Telegram với icon mới và tên nhóm
    context.bot.setChatTitle(chat_id=update.message.chat_id, title=f"{current_icon} {initial_topic}")

    # Thông báo cho người dùng là tên topic đã được thay đổi
    update.message.reply_text(f"Topic updated to: {current_icon} {initial_topic}")

# Đăng ký lệnh /on, /off, và /saveID
updater.dispatcher.add_handler(CommandHandler("on", on_icon))
updater.dispatcher.add_handler(CommandHandler("off", on_icon))
updater.dispatcher.add_handler(CommandHandler("saveID", on_icon))

# Khởi động bot
updater.start_polling()
updater.idle()
