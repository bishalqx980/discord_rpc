import os
import requests
from datetime import datetime, timezone
from time import time, sleep
from uuid import uuid4

from pypresence import Presence
from app import DATA_JSON, DATA_URL, BISHAL


def log(message):
    print(f"[+] {message}")


def send_webhook_message(webhook_url, message):
    try:
        res = requests.post(
            webhook_url,
            json={ "content": message }
        )

        return res
    except Exception as err:
        log(err)


def main():
    log(BISHAL)

    # uuid4
    log("Verifying device...")

    if os.path.exists("verified.log"):
        with open("verified.log", "r") as f:
            DEVICE_ID = f.read()
    else:
        with open("verified.log", "w") as f:
            DEVICE_ID = uuid4()
            f.write(str(DEVICE_ID))
    
    # Fetching Data
    log("Fetching data...")

    try:
        res = requests.get(DATA_URL)
        DATA = res.json() if res.ok else None
    except Exception as err:
        log(f"Error fetching data: {err}")
        return
    
    if not DATA:
        log("Something went wrong... (Data wasn't found)")
        return
    
    # Custom Status
    if os.path.exists("status.txt"):
        with open("status.txt", "r") as f:
            STATUS = f.read()
    else:
        with open("status.txt", "w") as f:
            STATUS = "Vibing"
            f.write(str(STATUS))
            
    # Status
    CLIENT_ID = DATA.get("client_id")
    WEBHOOK_URL = DATA.get("webhook_url")

    # Connecting RPC
    log(f"Connecting RPC - Starting Playing with status: {STATUS}")

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

        log(f"DiscordRPC is Running...")
    except Exception as err:
        log(f"Error occurred while connecting RPC: {err}")
        return
    
    # 15sec loop
    try:
        while True:
            sleep(15)
    except KeyboardInterrupt:
        log("Exiting...")


if __name__ == "__main__":
    main()
