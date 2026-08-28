import os
import json
from time import time, sleep

from pypresence import Presence
from app import (
    CONFIG_PATH,
    DEFAULT_CLIENT_ID
)


def log(message):
    print(f"[+] {message}")


def main():
    log("Please wait...")

    try:

        GTAVI = {
            "client_id": DEFAULT_CLIENT_ID,
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
