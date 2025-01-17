def get_todos(filepath='files/todos.txt'):
    """ return todos from text storage file
    returned value is a list
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos
def write_todos(todos, filepath='files/todos.txt'):
    """ writes todos list to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)

if __name__ == '__main__':
    print(get_todos())