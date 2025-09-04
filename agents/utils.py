# utils.py
# Fonctions communes pour tous les agents

def log(message, filename="log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def write_message(agent_name, message, filename="messages.txt"):
    """
    Permet à un agent d'écrire un message dans un fichier commun.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{agent_name}: {message}\n")

def read_messages(filename="messages.txt"):
    """
    Retourne tous les messages dans le fichier.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
