import functions
import time

now = time.strftime("%b %d, %Y %H : %M : %S")
print("It is", now)

while True:
    useraction = input("type add, show, edit, complete or exit:")
    useraction = useraction.strip()

    
    if useraction.startswith("add"):
        todo = useraction[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif useraction.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif useraction.startswith("edit"):
        try:
            num = int(useraction[5:])
            num = num - 1 

            todos = functions.get_todos()
            new_todo =  input("correct your todo: ")
            todos[num] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue

    elif useraction.startswith("complete"):
        try:
            num = int(useraction[9:])

            todos = functions.get_todos()

            index = num - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except ValueError:
            print("no todo on this number")
            continue
    elif useraction.startswith("exit"):
        break             
    else:
        print('command is not valid')
print("boye")