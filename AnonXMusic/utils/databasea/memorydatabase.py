
import config
from config import PRIVATE_BOT_MODE
from AnonXMusic.core.mongo import mongodb

channeldb = mongodb.cplaymode
commanddb = mongodb.commands
cleandb = mongodb.cleanmode
playmodedb = mongodb.playmode
playtypedb = mongodb.playtypedb
langdb = mongodb.language
authdb = mongodb.adminauth
videodb = mongodb.anonvideocalls
onoffdb = mongodb.onoffper
autoenddb = mongodb.autoend


# Shifting to memory [ mongo sucks often]
loop = {}
playtype = {}
playmode = {}
channelconnect = {}
langm = {}
pause = {}
audio = {}
video = {}
active = []
activevideo = []
command = []
cleanmode = []
nonadmin = {}
vlimit = []
maintenance = []
autoend = {}


async def is_video_allowed(chat_idd) -> str:
    chat_id = 123456
    if not vlimit:
        dblimit = await videodb.find_one({"chat_id": chat_id})
        if not dblimit:
            vlimit.clear()
            vlimit.append(config.VIDEO_STREAM_LIMIT)
            limit = config.VIDEO_STREAM_LIMIT
        else:
            limit = dblimit["limit"]
            vlimit.clear()
            vlimit.append(limit)
    else:
        limit = vlimit[0]
    if limit == 0:
        return False
    count = len(await get_active_video_chats())
    if int(count) == int(limit):
        if not await is_active_video_chat(chat_idd):
            return False
    return True
    
async def is_commanddelete_on(chat_id: int) -> bool:
    if chat_id not in command:
        return True
    else:
        return False


async def commanddelete_off(chat_id: int):
    if chat_id not in command:
        command.append(chat_id)


async def commanddelete_on(chat_id: int):
    try:
        command.remove(chat_id)
    except:
        pass
