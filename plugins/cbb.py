#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 ᴍʏ ɴᴀᴍᴇ :</b> <a href='https://t.me/Anime_all_file_store_bot'>ᵀᴴᴱ ᶜᴵᴰ ᴬᴺᴵᴹᴱ</a> \n<b>📝 ʟᴀɴɢᴜᴀɢᴇ :</b> <a href='https://python.org'>ᴾʸᵗʰᵒⁿ 3</a> \n<b>📚 ʟɪʙʀᴀʀʏ :</b> <a href='https://pyrogram.org'>ᴾʸʳᵒᵍʳᵃᵐ {__version__}</a> \n<b>🚀 ꜱᴇʀᴠᴇʀ :</b> <a href='https://heroku.com'>ᴴᵉʳᵒᵏᵘ</a> \n<b>📢 ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/THECIDANIME'>ᵀᴴᴱᶜᴵᴰᴬᴺᴵᴹᴱ</a> \n<b>🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href='tg://user?id={OWNER_ID}'>ᵀᴴᴱᶜᴵᴰᴬᴺᴵᴹᴱ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 sʜᴀᴅᴏᴡɢᴀʀᴅᴇɴ', url='https://t.me/THECIDKAGENOUSUPPORT')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


#⋗  ᴛᴇʟᴇɢʀᴀᴍ - @Codeflix_bots

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ ᴄᴏᴅᴇғʟɪx ʙᴏᴛs ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @codeflix_bots Community @Otakflix_Network </b>
