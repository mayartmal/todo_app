def logic():
    while True:
        # get user action and remove space from user action string
        user_action = input("Type 'add', 'edit', 'complete' or 'show/display' or 'exit': ")
        user_action = user_action.strip()
        match user_action:
            case "add":
                todo = input("Enter a todo: ") + "\n"
                file = open('files/todos.txt', 'r')
                todos = file.readlines()
                file.close()
                todos.append(todo)
                file = open('files/todos.txt', 'w')
                file.writelines(todos)
                file.close()
            case "show" | "display":
                file = open('files/todos.txt', 'r')
                todos = file.readlines()
                file.close()
                # below is the way to remove \n from hole list with comprehensions
                # new_todos = [item.strip('\n') for item in todos]
                # !!! here is list comprehensions logic
                # format  new var = [item.action() for item in items]
                # new_todos = []
                # for t in todos:
                #     new_todos.append(t.strip('\n'))
                for i, t in enumerate(todos):
                    t = t.strip('\n')
                    row = f"{i+1}) {t.title()}"
                    print(row)
            case "edit":
                file = open('files/todos.txt', 'r')
                todos = file.readlines()
                if len(todos) == 0:
                    print("Nothing to edit")
                else:
                    todo_number = int(input("Input number of todo to edit: ")) - 1
                    print("Existing todo is:", todos[todo_number])
                    new_todo = input("Enter a new todo: ")
                    todos[todo_number] = new_todo
            case 'complete':
                file = open('files/todos.txt', 'r')
                todos = file.readlines()
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