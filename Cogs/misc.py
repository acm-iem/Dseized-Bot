import discord
from discord.ext import commands
import os
import shutil
from os import system


from discord.utils import get
import time
from discord.ext.commands import check
from mal import *

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def info(self, ctx):
        #await ctx.send(f'My ping is {round(self.latency*1000, 2)} ms!')
        await ctx.send(f'`-play\n-pause\n-resume\n-skip\n-stop\n-queue\n-userinfo\n-as anime\n-ms manga\n-invite`')

    @commands.command()
    async def invite(self, ctx):
        await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=893777032423571457&permissions=0&scope=bot')

    @commands.command()
    async def sh(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'sheeeeeeeesh :cold_face:')

    @commands.command()
    async def hi(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Hello')
    
    @commands.command()
    async def wlc(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Welcome to the server')

    @commands.command()
    async def bye(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'adios amigo')
    
    @commands.command()
    async def simp(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'stop simping')

    #@client.command()
    @commands.command(aliases = ['jdh'])
    async def jadisconnectho(self, ctx : commands.Context, user : discord.Member = None):
        if user==None:
            user=ctx.author
        member = ctx.author if not user else user
        if user.voice is None:
            await ctx.send("Andha saala")
        elif ctx.author.voice is None:
            await ctx.send("Tor baap ke emon kyalabo na shuor er bachha")
        else:
            roles = [role for role in member.roles]
            embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
            embed.set_author(name=f"Gracefully Disconnected : {member}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Deemed Undeserving By {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Undeserving Idiot :", value=member.display_name, inline="False")
            embed.add_field(name="Disgracing the Role :", value=member.top_role.mention, inline="False")
            embed.add_field(name="Unimportant user:", value=member, inline="False")
            await ctx.send(embed=embed)
            await user.move_to(None)
    

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name, inline="False")
        embed.add_field(name="Created On:", value=member.created_at.strftime("%a, %d, %B, %Y, %I:%M %p UTC"), inline="False")
        embed.add_field(name="Joined On:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I:%M %p UTC"), inline="False")
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline="False")
        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline="False")
        embed.add_field(name="Bot:", value=member.bot, inline="False")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @commands.command(aliases = ['as'])
    async def animesearch(self, ctx, *, an: str, ):
        start = time.time()
        search = AnimeSearch(f"{an}") # Search for "cowboy bebop"
        id_ = search.results[0].mal_id
        url_ = search.results[0].url
        img_url = search.results[0].image_url
        ti = search.results[0].title
        sy = search.results[0].synopsis
        ty = search.results[0].type
        ep = search.results[0].episodes
        sc = search.results[0].score
        anime = Anime(id_)
        st = anime.status
        ai = anime.aired
        ra = anime.rank
        embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=img_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Anime Name:", value=ti, inline="False")
        embed.add_field(name="Synopsis:", value=sy, inline="False")
        embed.add_field(name="Contd:", value=url_, inline="False")
        embed.add_field(name="Type", value=ty, inline="False")
        embed.add_field(name="Episodes:", value=ep, inline="False")
        embed.add_field(name="Score:", value=sc, inline="False")
        embed.add_field(name="Status:", value=st, inline="False")
        embed.add_field(name="MAL_ID:", value=id_, inline="False")
        embed.add_field(name="Aired:", value=ai, inline="False")
        embed.add_field(name="Rank:", value=ra, inline="False")
        await ctx.send(embed=embed)
        end = time.time()
        await ctx.send(f"`Time taken: {round(end-start, 2)} seconds`")

    @commands.command(aliases = ['ms'])
    async def mangasearch(self, ctx, *, an: str, ):
        start = time.time()
        search = MangaSearch(f"{an}") # Search for "cowboy bebop"
        id_ = search.results[0].mal_id
        url_ = search.results[0].url
        img_url = search.results[0].image_url
        ti = search.results[0].title
        sy = search.results[0].synopsis
        ty = search.results[0].type
        vol = search.results[0].volumes
        sc = search.results[0].score
        manga = Manga(id_)
        st = manga.status
        ra = manga.rank
        ch = manga.chapters
        vol = manga.volumes
        embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=img_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Manga Name:", value=ti, inline="False")
        embed.add_field(name="Synopsis:", value=sy, inline="False")
        embed.add_field(name="Contd:", value=url_, inline="False")
        embed.add_field(name="Type", value=ty, inline="False")
        embed.add_field(name="Episodes:", value=vol, inline="False")
        embed.add_field(name="Score:", value=sc, inline="False")
        embed.add_field(name="Status:", value=st, inline="False")
        embed.add_field(name="MAL_ID:", value=id_, inline="False")
        embed.add_field(name="Chapters:", value=ch, inline="False")
        embed.add_field(name="Volumes:", value=vol, inline="False")
        embed.add_field(name="Rank:", value=ra, inline="False")
        await ctx.send(embed=embed)
        end = time.time()
        await ctx.send(f"`Time taken: {round(end-start, 2)} seconds`")


    


    @commands.command()
    async def say(self, ctx, say: str, id: int):
        channel = self.bot.get_channel(id)
        await ctx.channel.purge(limit=1)
        await channel.send(f"{say}")



def setup(client):
    client.add_cog(misc(client))