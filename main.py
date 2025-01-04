
todos = list()

def logic():
    while True:
        user_action = input("Type 'add' or 'show' or 'exit': ")

        match user_action:
            case "add":
                todo = input("Enter a todo: ")
                todos.append(todo)
            case "show":
                print(todos)
            case "exit":
                break



if __name__ == '__main__':
    logic()