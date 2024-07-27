import FreeSimpleGUI as sg
import functions

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

windows = sg.Window('To-Do App', 
                    layout=[[label], [input_box, add_button]], 
                    font=('Helvetica', 20))
while True:
    event, values = windows.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
windows.close()
