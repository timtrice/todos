FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text files and return the list of todos
    :param filepath:
    :return:
    """
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """
    Write the todo items to a text file.
    :param filepath:
    :param todos:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos)


if __name__ == "__main__":
    pass
