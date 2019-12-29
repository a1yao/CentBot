import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "$")

histList = []

f = open("key.txt", "r")
token = f.readline()
memList = []

@client.event
async def on_ready():
    print("bot is ready")



@client.command()
async def create (ctx, member : discord.Member, debt = 0.0):
    createBed = discord.Embed(
        title = member.name,
        description = '${:,.2f}'.format(debt)
    )
    await ctx.send(embed = createBed)
    memList.append([member.name, float(debt)])

@client.command()
async def give (ctx, member : discord.Member, amount, *, reason = None):
    for i in memList:
        if i[0] == member.name:
            i[1] = i[1] + float(amount)
            # await ctx.send(f'{i[0]}, {i[1]}')
            receiver = i[0]
        if i[0] == ctx.author.name:
            i[1] = i[1] - float(amount)
            # await ctx.send(f'{i[0]}, {i[1]}')
            giver = i[0]
    formattedAmount = '${:,.2f}'.format(float(amount))
    print(formattedAmount)
    if reason == None:
        await ctx.send(f"{giver} has given ${formattedAmount} to {receiver}")
        histList.append(f"{giver} has given ${formattedAmount} to {receiver}")
    else:
        await ctx.send(f"{giver} has given ${formattedAmount} to {receiver} for {reason}")
        histList.append(f"{giver} has given ${formattedAmount} to {receiver} for {reason}")

@client.command()
async def dash (ctx):
    membed = discord.Embed(
        title = "Dashboard"
    )
    for i in memList:
        membed.add_field(name = i[0], value = '${:,.2f}'.format(i[1]), inline= False)
    await ctx.send(embed = membed)

@client.command()
async def history (ctx):
    histDes = ""
    for i in histList:
        histDes = histDes + i + "\n"
    histBed = discord.Embed(
        title = "History",
        description = histDes
    )
    await ctx.send(embed = histBed)



client.run(token)

