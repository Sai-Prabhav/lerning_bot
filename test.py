# This example requires the 'message_content' privileged intent to function.

from discord.ext import commands
import os
import discord
from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix=commands.when_mentioned_or('.'),
            intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


class Confirm(discord.ui.View):
    def __init__(self, msg: discord.message):
        super().__init__()
        self.message = msg
        self.value = ""
        self.msg = ""
        self.result = 0

    async def update_num(self, num: int, interaction: discord.Interaction):
        await interaction.response.send_message('recorded', ephemeral=True)
        self.value += str(num)
        self.msg += str(num)
        await self.message.edit(content=f"```{self.msg}```")

    async def update_op(self, op: str, interaction: discord.Interaction):
        await interaction.response.send_message('recorded', ephemeral=True)
        self.value = ""
        self.msg += op
        await self.message.edit(content=self.msg)

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def inp_1(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(1, interaction)

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def inp_2(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(2, interaction)

    @discord.ui.button(label='3', style=discord.ButtonStyle.green)
    async def inp_3(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(3, interaction)

    @discord.ui.button(label='4', style=discord.ButtonStyle.green)
    async def inp_4(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(4, interaction)

    @discord.ui.button(label='5', style=discord.ButtonStyle.green)
    async def inp_5(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(5, interaction)

    @discord.ui.button(label='6', style=discord.ButtonStyle.green)
    async def inp_6(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(6, interaction)

    @discord.ui.button(label='7', style=discord.ButtonStyle.green)
    async def inp_7(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(7, interaction)

    @discord.ui.button(label='8', style=discord.ButtonStyle.green)
    async def inp_8(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(8, interaction)

    @discord.ui.button(label='9', style=discord.ButtonStyle.green)
    async def inp_9(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(9, interaction)

    @discord.ui.button(label='0', style=discord.ButtonStyle.green)
    async def inp_0(self,
                    interaction: discord.Interaction,
                    button: discord.ui.Button):

        await self.update_num(0, interaction)

    @discord.ui.button(label='+', style=discord.ButtonStyle.green)
    async def add(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button):
        self.result += int(self.value)
        await self.update_op("+", interaction)

    @discord.ui.button(label='-', style=discord.ButtonStyle.green)
    async def subtract(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button):
        self.result -= int(self.value)
        await self.update_op("-", interaction)

    @discord.ui.button(label='*', style=discord.ButtonStyle.green)
    async def multiply(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button):
        self.result *= int(self.value)
        await self.update_op("*", interaction)

    @discord.ui.button(label='submit', style=discord.ButtonStyle.grey)
    async def submit(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button):
        await interaction.response.send_message(
            f'```{self.msg} = {self.result + int(self.value)}```',
            ephemeral=True)
        await self.message.edit(content=f'```{self.msg} = {self.result + int(self.value)}```')
        self.stop()


bot = Bot()


@bot.command()
async def math(ctx: commands.Context):
    """Asks the user a question to confirm something."""
    msg = await ctx.send("text")

    view = Confirm(msg)
    await ctx.send(" ", view=view)
    # Wait for the View to stop listening for input...
    await view.wait()
    if view.value == "":
        print('Timed out...')
    elif view.value:
        print(view.result)
    else:
        print('Cancelled...')


bot.run(os.getenv("hi"))
