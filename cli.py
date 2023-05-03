import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    # get user input and strup space chars from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos('files/todo.txt')
        todos.append(todo + '\n')
        functions.write_todos(todos, 'files/todo.txt')

    elif user_action.startswith("show"):
        todos = functions.get_todos('files/todo.txt')
        for i, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{i+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1
            todos = functions.get_todos('files/todo.txt')
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            functions.write_todos(todos, 'files/todo.txt')
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos('files/todo.txt')
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            functions.write_todos(todos, 'files/todo.txt')
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")

lis = [3, 2, 1]
l = [1 , 2]
lis.append(l)





