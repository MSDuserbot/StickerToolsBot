from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
 ʜᴇʏ[👋](https://telegra.ph/file/57873ee2279555866f4c9.jpg) {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜᴜs ʙᴏᴛ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ
1) sᴛɪᴄᴋᴇʀs ᴛᴏ ɪᴍᴀɢᴇ
2) ɪᴍᴀɢᴇ ᴛᴏ sᴛɪᴄᴋᴇʀ

sᴇɴᴅ ᴍᴜʟᴛɪᴘʟᴇ ɪᴍᴀɢᴇs ᴏʀ sᴛɪᴄᴋᴇʀs ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴛʜᴇ sᴀᴍᴇ.

ʙʏ @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/StarkBots/7")],
        [InlineKeyboardButton(text="ʜᴏᴍᴇ", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("ᴅᴇᴠ", url="https://t.me/StarkBots/7")
        ],
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
ʏᴏᴜ ʀᴇᴀʟʟʏ ɴᴇᴇᴅ ʜᴇʟᴘ ?!?!?!?!

1) Sᴇɴᴅ Sᴛɪᴄᴋᴇʀ ᴛᴏ ɢᴇᴛ ɪᴍᴀɢᴇ
2) Sᴇɴᴅ ɪᴍᴀɢᴇ ᴛᴏ ɢᴇᴛ Sᴛɪᴄᴋᴇʀ

ɴᴏᴛᴇ : ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ɪᴍᴀɢᴇs ᴏʀ sᴛɪᴄᴋᴇʀs ᴏʀ ʙᴏᴛʜ ᴛᴏɢᴇᴛʜᴇʀ ᴀᴛ ᴏɴᴄᴇ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴡɪᴛʜ sᴀᴍᴇ sᴘᴇᴇᴅ ᴀɴᴅ ᴀᴄᴄᴜʀᴀᴄʏ.

ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. ᴋᴇᴇᴘ ᴛʀᴀᴄᴋ ʙʏ ᴊᴏɪɴɪɴɢ in development. Keep track by joining @StarkBots.
    """

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ @StarkBots

Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/StarkBotsIndustries/StickerToolsBot)

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

ᴅᴇᴠʟᴏᴘᴇʀ : @StarkProgrammer

Sᴜᴘᴘᴏʀᴛ : [ᴛᴀᴍɪʟ sᴜᴘᴘᴏʀᴛ]

ᴜᴘᴅᴀᴛᴇs : [ᴛᴀᴍɪʟʙᴏᴛs]



    """
