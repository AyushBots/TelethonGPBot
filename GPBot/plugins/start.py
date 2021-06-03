from GPBot import Stark
from telethon import events, Button

PM_START_TEXT = """
Hello!!🥰 {} , My Name Is {} ❤️
I am an Advanced AI Powered Group Manager Bot.🔥🔥
You Can Use Me To Manage Your Groups🏆🏆
Hit /help To Check All My Commands And How I Works!!!✨✨
Join @AyushBots To Use This Bot And Frequent Updates✔️✔️
For Help, Queries and Report Bugs Contact @CyberBoyAyushBot 🎅
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help And Commands", data="help")],
        [Button.url("Updates Channel✔️", "https://telegram.me/ayushbots")]),
        [Button.url("Support🔥", "https://telegram.me/CyberBoyAyushBot")]])
       return

    if event.is_group:
       await event.reply("**I am alive 24/7!**\n\nPowered By @AyushBots")
       return
