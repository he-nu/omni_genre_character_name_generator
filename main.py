import modules.functions as foos

import os
import subprocess

import ollama

def initiate_server_screen():
    session_name = "ollama_name_gen"
    com_ = "ollama serve"

    command = f"screen -dmLS {session_name} {com_}"
    # Run the command in screen
    subprocess.run(command, shell=True)

def stop_server_screen():
    session_name = "ollama_name_gen"
    command = f"screen -X -S {session_name} quit"
    subprocess.run(command, shell=True)


def ask_userinput() -> tuple:
    nickname = input("Input, nickname (optional): ")
    genre = input("Input genre: ")
    return nickname, genre

def generate_nicknames(user_choices):
    nickname, genre = user_choices
    if nickname:
        prompt_ = f"Generate 5 suggestions for the name '{nickname}'. Use the genre of {genre}. Return your answer as a python list and only the python list"
    else:
        prompt_ = f"Generate 5 suggestions for a name from the world of {genre}. Return your answer as a python list and only the python list"

    response = ollama.chat(model='phi3', messages=[
        {
            'role': 'user',
            'content': prompt_
        }
        ])

    message = response['message']['content']
    parsed_names_list = foos.parse_python_list(message)
    return parsed_names_list


def main():
    # Starts the server as a background process
    initiate_server_screen()

    wants_to_continue = True
    while wants_to_continue:
        print(os.linesep)
        user_choice = ask_userinput()
        names_list = generate_nicknames(user_choice)
        foos.print_from_list(names_list=names_list)
        print(os.linesep)
        ask_to_continue = input("Do you want to continue? y/n: ")
        print(os.linesep)

        if ask_to_continue == "y":
            continue
        else:
            break

    # Stops the sever
    stop_server_screen()

    return None


if __name__ == "__main__":
    main()