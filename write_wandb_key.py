import wandb
from wandb.lib import apikey

if __name__ == '__main__':
    wl = wandb.setup()
    settings = wl.settings()
    current_api_key = apikey.api_key(settings=settings)
    with open("wandb.key","w") as f:
        f.write(current_api_key)