def logic():
    while True:
        # get user action and remove space from user action string
        user_action = input("Type 'add todo', 'edit todo number', 'complete todo number' or 'show' or 'exit': ")
        user_action = user_action.strip()
        if user_action.startswith("add"):
            todo = user_action[4:] + '\n'
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
                todos.append(todo)
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        elif user_action.startswith("show"):
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for i, t in enumerate(todos):
                t = t.strip('\n')
                row = f"{i+1}) {t.title()}"
                print(row)
        elif user_action.startswith("edit"):
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
                if len(todos) == 0:
                    print("Nothing to edit")
                else:
                    # todo_number = int(input("Input number of todo to edit: ")) - 1
                    todo_number = int(user_action[5:]) - 1
                    print("Existing todo is:", todos[todo_number])
                    new_todo = input("Enter a new todo: ") + "\n"
                    todos[todo_number] = new_todo
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        elif user_action.startswith("complete"):
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
                if len(todos) == 0:
                    print("Nothing to complete")
                else:
                    # todo_number = int(input("Input number of todo to complete: ")) - 1
                    todo_number = int(user_action[9:]) - 1
                    completed_todo = todos[todo_number]
                    todos.pop(todo_number)
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            message = f'Todo "{completed_todo.strip('\n').title()}" was completed'
            print(message)
            print("Current to do list is: ")
            for i, t in enumerate(todos):
                t = t.strip('\n')
                row = f"{i+1}) {t.title()}"
                print(row)
        elif user_action.startswith("exit"):
            break
        else:
            print("Unknown command...")




if __name__ == '__main__':
    logic()