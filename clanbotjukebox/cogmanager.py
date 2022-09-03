import functools
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord import option, Permissions

import settings


async def logCommand(channel, ctx, *args, **kwargs):
    log_string = ":arrow_forward: Command:  "
    log_string += ctx.channel.mention if isinstance(ctx.channel, discord.TextChannel) else "????"
    log_string += f" | {ctx.author}: /{ctx.command} "
 
    for k, v in kwargs.items():
        log_string += f" {k}: {v}"
    await channel.send(log_string)


client = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=settings.INTENTS)
@client.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    """
    Give feedback to the user when user has no perms to use the command
    :param ctx: Original command context
    :param error: Error
    :return:
    """

    if isinstance(error, commands.errors.MissingRole):
        await ctx.response.send_message(f"{ctx.author.mention}, You do not have permissions to use that command.", ephemeral=True)
    else:
        raise error

@client.event
async def on_application_command_error(ctx: commands.Context, error: commands.CommandError):
    """
    Give feedback to the user when user has no perms to use the command
    :param ctx: Original command context
    :param error: Error
    :return:
    """
    await on_command_error(ctx, error)

def slashcommandlogger(func):
    """
    Decorator to log slash commands
    :param func: wrapped function
    :return:
    """
    @functools.wraps(func)
    async def wrapped(ctx, cog: str):
        # Some fancy foo stuff
        await logCommand(client.get_channel(settings.DISCORD_LOG_CHANNEL), ctx, cog=cog.lower())
        await func(ctx, cog)

    return wrapped

if __name__ == "__main__":
    # Load all cogs
    for cog in settings.DISCORD_COGS:
        client.load_extension(f'cogs.{cog.name}')

    client.run(settings.DISCORD_TOKEN)
