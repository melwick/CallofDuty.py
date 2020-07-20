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

    # Get my identities
    identities = await client.GetMyIdentities()
    for identity in identities:
        title = identity["title"].name
        username = identity["username"]
        platform = identity["platform"].name
        print(f"{title}: {username} ({platform})")


# Program Start:
asyncio.get_event_loop().run_until_complete(main())
