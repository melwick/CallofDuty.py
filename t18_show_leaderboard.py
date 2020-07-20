import asyncio
import os

from dotenv import load_dotenv

import callofduty as cod


async def main():
    # Load Environment Variables from the file ".env"
    load_dotenv()
    cod_user_email = os.environ["ATVI_EMAIL"]
    cod_user_pass = os.environ["ATVI_PASSWORD"]

    queryUser = os.environ["QUERY_USER"]

    print(queryUser)

    print(f"User Email: {cod_user_email}, User Password: {cod_user_pass}")

    # CoD Login:
    client = await cod.Login(cod_user_email, cod_user_pass)

    # show leaderboard
    print("Leaderboard Modern Warfare")
    leaderboard = await client.GetLeaderboard(
        cod.Title.ModernWarfare, cod.Platform.BattleNet, gameMode="cyber", page=1
    )
    for entry in leaderboard.entries:
        print(f"#{entry.rank}: {entry.username} ({entry.platform.name})")


# Program Start:
asyncio.get_event_loop().run_until_complete(main())
