from discord import Interaction, Object
from discord.app_commands import CommandTree
from src.slash_commands import SlashClient
from src.main import get_secret_key, formatsExplaination, time_tag_builder, timestamp
from random import randint

def make_dttime_command(tree: CommandTree, guild_id, style, desc):
    print(style, desc)
    @tree.command(name=desc.replace(' ', '_'), description=desc)
    async def self(interaction: Interaction):
        await interaction.response.send_message(f"{time_tag_builder(t='t', timestamp=timestamp(), style=style)}")
    return self


def main():
    client = SlashClient()
    tree = client.tree
    guild_id = 832176801417658388
    @tree.command(name='test', description='testing')
    async def self(interaction: Interaction):
        await interaction.response.send_message(f"Greetings! I was made by DayDay!")
    time_commands = {}
    for style, desc in formatsExplaination.items():
        time_commands[style] = make_dttime_command(tree, guild_id, style, desc)

    client.run(get_secret_key())


# if __name__ == '__main__':
#     main()
