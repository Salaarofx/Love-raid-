from .. import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://graph.org/file/d05fd71077ba7bde65984.jpg"

Riz_Help = "🔥 𝗦𝗮𝗹𝗮𝗮𝗿 🔥\n\n"
 
Riz_Help += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ʀɪᴢᴏᴇʟ x sᴘᴀᴍ__\n\n"

Riz_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots\n\n"
 
Riz_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"
 
Riz_Help += f"ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ.\n\n"

Riz_Help += f"© @Notyouaagain | @Notyouaagain \n"


@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("ᴀʟʟ ᴄᴍᴅs", "https://graph.org/file/d05fd71077ba7bde65984.jpg")
        ],
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/King_salaar_op")
        ] 
        ]
        )                                                         
