import PySimpleGUI as sg
class MyWindow():
    def __init__(self, window):
        self.window =window

    layout = [
        [sg.Text('Поступление')],
        [sg.Button('Выход', key='-exit-')]
    ]


    def returnLayout(self):
        pass


    def startWindow(self):
        self.window.Hide()
        windowClass =sg.Window('Окно',self.layout)
        while True:
            event, values = windowClass.read()

            if event in (None, '-exit-'):
                windowClass.close()
                self.window.UnHide()
                break
        windowClass.close()

