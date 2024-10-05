#! ../.venv/bin/python3

import subprocess
import time

SESSION = "ollama_phi_loader"

def initiate_server_screen():
    session_name = SESSION
    screen_command = "ollama serve"

    print(f"Starting screen {SESSION}")
    command = f"screen -dmLS {session_name} {screen_command}"
    # Run the command
    subprocess.run(command, shell=True)
    print("Waiting for server...")
    secs = 3
    for s in range(secs):
        print(f": {secs - s}")
        time.sleep(1)


def pull_phi3():
    command = "ollama pull phi3"
    print("Loading phi3")
    subprocess.run(command, shell=True)


def stop_server_screen():
    session_name = SESSION
    command = f"screen -X -S {session_name} quit"
    subprocess.run(command, shell=True)


def main():
    initiate_server_screen()
    pull_phi3()
    stop_server_screen()
    print("Server closed, everything is ready!")

if __name__ == "__main__":
    main()