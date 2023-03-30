import discord
import openai
import os

# Set up the Discord client with intents
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

os.environ['OPENAI_API_KEY'] = 'YOURAPIKEYHERE'

# Set up the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set up the ChatGPT model
model_engine = 'text-davinci-002'
prompt = ''

# Respond to messages
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Set up the prompt
    global prompt
    prompt += message.content

    # Get the response from the ChatGPT model
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the response back to the Discord channel
    await message.channel.send(response.choices[0].text)

# Run the bot
client.run('YOURDISCORDBOTTOKEN')
