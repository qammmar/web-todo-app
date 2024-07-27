import FreeSimpleGUI as sg
import functions

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

windows = sg.Window('To-Do App', layout=[[label], [input_box, add_button]])
windows.read()
windows.close()
