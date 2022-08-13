
#pip install requests
#pip install requests-HTML
#pip install padas
#py -3 -m pip install -U hikari
import hikari
import lightbulb

bot = lightbulb.BotApp(token='MTAwNzc5NjE0ODk4MDk1NzI3NA.GjXAP7.Kw-ZWLHlFDfYxmrsghkQQyZ2hdsiWEhlNz7mE8', default_enabled_guilds=(692089694254530570))

@bot.listen(hikari.GuildMessageCreateEvent)
async def deploy_monster(event):
    if event.channel_id == 1007782614079373373 and event.is_bot == False:
        print(event.channel_id)
        print(event.content)
        await event.message.respond("Go fuck yourself")
      
    



@bot.command
@lightbulb.command('monster','Retrieves a monster statblock')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("This response is not ready yet")


bot.run()