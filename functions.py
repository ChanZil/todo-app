FILEPATH = "files/todo.txt"


def get_todos(file_path=FILEPATH):
    """Read a text file and return the list of
    to-do items.
    """
    with open(file_path, 'r') as local_file:
        new_todos = local_file.readlines()
    return new_todos


def write_todos(todo_arg, file_path=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(file_path, 'w') as local_file:
        local_file.writelines(todo_arg)



