# this program is cursed, please leave while you still can
# ok the above isnt so true anymore im starting to find uwuBot very cute oh god what am i doing
# made by smubear do not steal
import random
import discord

#SETTINGS
uwus = ["uwu", "owo", "0w0", "qwq"]
sad_faces = [":(", ":frowning:", ":c", ":<", ":{", ":[", "'^'", "):"]

client = discord.Client()


@client.event
async def on_ready():
    print("Teh bot is ready")
    await client.change_presence(game=discord.Game(name="up and wunning"))


@client.event
async def on_message(message):
    # check to make sure the message being checked isnt from the bot
    if message.author == client.user:
        return
    check = message.content[:3].lower()
    if "uwu" in check:
        print("OWO! uwuBot requested by {}".format(message.author))
        reply = uwu(message.content[3:])
        await client.send_message(message.channel, reply)
        print(reply)

    # this elif was inspired by NeoHaru26
    elif check.lower() in uwus:
        reply = uwu("")
        await client.send_message(message.channel, reply)
        print("uwuBot has replied to {}: '{}'".format(message.author, reply))

    elif check.lower() in sad_faces:
        author = str(message.author)[:-5]  # this removes the discord tag
        reply = "dont be sad {}, im hewe fow u uwu".format(uwu(author, False))
        await client.send_message(message.channel, reply)
        print("{} was sad, uwuBot cheered them up.".format(message.author))


def main():
    print_header()
    while True:
        uwu_text = input("what text awe you putting in\n>>>").strip().lower()
        print(uwu(uwu_text))
        print("--------------------------")


def print_header():
    print("--------------------------")
    print("     uwu genewatow")
    print("(please leave this program its so bad)")
    print("--------------------------")


# cursed begins after this line
def uwu(text, mod = True):
    modifiers = ["uwu", "owo", "UWU", "OWO"]
    while text.find("l") != -1:
        spot = text.find("l")
        text_1 = text[:spot]
        text_2 = text[spot+1:]
        text = "{}w{}".format(text_1, text_2)
    while text.find("r") != -1:
        spot = text.find("r")
        text_1 = text[:spot]
        text_2 = text[spot+1:]
        text = "{}w{}".format(text_1, text_2)
    while text.find("th") != -1:
        spot = text.find("th")
        text_1 = text[:spot]
        text_2 = text[spot+2:]
        text = "{}d{}".format(text_1, text_2)
    while text.find("st") != -1:
        spot = text.find("st")
        text_1 = text[:spot]
        text_2 = text[spot+2:]
        text = "{}sht{}".format(text_1, text_2)
    while text.find("hot") != -1:
        spot = text.find("hot")
        text_1 = text[:spot]
        text_2 = text[spot+3:]
        text = "{}hawt{}".format(text_1, text_2)
    if mod:
        return "{} {}".format(text.lower(), random.choice(modifiers))
    else:
        return text.lower()


if __name__ == "__main__":
    # main()
    client.run("NTM5NTcyOTM1MjkyMjIzNDk5.DzEVCQ.5GYhkZcZUd88JQAKRtRJ7mYh3Ss")
