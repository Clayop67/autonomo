from agents import utils
from datetime import datetime

def main():
    agent_name = "Agent0"
    now = datetime.now().isoformat(sep=' ', timespec='seconds')
    msg = f"Hello from {agent_name}! {now}"
    utils.write_message(agent_name, msg)
    print(msg)

if __name__ == "__main__":
    main()
