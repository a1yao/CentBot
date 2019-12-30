import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "$")

histList = []

f = open("key.txt", "r")
token = f.readline()
memList = []
fixed = ""

def fixSign(val):
    if val >= 0:
        fixed = '${:,.2f}'.format(val)
    if val < 0:
        fixed = '-${:,.2f}'.format(val * -1)
    return(fixed)



@client.event
async def on_ready():
    print("bot is ready")



@client.command()
async def create (ctx, member : discord.Member, debt = 0.0):
    if debt >= 0:
        temp = '${:,.2f}'.format(debt)
    if debt < 0:
        temp = '-${:,.2f}'.format(debt*-1)
    createBed = discord.Embed(
        title = member.name,
        description = temp
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
    if float(amount) >= 0:
        temp3 = '${:,.2f}'.format(float(amount))
    if float(amount) < 0:
        temp3 = '-${:,.2f}'.format(float(amount)*-1)
    if reason == None:
        await ctx.send(f"{giver} has given {temp3} to {receiver}")
        histList.append(f"{giver} has given {temp3} to {receiver}")
    else:
        await ctx.send(f"{giver} has given {temp3} to {receiver} for {reason}")
        histList.append(f"{giver} has given {temp3} to {receiver} for {reason}")

@client.command()
async def dash (ctx):
    membed = discord.Embed(
        title = "Dashboard"
    )
    for i in memList:
        if i[1] >= 0:
            temp2 = '${:,.2f}'.format(i[1])
        if i[1] < 0:
            temp2 = '-${:,.2f}'.format(i[1]*-1)
        membed.add_field(name = i[0], value = temp2, inline= False)
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

