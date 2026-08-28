import subprocess

# version
version = {
    "__comment__": "major.minor.update.commit",
    "__version__": "1.2.0.13",
    "status": "Stable"
}


# Constants
CONFIG_PATH = "config.json"
DEFAULT_CLIENT_ID = "1542855976913207296" # GTAVI App

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
