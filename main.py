import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from random import randint

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



# Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="<b>Let's play Rock Paper Scissors!</b>\n" + \
                                   "Choose one of the options in the menu.\n/start | /rock | /paper | /scissors", 
                                   parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)

async def rock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_choice = randint(1, 3)

    match bot_choice:
        case 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Rock 🪨</b>\n" + \
                                        "Bot's Choice: <b>Rock 🪨</b>\nResult: <b>Tie!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)
        case 2:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Rock 🪨</b>\n" + \
                                        "Bot's Choice: <b>Paper 📃</b>\nResult: <b>Bot wins!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)  
        case 3:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Rock 🪨</b>\n" + \
                                        "Bot's Choice: <b>Scissors ✂️</b>\nResult: <b>You win!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)


async def paper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_choice = randint(1, 3)

    match bot_choice:
        case 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Paper 📃</b>\n" + \
                                        "Bot's Choice: <b>Rock 🪨</b>\nResult: <b>You win!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)
        case 2:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Paper 📃</b>\n" + \
                                        "Bot's Choice: <b>Paper 📃</b>\nResult: <b>Tie!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)  
        case 3:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Paper 📃</b>\n" + \
                                        "Bot's Choice: <b>Scissors ✂️</b>\nResult: <b>Bot wins!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)

async def scissors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_choice = randint(1, 3)

    match bot_choice:
        case 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Scissors ✂️</b>\n" + \
                                        "Bot's Choice: <b>Rock 🪨</b>\nResult: <b>Bot wins!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)
        case 2:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Scissors ✂️</b>\n" + \
                                        "Bot's Choice: <b>Paper 📃</b>\nResult: <b>You win!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)  
        case 3:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Your Choice: <b>Scissors ✂️</b>\n" + \
                                        "Bot's Choice: <b>Scissors ✂️</b>\nResult: <b>Tie!</b>", 
                                        parse_mode='HTML', protect_content=True, reply_to_message_id=update.message.id)

# Any other message 
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="<b>You sent an invalid message</b>\n" + \
                                    "Please use only the commands in the menu" + \
                                    "\n/start | /rock | /paper | /scissors", 
                                    protect_content=True,
                                    parse_mode='HTML',
                                    reply_to_message_id=update.message.id)




if __name__ == '__main__':
    application = ApplicationBuilder().token('__token__').build()
    
    start_handler = CommandHandler('start', start)
    rock_handler = CommandHandler('rock', rock)
    paper_handler = CommandHandler('paper', paper)
    scissors_handler = CommandHandler('scissors', scissors)
    echo_handler = MessageHandler(filters.ALL, echo)

    application.add_handler(start_handler)
    application.add_handlers((rock_handler, paper_handler, scissors_handler))
    application.add_handler(echo_handler)
    
    application.run_polling()