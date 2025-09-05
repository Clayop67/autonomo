from agents import utils
from datetime import datetime

if __name__ == "__main__":
    # Nettoyage automatique avant d’écrire
    utils.clean_messages()

    now = datetime.now().isoformat(sep=' ', timespec='seconds')
    msg = f"Hello from Agent0! {now}"
    utils.write_message("Agent0", msg)
    utils.log(f"Agent0 started at {now}")
    print(msg)
