from dotenv import load_dotenv
from os import getenv
from disnake.ext.commands import InteractionBot
from disnake import (
    Intents,
    Activity,
    Status,
    AuditLogEntry,
    AuditLogAction,
    Member,
    Role,
)
from typing import (
    Dict,
    List,
)

load_dotenv()

# Will make better later.
intents = Intents.all()

bot = InteractionBot(
    intents=intents,
    status=Status.dnd,
    activity=Activity(name=f"Patreons bot make mistakes.", type=4),
)

ROLE_UPDATE: Dict[int, List[Role]] = {}

PATREON_DISCORD_BOT_ID = getenv("PATREON_DISCORD_BOT_ID")


async def wait_and_check(entry: AuditLogEntry) -> None:
    pass


@bot.event
async def on_ready() -> None:
    print("Bot has connected to the Discord gateway")


@bot.listen("on_audit_log_entry_create")
async def on_audit_log_entry_create_handler(entry: AuditLogEntry) -> None:
    if (
        entry.user == PATREON_DISCORD_BOT_ID
        and entry.action == AuditLogAction.member_role_update
    ):
        pass


@bot.listen("on_member_update")
async def on_member_update_handler(before: Member, after: Member) -> None:
    if before.roles != after.roles:
        pass


bot.run(getenv("DISCORD_BOT_TOKEN"))
