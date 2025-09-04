from agents import utils
from datetime import datetime

def main():
    agent_name = "Agent1"
    messages = utils.read_messages()
    print(f"{agent_name} lit {len(messages)} message(s) :")
    for m in messages:
        print(m.strip())

    now = datetime.now().isoformat(sep=' ', timespec='seconds')
    utils.write_message(agent_name, f"Agent1 ack at {now} (read {len(messages)} messages)")
    print(f"{agent_name} a répondu.")

if __name__ == "__main__":
    main()
