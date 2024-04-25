FILEPATH = "main.txt"
def get_todos(file_path=FILEPATH):
    """ Reads To Do List """
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """ Writes To Do List to File """
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
