from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def mines(ctx, round_id):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        await ctx.send("Invalid round id")
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:', ':bomb:'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = ":gem: "
        elif a == 2:
            mine2 = ":gem: "
        elif a == 3:
            mine3 = ":gem: "
        elif a == 4:
            mine4 = ":gem: "
        elif a == 5:
            mine5 = ":gem: "
        elif a == 6:
            mine6 = ":gem: "
        elif a == 7:
            mine7 = ":gem: "
        elif a == 8:
            mine8 = ":gem: "
        if b == 9:
            mine9 = ":gem: "
        elif b == 10:
            mine10 = ":gem: "
        elif b == 11:
            mine11 = ":gem: "
        elif b == 12:
            mine12 = ":gem: "
        elif b == 13:
            mine13 = ":gem: "
        if c == 14:
            mine14 = ":gem: "
        elif c == 15:
            mine15 = ":gem: "
        elif c == 16:
            mine16 = ":gem: "
        elif c == 17:
            mine17 = ":gem: "
        if d == 18:
            mine18 = ":gem: "
        elif d == 19:
            mine19 = ":gem: "
        elif d == 20:
            mine20 = ":gem: "
        elif d == 21:
            mine21 = ":gem: "
        elif d == 22:
            mine22 = ":gem: "
        elif d == 23:
            mine23 = ":gem: "
        elif d == 24:
            mine24 = ":gem: "
        elif d == 25:
            mine25 = ":gem: "
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(65, 92))
        em = discord.Embed(color=0xB87DFF)
        em.set_footer(text="There is no 💯")
        em.add_field(name="Bloxflip Mines predictor",value=row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "**Accuracy**" + "\n" + info +"%")
        await ctx.reply(embed=em)


bot.run("Your bot token here")