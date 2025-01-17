# from storage_logic import get_todos, write_todos
import storage_logic

def console_ui():
    while True:
        # get user action and remove space from user action string
        user_action = input("Type 'add todo', 'edit todo number', 'complete todo number' or 'show' or 'exit': ")
        user_action = user_action.strip()
        if user_action.startswith("add"):
            todo = user_action[4:] + '\n'
            todos = storage_logic.get_todos()
            todos.append(todo)
            storage_logic.write_todos(todos)
        elif user_action.startswith("show"):
            todos = storage_logic.get_todos()
            for i, t in enumerate(todos):
                t = t.strip('\n')
                row = f"{i+1}) {t.title()}"
                print(row)
        elif user_action.startswith("edit"):
            try:
                todos = storage_logic.get_todos()
                todo_number = int(user_action[5:]) - 1
                print("Existing todo is:", todos[todo_number])
                new_todo = input("Enter a new todo: ") + "\n"
                todos[todo_number] = new_todo
                storage_logic.write_todos(todos)
            except ValueError:
                print("Your command in not valid")
                continue
        elif user_action.startswith("complete"):
            try:
                todos = storage_logic.get_todos()
                todo_number = int(user_action[9:]) - 1
                completed_todo = todos[todo_number]
                todos.pop(todo_number)
                storage_logic.write_todos(todos)
                message = f'Todo "{completed_todo.strip('\n').title()}" was completed'
                print(message)

            except IndexError:
                print("Wrong number of a todo item")
                continue
        elif user_action.startswith("exit"):
            break
        else:
            print("Unknown command...")


if __name__ == '__main__':
    console_ui()