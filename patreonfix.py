from dotenv import load_dotenv
from os import getenv
from disnake.ext.commands import InteractionBot
from disnake import (
    Intents,
    Activity,
    Status,
    AuditLogEntry,
    AuditLogAction,
)

load_dotenv()

# I hate this, but on_audit_log_entry_create is pretty much entirely cache based, fml.
intents = Intents.all()

bot = InteractionBot(
    intents=intents,
    status=Status.dnd, 
    activity=Activity(name=f'Patreons bot make mistakes.', type=4),
)

@bot.event
async def on_ready():
    print("Bot has connected to the Discord gateway")

@bot.listen('on_audit_log_entry_create')
async def on_audit_log_entry_create(entry: AuditLogEntry) -> None:
    if entry.action == AuditLogAction.member_role_update:
        print("updated roles")

bot.run(getenv('DISCORD_BOT_TOKEN'))
