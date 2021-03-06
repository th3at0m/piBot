# piBot
A functional Discord bot for your Raspberry Pi.

# How to set up
1. On a terminal run ```sudo apt update``` and ```sudo apt install git python3-dotenv```

2. Go to [Discord Developer Portal](https://discord.com/developers/applications) and create an Application, then a Bot.

3. Regenerate your token (**Do NOT share your token with anyone!**)

4. On the terminal run ```git clone https://github.com/th3at0m/piBot.git && cd piBot```

5. Run ```mv .env.example .env``` and edit the `.env` file with your Bot Token and your User ID.

6. Run ```sudo pip3 install discord-py-interactions```

7. Run ```python3 main.py``` and you're good to go!

# Commands
```/temp``` ---> Shows your Pi temperature


```/shutdown``` ---> Reboots or halts your Pi


```/eval``` ---> Runs a command on your Pi

# License & Credits
piBot is protected by AGPL v3 license.

piBot uses [interactions.py](https://discord-py-slash-command.readthedocs.io)