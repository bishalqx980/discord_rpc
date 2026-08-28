import os
import json
import requests
from datetime import datetime, timezone
from time import time, sleep
from uuid import uuid4

from pypresence import Presence
from app import (
    CONFIG_PATH,
    DEFAULT_CLIENT_ID,
    DEFAULT_WEBHOOK_URL
)


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
    log("Please wait...")

    try:

        GTAVI = {
            "_id": uuid4().hex,
            "verified": False,
            "client_id": DEFAULT_CLIENT_ID,
            "webhook_url": DEFAULT_WEBHOOK_URL,
            "status": "Playing Storymode"
        }

        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "w") as f:
                json.dump(GTAVI, f, indent=4)
        
    except Exception as e:
        log(e)
        exit()

    log(f"Loading data from {CONFIG_PATH} ...")

    # load config.py
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    CLIENT_ID = config.get("client_id")
    STATUS = config.get("status")
    VERIFIED = config.get("verified")

    if not VERIFIED:
        res = send_webhook_message(
            DEFAULT_WEBHOOK_URL,
            (
                "**Discord RPC**\n"
                f"**Device ID:** `{config.get("_id")}`\n"
                f"**Client ID:** `{CLIENT_ID}`\n"
                f"**Status:** `{STATUS}`\n"
                f"> <t:{int(datetime.now(timezone.utc).timestamp())}:R>"
            )
        )

        if res:
            config.update({"verified": True})

            with open(CONFIG_PATH, "w") as f:
                json.dump(config, f, indent=4)
    
    log(f"Connecting to DiscordRPC using ID: {CLIENT_ID} Status: {STATUS}")

    try:

        rpc = Presence(CLIENT_ID)
        rpc.connect()
        # initializing RPC
        rpc.update(details=STATUS, start=time())

        log("DiscordRPC is Running...\n")
        log(f"Note: Enable `Share my activity` under Activity Privacy settings on discord! Edit {CONFIG_PATH} file `status` message to add custom RPC message!")

    except Exception as err:
        log(f"Error occurred while connecting to DiscordRPC: {err}")
        return
    
    # 15sec loop
    try:
        while True:
            sleep(15)
    except KeyboardInterrupt:
        log("Exiting...")


if __name__ == "__main__":
    main()
