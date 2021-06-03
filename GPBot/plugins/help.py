from telethon import events, Button
from GPBot import Stark
from Configs import Config

btn =[
    [Button.inline("Admin", data="admin"), Button.inline("Bans", data="bans")],
    [Button.inline("Pins", data="pins"), Button.inline("Pugres", data="purges")],
    [Button.inline("Locks", data="locks"), Button.inline("Misc", data="misc")],
    [Button.inline("Chat Cleaner", data="zombies")]]

HELP_TEXT = """
Hey there! My name is *{}*.
I am an Advanced AI Powered Group Manager Bot.🔥🔥
For Help, Queries and Report Bugs Contact @CyberBoyAyushBot 🎅
*Commands Available*:
 - /start: Star The Bot
 - /help: Help Commands!!
 - /help <module name>: Send's You Info Of Particular Module.
 - /settings:
   - in PM: will send you your settings for all supported modules.
   - in a group: will redirect you to pm, with all that chat's settings.
""".format(Config.BOT_US)


@Stark.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):

    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", buttons=[
       [Button.url("Help And Commands!", "T.me/{}?start=help".format(Config.BOT_US))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Stark.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@Stark.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
