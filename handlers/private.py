from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Jason](https://t.me/ImJanindu).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🛠", url="https://github.com/Hexor752/SankiiPublicBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 ɢʀᴏᴜᴘ", url="https://t.me/SankiiPublic"
                    ),
                    InlineKeyboardButton(
                        "🔊 ᴏᴡɴᴇʀ", url="https://t.me/its_Hexor"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ɢʀᴏᴜᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ᴏɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 ᴏᴡɴᴇʀ", url="https://t.me/Its_Hexor")
                ]
            ]
        )
   )

