# run_agents.py (à la racine du projet)
import subprocess
import sys
import os

agents = ["agent0", "agent1", "agent2"]

for agent in agents:
    print(f"\n=== Exécution de {agent} ===")
    module_path = f"agents.{agent}.agent"
    subprocess.run([sys.executable, "-m", module_path], cwd=os.getcwd())
