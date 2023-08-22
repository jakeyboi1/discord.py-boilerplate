### This file should only contain code the bot will directly use. Try to keep this as small and as clean as possible by using the helpers/data/services folders!###

# Importing neededmodules into our code
import discord #Gets discord
from discord import app_commands #gets commands from discord
from discord.ext import commands #gets discord.ext from discord
import services.randomNumberGen as rng #This imports our file under the services folder allowing us to use functions from inside that file here!
import threading
import time

bot = commands.Bot(command_prefix="insertPrefix", intents=discord.Intents.all()) #Setting up our bot(note command prefix I generally do not use, and for this boilerplate will only be using slash commands)

# Initial loading of our bot
@bot.event #Defining a bot event
async def on_ready(): #This function will trigger when your bot has been loaded! Nothing can or should be run before this function is called, and do not rename this function!
    print("Bot is loaded, and ready!")

    #Loading/syncing our commands
    try:
        await bot.tree.sync() #This is loading and syncing our commands!
        print("Bot has been synced, and commands have been registerd!")
    except Exception as e:
        print(e)

    await bot.change_presence(activity=discord.CustomActivity(name='Monitoring /helloworld')) #Setting bots status

    #Setting up our thread for our threading example function
    exampleThread = threading.Thread(target=threadingExample) #Creates a variable used for our thread, the target paramater needs to be the function you want this thread to trigger
    exampleThread.start() #Starts our thread!
    print("Our thread is running and so is all of our other code without any code being blocked!")

#This is an example of threading which can be useful if you have code with a while loop, but dont want it to block the rest of your code from running while the loop is going
def threadingExample():
    while True:
        print("Thread running! You will notice this does not affect your bots functionality all commands will still run fine while this loop is going, this is the power of threading in python!")
        time.sleep(5)
        #Note if you just triggered this function normally instead of using threading only this function will run, and none of our slash commands will work as all of our bots code will be being blocked by this function


#Registering our first slash command without any accepted arguments!
@bot.tree.command(name="helloworld") #Setting the name of our slash command
async def helloworld(interaction: discord.Interaction): #the function that will trigger when the command is used note these have to be async functions, and must always have the paramater of interaction: discord.Interaction the functions name must be the same as the commands name aswell
    await interaction.response.send_message("Hello world!") #Will send a message in the chat saying "Hello world!" in the chat the command was used in


#Register a function to trigger when a message is sent
@bot.event
async def on_message(message):
    # Here is some useful data you can pull from the message variable. "message.content" - The message that was sent, "message.author" - The user who sent the message, "message.channel" - the channel the message was sent from
    if message.author == bot.user: #this is checking if the message is from this bot
        return # Returns (does not run any code below this point)
    
    await message.channel.send(f'User: "{message.author}" sent message: "{message.content}"') #will send a message to the channel the message came from saying "User: SendersName sent: messageSent" f'' just allows you to input variables and code into the string inside of {}


#Registering a slash command with accepted arguements
@bot.tree.command(name="randomnumber") #Naming our command must be all lowercase
@app_commands.describe(minimumnumber="Lowest possible number", maximumnumber="Highest possible number") #setting our desired user input of minimumnumber and maximumnumber must be all lowercase
async def randomnumber(interaction: discord.Interaction, minimumnumber: str, maximumnumber: str): #defining the function that will trigger when the command is used not the command name must be the same as the commands name. catches the user input paramaters of minimumnumber and maximunumber these variables must be named exactly the same as they are when describing them above in the @app_commands.describe
    await interaction.response.send_message(f'Random number generated between {minimumnumber} and {maximumnumber}! Number: {rng.generateRandomNumber(int(minimumnumber), int(maximumnumber))}') #This will send a message in the channel the command was used in, and will call  the function from randomNumberGen.py file to get a random number between the minimum and maximum numbers!

bot.run("insert your bot token here in these quotes") #Will start our bot This must be at the bottom of your code