from agents import utils
from datetime import datetime

if __name__ == "__main__":
    # Nettoyage automatique avant de lire/écrire
    utils.clean_messages()

    messages = utils.read_messages()
    print(f"Agent1 lit {len(messages)} message(s) :")
    for m in messages:
        print(m.strip())

    now = datetime.now().isoformat(sep=' ', timespec='seconds')
    msg = f"Agent1 ack at {now} (read {len(messages)} messages)"
    utils.write_message("Agent1", msg)
    utils.log(f"Agent1 executed at {now}")
    print("Agent1 a répondu.")
