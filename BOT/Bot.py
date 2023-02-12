import discord
from discord.ext import commands
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from settings import settings # file with dictionary where lies my personal information (for example: telegram_token, my_id, email_password)

def send_telegram(text: str):
    token = settings["token_telegram"] # token of your telegram bot
    url = "https://api.telegram.org/bot"
    my_id = settings["my_id"] # my telegram id
    url = url + token
    method = url + "/sendMessage"

    message = requests.post(method, data={"chat_id": my_id, "text": text})

    if message.status_code != 200:
        raise Exception("post_text error")
    
    send_email(text)

def send_email(text):
    sms = MIMEMultipart()
    message = text
    password = settings["email_password"] # your password of an application that does not support two-step verification
    sms["From"] = settings["From"] # your email
    sms["To"] = settings["To"] # email of recipient
    sms["Subject"] = settings["Subject"] # message theme
    sms.attach(MIMEText(message, "plain"))
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()
    server.login(sms["From"], password)
    server.sendmail(sms["From"], sms["To"], sms.as_string())
    server.quit()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "", intents = intents)
key_words = ["<@1027634774031990794>", "<@1027634774031990794>,"] # my discord id

@bot.event
async def on_message(our_message):
    for content in our_message.content.split(" "):
        for word in key_words:
            if content.lower() == word:
                text = str(f"{our_message.author}, mentioned your on server: {our_message.guild.name}, in channel: {our_message.channel}\n{our_message.author}'s status: {our_message.author.status}\nMessage:\n {our_message.content}\nTime: {our_message.created_at}")
                send_telegram(text)

bot.run(settings["token_discord"]) # token of your discord bot