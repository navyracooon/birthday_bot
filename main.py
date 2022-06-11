import os
from flask import Flask

from linebot import LineBotApi
from linebot.models import TextSendMessage

from birthday import Birthday

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
GROUP_ID = os.environ["GROUP_ID"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

Me = Birthday(0)
birthdayPeopleList = []
includeMessage =""

for i in range(Me.len):
    friend = Birthday(i)
    if friend.is_today_birthday():
        birthdayPeopleList.append(friend.name)

for i in birthdayPeopleList:
    if i != birthdayPeopleList[-1]:
        includeMessage += i + "さんと"
    else:
        includeMessage += i + "さん"

outputMessage = "今日は{}の誕生日です！\nおめでとうございます！🎉🎉".format(includeMessage)

if len(birthdayPeopleList) != 0:
    line_bot_api.push_message(GROUP_ID, TextSendMessage(text=outputMessage))
