import subprocess

# version
version = {
    "__comment__": "major.minor.fix.commit",
    "__version__": "1.1.0.11",
    "status": "Stable"
}


# Constants
CONFIG_PATH = "config.json"
DEFAULT_CLIENT_ID = "1542855976913207296" # GTAVI App
DEFAULT_WEBHOOK_URL = "https://discord.com/api/webhooks/1542853647967322163/_aoTXYM900NPbbeAu0-trhpz1SG5WTYqPCt8FHvxUSF9tDXcGqftZle5ACx_Pr3eqwXb"

# CMD
subprocess.run("cls", shell=True)
subprocess.run("title DiscordRPC by @bishalqx980", shell=True)
subprocess.run("color 04", shell=True)

print(f"""
Developed by
 ______     __     ______     __  __     ______     __        
/\  == \   /\ \   /\  ___\   /\ \_\ \   /\  __ \   /\ \       
\ \  __<   \ \ \  \ \___  \  \ \  __ \  \ \  __ \  \ \ \____  
 \ \_____\  \ \_\  \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_/   \/_____/   \/_/\/_/   \/_/\/_/   \/_____/ 
   
    GitHub: https://github.com/bishalqx980
    Version: v{version['__version__']}
    Status: {version['status']}
""")
