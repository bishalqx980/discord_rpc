import os
import requests
from datetime import datetime, timezone
from time import time, sleep
from uuid import uuid4
from pypresence import Presence

from logger import setup_logging

# Variables
DATA_URL = "https://gist.githubusercontent.com/bishalqx980/8b023d11425997da267e1f601d94082d/raw/discord_rpc.json"
logger = setup_logging()


def send_webhook_message(webhook_url, message):
    try:
        res = requests.post(
            webhook_url,
            json={ "content": message }
        )

        return res
    except Exception as err:
        logger.error(err)


def main():
    BISHAL = """
Developed by
 ______     __     ______     __  __     ______     __        
/\  == \   /\ \   /\  ___\   /\ \_\ \   /\  __ \   /\ \       
\ \  __<   \ \ \  \ \___  \  \ \  __ \  \ \  __ \  \ \ \____  
 \ \_____\  \ \_\  \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_/   \/_____/   \/_/\/_/   \/_/\/_/   \/_____/ 
   
    GitHub: https://github.com/bishalqx980
"""

    print(BISHAL)

    # Getting Device ID
    logger.info("Verifying device...")

    if os.path.exists("verified.log"):
        with open("verified.log", "r") as f:
            DEVICE_ID = f.read()
    else:
        with open("verified.log", "w") as f:
            DEVICE_ID = uuid4()
            f.write(str(DEVICE_ID))
    
    # Fetching Data
    logger.info("Fetching data...")

    try:
        res = requests.get(DATA_URL)
        DATA = res.json() if res.ok else None
    except Exception as err:
        logger.error(f"Error fetching data: {err}")
        return
    
    if not DATA:
        logger.error("Something went wrong... (Data wasn't found)")
        return
    
    # Custom Status
    if os.path.exists("status.txt"):
        with open("status.txt", "r") as f:
            STATUS = f.read()
    else:
        with open("status.txt", "w") as f:
            STATUS = "Vibing"
            f.write(str(STATUS))
        
    
    # Device ID
    # Status
    CLIENT_ID = DATA.get("client_id")
    WEBHOOK_URL = DATA.get("webhook_url")

    # Connecting RPC
    logger.info(f"Connecting RPC - Starting Playing with status: {STATUS}")

    try:
        rpc = Presence(CLIENT_ID)
        rpc.connect()
        # initializing RPC
        rpc.update(details=STATUS, start=time())

        # Send Webhook message
        send_webhook_message(
            WEBHOOK_URL,
            (
                "**Activity Alert !!! [ <@&1462103653883314287> ]**\n"
                f"Device ID: `{DEVICE_ID}`\n"
                f"Client/App ID: `{CLIENT_ID}`\n"
                f"Status: `{STATUS}`\n"
                f"> <t:{int(datetime.now(timezone.utc).timestamp())}:R>"
            )
        )

        # Cleaning Console
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{BISHAL}\nDiscord RPC Running...", flush=True)
    except Exception as err:
        logger.error(f"Error occurred while connecting RPC: {err}")
        return
    
    # 15sec loop
    try:
        while True:
            sleep(15)
    except KeyboardInterrupt:
        logger.info("Exiting...")


if __name__ == "__main__":
    main()
