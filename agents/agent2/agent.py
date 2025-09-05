from agents import utils
from datetime import datetime

if __name__ == "__main__":
    # Nettoyage automatique avant de lire/écrire
    utils.clean_messages()

    messages = utils.read_messages()
    count = len(messages)
    now = datetime.now().isoformat(sep=' ', timespec='seconds')
    utils.log(f"Agent2 processed {count} messages at {now}")
    utils.write_message("Agent2", f"Agent2 logged {count} messages at {now}")
    print("Agent2 logged and replied.")
