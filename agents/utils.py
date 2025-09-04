# utils.py
# Fonctions communes pour tous les agents

def log(message, filename="log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(message + "\n")
