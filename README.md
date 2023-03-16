# PatreonDiscordBotKoFiCompatibilityPatch

|  |  |
|--|--|
| <img align="center" src="https://i.imgur.com/QhMmR5M.png" height="128" width="128"/> | <img align="center" src="https://img.shields.io/github/license/scrumpyy/PatreonDiscordBotKoFiCompatibilityPatch?style=for-the-badge"/><img align="center" src="https://img.shields.io/github/issues/scrumpyy/PatreonDiscordBotKoFiCompatibilityPatch?style=for-the-badge"/><br><img align="center" src="https://img.shields.io/github/stars/scrumpyy/PatreonDiscordBotKoFiCompatibilityPatch?style=for-the-badge"/> |

Patreons Discord bot will remove Discord roles from users who do not have an active subscription, regardless on if they *ever* had a subscription.

This fairly poor implementation results in numerous issues and makes it impossible to use other subscription services such as KoFi or BuyMeACoffee with the same reward roles as Patreon.

This bot fixes that.

## Setup
All you need to do to set it up yourself is to create a new role (i.e a role called "Patreon Subscriber") that is given to *everyone* who subscribes through Patreon and then update the example.env file's `PATREON_ROLE_ID` to be equal to the role ID of that role.

After you have done that you just need to create a Discord bot, set the `DISCORD_BOT_TOKEN` equal to your bots token & then rename `example.env` to `.env`.

To setup on a VPS you need to install Python 3.8+ and run the following command: `pip install -r requirements.txt`, alternatively you may need to do `python -m pip install -r requirements.txt`. Then just run like normal with `python patreonfix.py`.

## But why don't KoFi/BuyMeACoffee need one of these?
Well, that's because KoFi & BMAC hired a competent developer. Instead of removing roles from *everyone* they instead only remove roles from people who *have cancelled their subscription.* This means that KoFi/BMAC will *only* remove roles from people who were originally given the roles through KoFi/BMAC and have since cancelled their subscription (i.e. when they are supposed to take roles away).

## Example
![Logo](https://i.imgur.com/wpzlm7k.png)
