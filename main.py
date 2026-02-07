import json
import os
import sys
import requests
from uuid import uuid4
from time import time, sleep
from pypresence import Presence


def resource_path(relative):
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.abspath(relative)


def get_app_dir():
    # If running as EXE
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)

    # If running as .py
    return os.path.dirname(os.path.abspath(__file__))


def load_config():
    path = os.path.join(get_app_dir(), "config.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found at {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def send_webhook_msg(device_id):
    WEBHOOK_URL = "https://discord.com/api/webhooks/1469599680869437546/elBL1MT7klb6RNhF8-ag8fAe6IvXsAD_MzNeLIkOJFMcicQCI1wTDujfCf5i4UiEc7ze"

    data = {
        "content": f"> Device {device_id} is Playing Grand Theft Auto VI"
    }

    try:
        requests.post(WEBHOOK_URL, json=data)
    except:
        pass


def main():
    try:
        config = load_config()
    except Exception as e:
        print(f"Failed to load config: {e}")
        return

    client_id = config.get("key")
    if not client_id:
        print("Client ID (key) is missing in config.")
        return

    status = config.get("status") or "Prologue"

    # Device ID
    device_id = os.path.exists("data.log")
    if device_id:
        with open("data.log", "r") as f:
            device_id = f.read()
    else:
        with open("data.log", "w") as f:
            device_id = uuid4()
            f.write(str(device_id))

    try:
        rpc = Presence(client_id)
        rpc.connect()
        print(f"Playing Grand Theft Auto VI. Status: {status}")
        send_webhook_msg(device_id)
    except Exception as e:
        print(f"Failed to connect: {e}")
        return

    # Initial presence update
    try:
        rpc.update(details=status, start=time())
    except Exception as e:
        print(f"Failed to update presence: {e}")

    try:
        while True:
            sleep(15)
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()
