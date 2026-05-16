# Alex-MD Command Handler (Python Version)

import random
import datetime

commands = {}

# Helper function to register commands
def command(name, description, category):
    def decorator(func):
        commands[name] = {
            "name": name,
            "description": description,
            "category": category,
            "handler": func
        }
        return func
    return decorator


# ===== GENERAL COMMANDS =====

@command("ping", "Check if bot is online", "general")
async def ping(sock, sender, args):
    await sock.send_message(sender, "🏓 Pong! Bot is active!")


@command("owner", "Show owner information", "general")
async def owner(sock, sender, args):
    owner_name = "〖ᴹᴿ•ᴀʟᴇ᥊᭄𓋆 ⁰⁰³"
    msg = f"👤 Owner: {owner_name}\n\n🤖 Bot: Alex-MD\n✨ Status: Online"
    await sock.send_message(sender, msg)


@command("info", "Bot information", "general")
async def info(sock, sender, args):
    msg = """
╔════════════════════════════════╗
║        Alex-MD BOT INFO        ║
╠════════════════════════════════╣
║ 🤖 Bot Name: Alex-MD
║ 👤 Owner: 〖ᴹᴿ•ᴀʟᴇ᥊᭄𓋆 ⁰⁰³
║ 📱 Platform: WhatsApp
║ 🔧 Framework: Python Bot
║ 💻 Language: Python
║ ⚡ Status: Online
║ 📅 Version: 1.0.0
╚════════════════════════════════╝
"""
    await sock.send_message(sender, msg)


# ===== GAME COMMANDS =====

@command("dice", "Roll a dice", "games")
async def dice(sock, sender, args):
    result = random.randint(1, 6)
    emojis = ["", "✨", "⭐", "🌟", "💫", "⚡", "🔥"]
    msg = f"🎲 You rolled: {result}\n\n{emojis[result] * result}"
    await sock.send_message(sender, msg)


@command("coin", "Flip a coin", "games")
async def coin(sock, sender, args):
    result = random.choice(["Heads", "Tails"])
    await sock.send_message(sender, f"🪙 Result: {result}")


@command("rps", "Rock Paper Scissors", "games")
async def rps(sock, sender, args):
    choices = ["rock", "paper", "scissors"]

    if not args or args[0].lower() not in choices:
        await sock.send_message(sender, "❌ Usage: .rps <rock|paper|scissors>")
        return

    user = args[0].lower()
    bot = random.choice(choices)

    if user == bot:
        result = "Draw!"
    elif (user == "rock" and bot == "scissors") or \
         (user == "paper" and bot == "rock") or \
         (user == "scissors" and bot == "paper"):
        result = "You won! 🎉"
    else:
        result = "I won! 😎"

    msg = f"You: {user}\nBot: {bot}\n\n{result}"
    await sock.send_message(sender, msg)


# ===== UTILITY COMMANDS =====

@command("time", "Current time", "utility")
async def time_cmd(sock, sender, args):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await sock.send_message(sender, f"🕐 Time: {now}")


@command("date", "Current date", "utility")
async def date_cmd(sock, sender, args):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    await sock.send_message(sender, f"📅 Date: {today}")


@command("calc", "Simple calculator", "utility")
async def calc(sock, sender, args):
    if not args:
        await sock.send_message(sender, "🧮 Usage: .calc 5+5")
        return

    try:
        result = eval("".join(args))
        await sock.send_message(sender, f"🧮 Result: {result}")
    except:
        await sock.send_message(sender, "❌ Invalid calculation")


@command("quote", "Random quote", "utility")
async def quote(sock, sender, args):
    quotes = [
        "The only way to do great work is to love what you do.",
        "Innovation distinguishes between a leader and a follower.",
        "Life is what happens when you're busy making plans."
    ]
    await sock.send_message(sender, random.choice(quotes))


# ===== HELP FUNCTION =====

def get_command_help():
    return """
📌 GENERAL:
• .ping
• .owner
• .info

🎮 GAMES:
• .dice
• .coin
• .rps

🔧 UTILITY:
• .time
• .date
• .calc
• .quote
"""
