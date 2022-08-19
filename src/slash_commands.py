from typing import Any
from discord import Intents, app_commands, Object
from discord.app_commands import CommandTree
import discord

class SlashClient(discord.Client):
    def __init__(self, intents: Intents=Intents.default(), *args, **options: Any) -> None:
        super().__init__(intents=intents, **options)
        self.synced = False
        self._tree = CommandTree(self)

    @property
    def tree(self):
        return self._tree

    async def on_ready(self) -> None:
        await self.wait_until_ready()
        if not self.synced:
            guild_id = 832176801417658388
            await self._tree.sync(guild=Object(id=guild_id))  # guild sync, remove id for global sync
            self.synced = True
        print(f'we have logged in as {self.user}./')
