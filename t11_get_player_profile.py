import asyncio
import os

from dotenv import load_dotenv

import callofduty as cod

# we want to write the date into a json file
import json


async def main():
    # Load Environment Variables from the file ".env"
    load_dotenv()
    cod_user_email = os.environ["ATVI_EMAIL"]
    cod_user_pass = os.environ["ATVI_PASSWORD"]

    # queryUser = os.environ["QUERY_USER"]
    queryUser = "Icoryx"
    print(queryUser)

    print(f"User Email: {cod_user_email}, User Password: {cod_user_pass}")

    # CoD Login:
    client = await cod.Login(cod_user_email, cod_user_pass)

    results = await client.GetPlayerProfile(
        cod.Platform.Activision,
        "Icoryx",
        cod.Title.ModernWarfare,
        cod.Mode.Multiplayer,
    )

    with open(f"player_data_{queryUser}.json", "w") as outfile:
        json.dump(results, outfile)


# Program Start:
asyncio.get_event_loop().run_until_complete(main())
