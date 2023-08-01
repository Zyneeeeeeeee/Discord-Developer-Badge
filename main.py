import nextcord
from nextcord.ext import commands
from nextcord.shard import EventItem
from config import TOKEN

bot_version = "0.0.1"

intents = nextcord.Intents.all()
client = nextcord.Client()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot Has Connected To Discord! Logged in as {bot.user.name} - {bot.user.mention}")
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="/get"))

@bot.slash_command(guild_ids=[])
async def get(interaction: nextcord.Interaction):
    embed = nextcord.Embed(
        title='Discord Developer Badge',
        description='🎉 Bravo! 🎉 You have successfully executed the slash command. A 🏅 "Developer Badge" 🏅 will be yours soon.\n\n🤖 Discord Developer Badge Article: https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge\n\n✔ Claim your Discord Developer Badge Here: https://discord.com/developers/active-developer',
        color=nextcord.Color.green()
    )
    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)