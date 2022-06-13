# (c) 2022 th3atom
# Protected by AGNUv3
# piBot: A Discord bot for managing your Raspberry Pi

# Load Modules
import interactions, subprocess, os
from dotenv import load_dotenv

# Initialize Bot and .env file
load_dotenv()
UID = os.getenv("UID")
TOKEN = os.getenv("TOKEN")
bot = interactions.Client(token=TOKEN)

# buttons and rows
reboot = interactions.Button(
    style=interactions.ButtonStyle.DANGER,
    label="Reboot",
    custom_id="reb"
)

halt = interactions.Button(
    style=interactions.ButtonStyle.DANGER,
    label="Halt",
    custom_id="hal"
)

shucanc = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Cancel",
    custom_id="shucancbut"
)

shurow = interactions.ActionRow(
    components=[reboot, halt, shucanc]
)

@bot.command(
    name="temp",
    description="Outputs temperature of the Pi"
)
async def temp(ctx: interactions.CommandContext):
    if ctx.user.id == UID:
        cout = subprocess.run(["/usr/bin/vcgencmd", 'measure_temp'], stdout=subprocess.PIPE)
        cout = cout.stdout
        cout = cout.decode('utf-8')
        cout = cout[5:]
        await ctx.send("🌡️ Temperature: " + cout)
    else:
        pass

@bot.command(
    name="shutdown",
    description="Halts or reboots the Pi",
)
async def shutdown(ctx: interactions.CommandContext):
    if ctx.user.id == UID:
        msg1 = await ctx.send("What would you like to do?", components=shurow, ephemeral=True)
    else:
        pass

@bot.component("reb")
async def button_response(ctx):
    if ctx.user.id == UID:
        await ctx.edit("⌛ Rebooting...", components=None)
        os.system("reboot")
    else:
        pass

@bot.component("hal")
async def button_response(ctx):
    if ctx.user.id == UID:
        await ctx.edit("⌛ Halting the Pi...", components=None)
        os.system("halt")
    else:
        pass

@bot.component("shucancbut")
async def button_response(ctx):
    if ctx.user.id == UID:
        await ctx.edit("Interaction cancelled!", components=None)
    else:
        pass

@bot.command(
    name="eval",
    description="Runs a command on the Pi",
    options = [
        interactions.Option(
            name="command",
            description="Command to run",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)

try:
    bot.start()
except KeyboardInterrupt:
    print("Shutting down bot...")
    exit()