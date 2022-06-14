# (c) 2022 th3atom
# Protected by AGNUv3
# piBot: A Discord bot for managing your Raspberry Pi

# Load Modules
import interactions, subprocess, os
import random
import string
from dotenv import load_dotenv
import time

BASEDIR = os.path.abspath(os.path.dirname(__file__))

print("√ Booting up bot...")

# Initialize Bot and .env file
load_dotenv(os.path.join(BASEDIR, '../.env'))
UID = os.getenv("UID")
TOKEN = os.getenv("TOKEN")
VER = os.getenv("VER")
print("Running on piBot v" + VER)
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
        os.system("sudo reboot")
    else:
        pass

@bot.component("hal")
async def button_response(ctx):
    if ctx.user.id == UID:
        await ctx.edit("⌛ Halting the Pi...", components=None)
        os.system("sudo halt")
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

async def eval(ctx: interactions.CommandContext, command: str):
    if ctx.user.id == UID:
        try:
            filename = "./tmp/eval.log"
            out = open(filename, "w")
            subprocess.run(command.split(), stdout=out, stderr=out)
            out.close()
            voap = open(filename)
            data = voap.read()
            await ctx.send("```" + data + "```", ephemeral=False)
        except FileNotFoundError as err:
            await ctx.send("❌ Command or file not found.", ephemeral=False)
            print(err)
    else:
        pass

try:
    bot.start()
except KeyboardInterrupt:
    print("Shutting down bot...")
    exit()