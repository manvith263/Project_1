#imagegui.py

import PySimpleGUI as sg

layout = [[sg.Text("Upload impage here")], [sg.Button("OK")]]

#create a window

window = sg.Window("Demo", layout)

#create an event loop
while True:
    event, value = window.read()
    #end program if user closes window or
    #press the ok button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

    window.close()
