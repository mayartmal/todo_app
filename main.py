
todos = list()

def logic():
    while True:
        user_action = input("Type 'add' or 'show/display' or 'exit': ")
        user_action = user_action.strip()

        match user_action:
            case "add":
                todo = input("Enter a todo: ")
                todos.append(todo)
            case "show" | "display":
                for i, t in enumerate(todos):
                    print(f"{i+1}) ", t.title())
            case "edit":
                if len(todos) == 0:
                    print("Nothing to edit")
                else:
                    todo_number = int(input("Input number of todo to edit: ")) - 1
                    print("Existing todo is:", todos[todo_number])
                    new_todo = input("Enter a new todo: ")

                    todos[todo_number] = new_todo
            case 'complete':
                if len(todos) == 0:
                    print("Nothing to complete")
                else:
                    todo_number = int(input("Input number of todo to complete: ")) - 1
                    todos.pop(todo_number)

            case "exit":
                break
            case _:
                print("Unknown command...")




if __name__ == '__main__':
    logic()