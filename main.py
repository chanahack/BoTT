import discord
from discord.ui import Button, View
from myserver import server_on
import os
from dotenv import load_dotenv

# ✅ โหลด Token จากไฟล์ .env
load_dotenv()
TOKEN = os.getenv("")

# ☁️ เปิดเซิร์ฟเวอร์ Flask (สำหรับให้บอทออนไลน์ต่อเนื่องใน Replit/Render)
server_on()

# 🔧 เปิด intents สำหรับอ่านข้อความ
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!win":
        embed = discord.Embed(
            title="📨 กดเปิดลิ้ง",
            description="หากคุณต้องการีเซ็ทUID กรุณากดปุ่มด้านล่างนี้ 👇",
            color=0xFFD700
        )

        embed.set_image(
            url="https://cdn.discordapp.com/attachments/941704661444993104/986945355474149406/df54d411305571ca5d82371db65a97ea.gif"
        )
        embed.set_footer(
            text="🔗 BOT | พัฒนาโดย WINHACK",
            icon_url="https://media.discordapp.net/attachments/1357719390140764211/1361633637946359940/pets.gif"
        )

        button = Button(
            label="เปิด",
            style=discord.ButtonStyle.link,
            emoji="📩",
            url="https://www.winhack.x10.mx/uid.php"
        )

        view = View()
        view.add_item(button)

        await message.channel.send(embed=embed, view=view)

# ✅ ใช้ Token จาก ENV
if TOKEN:
    client.run(TOKEN)
else:
    print("❌ ไม่พบ Token ใน .env กรุณาตรวจสอบว่าได้ตั้งค่า DISCORD_TOKEN แล้ว")
