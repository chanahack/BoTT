import discord
from discord.ui import Button, View
from myserver import server_on

# เรียกใช้ server flask (เพื่อให้บอทออนไลน์บน Replit)
server_on()

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
        # สร้าง embed
        embed = discord.Embed(
            title="📨 กดเปิดลิ้ง",
            description="หากคุณต้องการีเซ็ทUID กรุณากดปุ่มด้านล่างนี้ 👇",
            color=0xFFD700  # สีทอง
        )

        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/941704661444993104/986945355474149406/df54d411305571ca5d82371db65a97ea.gif?ex=6813fa3d&is=6812a8bd&hm=f6e5cf698f7d85e55729c267403484a4967298191b174941474e23eca91d4166&"
        )
        embed.set_footer(
            text="🔗 BOT | พัฒนาโดย WINHACK",
            icon_url=
            "https://media.discordapp.net/attachments/1357719390140764211/1361633637946359940/pets.gif?ex=6813e6e5&is=68129565&hm=76dfa2d7693219a300524c451aef617c30fc964e9b7895fb4efb399cf67e7b29&=&width=350&height=350"
        )

        # ปุ่มแบบลิงก์พร้อม emoji ซองจดหมาย
        button = Button(
            label="เปิด",
            style=discord.ButtonStyle.link,
            emoji="📩",
            url="https://www.winhack.x10.mx/uid.php"  # เปลี่ยน URL ได้ตามต้องการ
        )

        view = View()
        view.add_item(button)

        await message.channel.send(embed=embed, view=view)


client.run(
    "MTM2MjEyMjUzNzA0NzE2NzAwNg.Gt0bQR.qj69vkCvSL2NlVtNZ3z0eD01Zwd_2Z5LaPZCSA")
