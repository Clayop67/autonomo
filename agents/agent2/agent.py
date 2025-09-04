from agents import utils
from datetime import datetime

def main():
    agent_name = "Agent2"
    messages = utils.read_messages()
    count = len(messages)
    now = datetime.now().isoformat(sep=' ', timespec='seconds')
    utils.log(f"{agent_name} processed {count} messages at {now}")
    utils.write_message(agent_name, f"Agent2 logged {count} messages at {now}")
    print(f"{agent_name} logged and replied.")

if __name__ == "__main__":
    main()
