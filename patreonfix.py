from asyncio import sleep
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
    Optional,
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
PATREON_ROLE_ID = getenv("PATREON_ROLE_ID")
SLEEP_DURATION = getenv("SLEEP_DURATION")


async def wait_and_check(entry: AuditLogEntry) -> None:
    await sleep(SLEEP_DURATION)


@bot.event
async def on_ready() -> None:
    print("Bot has connected to the Discord gateway")


@bot.listen("on_audit_log_entry_create")
async def on_audit_log_entry_create_handler(entry: AuditLogEntry) -> None:
    if (
        entry.user == PATREON_DISCORD_BOT_ID
        and entry.action == AuditLogAction.member_role_update
    ):
        await wait_and_check(entry)


@bot.listen("on_member_update")
async def on_member_update_handler(
        member_before: Optional[Member],
        member_after: Optional[Member],
    ) -> None:
    if member_before is None or member_after is None:
        # Member has only just joined or just left.
        return

    if len(member_before.roles) < len(member_after.roles):
        # There's less roles than before.
        for role in before_role_ids:
            if role not in after_role_ids:
                # This is the role that was removed.
                if ROLE_UPDATE.get(member_after.id, None) is None:
                    ROLE_UPDATE[member_after.id] = []
                ROLE_UPDATE[member_after.id].append(role)


bot.run(getenv("DISCORD_BOT_TOKEN"))
