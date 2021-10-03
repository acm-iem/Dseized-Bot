import uwuify
from discord.ext import commands
import requests


class uwu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uwu(self, ctx, say: str):
        await ctx.channel.purge(limit=1)
        flags = uwuify.SMILEY | uwuify.YU
        print(f"{say}")
        conv = uwuify.uwu(f"{say}", flags=flags)
        await ctx.send(conv)
    @commands.command()
    async def meme(self, ctx, temp: str, top: str, bot: str)
        url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"
        querystring = {"top":top,"bottom":bot,"meme":temp,"font_size":"50","font":"Impact"}

        headers = {
            'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
            'x-rapidapi-key': "23f2517700msh6142344059b059ep1838a6jsn0f069946c950"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        

def setup(client):
    client.add_cog(uwu(client))