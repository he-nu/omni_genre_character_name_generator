import ast
import os


def parse_python_list(model_response:str) -> list:
    """ Takes the string response and returns a list."""

    # The list lies between [ and ]
    open_bracket = "["
    close_bracket = "]"

    # --> open bracket is closer to the start
    for i, ch in enumerate(model_response):
        if ch == open_bracket:
            open_bracket_index = i
            break
    # <-- close bracket is closet to the end
    for i, ch in enumerate(model_response[::-1]):
        if ch == close_bracket:
            close_bracket_index = len(model_response) - i

    list_content = model_response[open_bracket_index:close_bracket_index]
    content_as_list = ast.literal_eval(list_content)

    return content_as_list


def print_from_list(names_list):
    print(os.linesep)
    for i, name in enumerate(names_list, start=1):
        print(f"{i}: {name}")