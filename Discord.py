import discord
from discord.ext import commands
from googlesearch import search
from math import *
from statistics import*
from wikipedia import *
import wikipedia
import math as ma
import statistics as s
import googlesearch
import youtube_dl
import os
if True:
    client=commands.Bot(command_prefix="'")
    @client.event
    async def on_ready():
        print("Prepared")
    censor=[] 
    da={}
    re=[0,"OK"]
    @client.command()
    async def connect_music(ctx):
        voiceChannel=discord.utils.get(ctx.guild.voice_channels,name="vc")
        await voiceChannel.connect()
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
        await ctx.send("Connected")
    @client.command()
    async def url_song(ctx,url:str):
        song=os.path.isfile("song.mp3")
        try:
             if song:
                 os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait or use stop")
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)

        ydl_op={'format':'bestaudio/best','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'320',}],}
        with youtube_dl.YoutubeDL(ydl_op) as ydl:
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file,"song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    @client.command()
    async def play(ctx):
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    @client.command()
    async def leave(ctx):
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
        await voice.disconnect()
    @client.command()
    async def pause(ctx):
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
        voice.pause()
    @client.command()
    async def resume(ctx):
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
        voice.resume()
    @client.command()
    async def stop(ctx):
        voice=discord.utils.get(client.voice_clients,guild=ctx.guild)
        voice.stop()
    @client.command()
    async def clear(ctx,*,text):
    	req()
    	await ctx.channel.purge(limit=1)
    	if str(text)==re[1]:    		
    		await ctx.channel.purge(limit=100000)
    	else:
    		await ctx.send("Wrong password")
    @client.command(aliases=['w'])
    async def wikipedia(ctx,*,text):
    	req()
    	t=str(search(text)[0].encode("utf-8"))    	
    	em=discord.Embed(title=text,description=str(summary(t,sentences=5)),color=ctx.author.color)
    	await ctx.send(embed=em)
    @client.command()
    async def check(ctx):
        req()
        print("check")
        em=discord.Embed(title="Online",description="Dormammu, I've come to bargain",color=ctx.author.color)
        await ctx.send(embed=em)
    @client.command()
    async def yey(ctx):
        req()
        print("yey")
        em=discord.Embed(title="*yey*")
        await ctx.send(embed=em)    
    @client.command(aliases=['g'])
    async def google(ctx,*,text):
        req()
        print(text)
        li="**"+text+"** \n\n"
        for i in googlesearch.search(text,num=7,stop=7,pause=0):
            li=li+i+" \n\n"
        text=text.replace(' ','%20')
        li=li+"**Query link:**https://www.google.com/search?q="+text+"\n"
        await ctx.send(li)    
    @client.command(aliases=['cen'])
    async def add_censor(ctx,*,text):
    	string=""
    	censor.append(text.lower())
    	for i in range(0,len(text)):
    		string=string+"-"
    	em=discord.Embed(title="Added "+string+" to the list",decription="Done",color=ctx.author.color)
    	await ctx.send(embed=em)
    @client.event
    async def on_message(msg):
    	for word in censor:
    		if word in msg.content.lower():
    			await msg.delete()    	
    	await client.process_commands(msg)
    @client.command(aliases=['m'])
    async def meth(ctx,*,text):
        req()
        pi=ma.pi
        a=eval(text)
        text=text.replace("ma.","")
        text=text.replace("s.","")        
        print(text)
        em=discord.Embed(title=text,description=text+"="+str(a),color=ctx.author.color)
        await ctx.send(embed=em)
    @client.command()
    async def get_req(ctx):
        req()
        number=g_req()
        em=discord.Embed(title="Requests",description=str(number),color=ctx.author.color)
        await ctx.send(embed=em)
    def r(x):
        return ma.radians(x)
    def d(x):
        return ma.degrees(x)
    def add(p1,p2):
        da[p1]=p2
        return "Done"
    def get(k):
        return da.get(k,"Not assigned yet")
    def de(k):
        del da[k]
        return "Done"
    def req():
        re[0]=re[0]+1
    def g_req():
        return re[0]
    def quad(eq):
        if "x^2" not in eq:
            return "x^2 not found, try again"
        print(eq)
        eq=eq.replace("2+","2 + ")
        eq=eq.replace("2-","2 - ")
        eq=eq.replace("x+","x + ")
        eq=eq.replace("x-","x - ")
        
        #try to get correct equation
        parts = [x.strip() for x in eq.split(" ")]
        a, b, c = 0, 0, 0
        for i in parts:
            if i==' ':
                parts.remove(' ')
        
        for index, part in enumerate(parts):
            if part in ["+", "-"]:
                continue
            
            symbol = -1 if index - 1 >= 0 and parts[index - 1] == "-" else 1

            if part.endswith("x^2"):
                coeff = part[:-3]
                a = float(coeff) if coeff != '' else 1
                a *= symbol
            elif part.endswith("x"):
                coeff = part[:-1]
                b = float(coeff) if coeff != '' else 1
                b *= symbol
            elif part.isdigit():
                c = symbol * float(part)

        determinant = b**2 - (4 * a * c)

        if determinant < 0:
            return "Not Real"
        if determinant == 0:
            root = -b / (2 * a)
            return "Equation has one root:"+str(root) 
 
        if determinant > 0:
            determinant = determinant ** 0.5
            root1 = (-b + determinant) / (2 * a)
            root2 = (-b - determinant) / (2 * a)
            return "This equation has two roots: "+str(root1)+","+str(root2)
	
        
    @client.command()
    async def p(ctx,*,text):
        req()
        print("P"+text)
        a=eval(text)
        ans=ma.factorial(a[0])/ma.factorial(a[0]-a[1])
        em=discord.Embed(title="P"+text+":",description=str(ans),color=ctx.author.color)
        await ctx.send(embed=em)
    @client.command()
    async def c(ctx,*,text):
        req()
        print("c"+text)
        a=eval(text)
        ans=ma.factorial(a[0])/(ma.factorial(a[1])*ma.factorial(a[0]-a[1]))
        em=discord.Embed(title="C"+text+":",description=str(ans),color=ctx.author.color)
        await ctx.send(embed=em)
    @client.command(aliases=['mu'])
    @commands.has_permissions(kick_members=True)
    async def mute(ctx,member:discord.Member):
    	req()
    	try:
    		add_role=discord.utils.get(ctx.guild.roles,name="dunce")
    		await member.add_roles(add_role)
    		await ctx.send("Muted "+member.mention)
    		print(member,"muted")
    	except:
    		await ctx.send("Not Done")
    @client.command(aliases=['um'])
    @commands.has_permissions(kick_members=True)
    async def unmute(ctx,member:discord.Member):
    	req()
    	try:
    		add_role=discord.utils.get(ctx.guild.roles,name="dunce")
    		await member.remove_roles(add_role)
    		await ctx.send("Unmuted "+member.mention)
    		print(member,"unmuted")
    	except:
    		await ctx.send("Not Done") 
    
    	
    te="**Commands**\n'google <text to search> \n'help to get this screen\n'c (n,r) for *combination* \n'p (n,r) for *permutation* \n**Leave space between p/c and the bracket'('** \n'meth <Expression> for any math calculation *(includes statistic)*\n'get_req for no. of requests\n"
    te=te+"**Modules**:\n**ma** for math module\n**s** for statistics module \n\nr(angle in degree) to convert angle to radian \nd(angle in radian) to convert angle to radian\n\n"
    te=te+"**Alias**: \n'g <text to search> \n'h to show this message \n'm <Expression> for any math calculation *(includes statistic)*\n\n"
    te=te+"**Example**:\n'm quad('4x^2+2x-3')\n'p (10,9) \n'm ma.sin(r(45))\n'm ma.cos(pi)\n'help\n**Use small letters only**"
    client.remove_command("help")
    @client.group(invoke_without_command=True)
    async def help(ctx):
        req()
        print("help")
        em=discord.Embed(title="**HELP** \n",description=te,color=ctx.author.color)   
        await ctx.send(embed=em)
    @client.group(invoke_without_command=True)
    async def h(ctx):
        req()
        print("help")
        em=discord.Embed(title="**HELP** \n",description=te,color=ctx.author.color)
        await ctx.send(embed=em)   
    client.run("ODExNTkxNjIzMjQyMTU0MDQ2.YC0bmQ.4oW1hyppcaQJpRfKFRJCiddZ5aI")
else:
    print("Something has occured")

