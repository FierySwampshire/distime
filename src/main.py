from datetime import datetime
from operator import pos
from src.client.my_client import MyClient
import os
import discord

# (t, timestamp, style)
time_tag_builder = '<{t}:{timestamp}:{style}>'.format

def timestamp():
    return int(datetime.now().timestamp())
# key:value
displayFormats = {
    't': "LT",  # short time
    'T': "LTS",  # long time
    'd': "L",  # short date
    'D': "LL",  # long date
    'f': "LLL",  # short date/time
    'F': "LLLL",  # long date/time
    "R": "R"  # relative time
}

formatsExplaination = {
't': 'short time',
'T': 'long time',
'd': 'short date',
'D': 'long date',
'f': 'short date time',
'F': 'long date time',
"R": 'relative time',
}

def test():
    timestamp = int(datetime.now().timestamp())
    for k, v in formatsExplaination.items():
        print(v, time_tag_builder(t='t', timestamp=timestamp, style=k))


def get_secret_key():
    SECRET_KEY = str(os.getenv("SECRET_KEY", None))
    return SECRET_KEY


def main():
    # client = MyClient()
    SECRET_KEY = str(os.getenv("SECRET_KEY", None))
    print(f'{SECRET_KEY=}')
    if SECRET_KEY == str(None):
        SECRET_KEY = 'MTAwNTg1NTAzNDQ4NDk4NTk1Nw.GNu8mk._SON33hkTeeBexbeR_84WYxKSm18eXzkvrda7o'
    # client.run(str(SECRET_KEY))
    client(SECRET_KEY)


def msg_dict(message: discord.Message):
    return {
        # 'ack':message.ack,
        'activity':message.activity,
        # 'add_reaction':message.add_reaction,
        'application':message.application,
        'attachments':message.attachments,
        'author':message.author,
        # 'call':message.call,
        'channel':message.channel,
        # 'channel_mentions':message.channel_mentions,
        # 'clean_content':message.clean_content,
        # 'clear_reaction':message.clear_reaction,
        # 'clear_reactions':message.clear_reactions,
        'content':message.content,
        'created_at':message.created_at,
        # 'delete':message.delete,
        # 'edit':message.edit,
        'edited_at':message.edited_at,
        'embeds':message.embeds,
        'flags':message.flags,
        'guild':message.guild,
        'id':message.id,
        # 'is_system':message.is_system,
        'jump_url':message.jump_url,
        'mention_everyone':message.mention_everyone,
        'mentions':message.mentions,
        'nonce':message.nonce,
        # 'pin':message.pin,
        'pinned':message.pinned,
        # 'publish':message.publish,
        'raw_channel_mentions':message.raw_channel_mentions,
        'raw_mentions':message.raw_mentions,
        'raw_role_mentions':message.raw_role_mentions,
        'reactions':message.reactions,
        'reference':message.reference,
        # 'remove_reaction':message.remove_reaction,
        # 'reply':message.reply,
        'role_mentions':message.role_mentions,
        'stickers':message.stickers,
        'system_content':message.system_content,
        'to_message_reference_dict':message.to_message_reference_dict(),
        # 'to_reference':message.to_reference,
        'tts':message.tts,
        'type':message.type,
        # 'unpin':message.unpin,
        'webhook_id':message.webhook_id,
    }


def client(SECRET_KEY):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message:discord.message.Message):
        print(type(message))
        print(message)
        print(msg_dict(message))
        author:discord.member.Member = message.author
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send(f'{author.mention} Hello!')
    client.run(SECRET_KEY)

def run():
    test()
    main()
