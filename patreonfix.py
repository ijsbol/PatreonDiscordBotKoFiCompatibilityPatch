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

intents = Intents.none()
intents.members = True
intents.moderation = True

bot = InteractionBot(
    intents=intents,
    status=Status.dnd,
    activity=Activity(name=f"Patreons bot make mistakes.", type=4),
)

ROLE_UPDATE: Dict[int, List[Role]] = {}

PATREON_DISCORD_BOT_ID = int(getenv("PATREON_DISCORD_BOT_ID"))
PATREON_ROLE_ID = int(getenv("PATREON_ROLE_ID"))
SLEEP_DURATION = int(getenv("SLEEP_DURATION"))


async def wait_and_check(entry: AuditLogEntry) -> None:
    # Wait for all roles to be removed by the Patreon bot.
    await sleep(SLEEP_DURATION)

    targetted_member = entry.guild.get_member(entry.target.id)

    removed_roles = [role for role in ROLE_UPDATE[entry.target.id]]

    if PATREON_ROLE_ID in [role.id for role in removed_roles]:
        # Patreon is removing roles from someone it should be removing roles from.
        return
    
    for role in removed_roles:
        # Add roles back that patreon mistakenly removed.
        await targetted_member.add_roles(role, reason="Adding role back that Patreon removed.")
    
    del ROLE_UPDATE[entry.target.id]


@bot.event
async def on_ready() -> None:
    print("Bot has connected to the Discord gateway")


@bot.listen("on_audit_log_entry_create")
async def on_audit_log_entry_create_handler(entry: AuditLogEntry) -> None:
    if (
        entry.user.id == PATREON_DISCORD_BOT_ID
        and entry.action == AuditLogAction.member_role_update
        and len(entry.changes.before.roles) == 1 # Role was removed rather than added.
    ):
        removed_role = entry.changes.before.roles[0]
        targetted_user = entry.target

        if ROLE_UPDATE.get(targetted_user.id, None) is None:
            # The Patreon bot hasn't removed any roles yet.
            ROLE_UPDATE[targetted_user.id] = [removed_role]
            return await wait_and_check(entry)

        # Store addtional roles that the Patreon bot removes.
        ROLE_UPDATE[targetted_user.id].append(removed_role)


bot.run(getenv("DISCORD_BOT_TOKEN"))
