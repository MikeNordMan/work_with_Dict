import PySimpleGUI as sg
from window_class import MyWindow
from addWindow import AddWindow


def openMineWindow():


    layout=[
            [sg.Text('Главная страница Приложения')],
            [sg.Button('Окно Поступления', key='-add-')],
            [sg.Button('Окно Реализации', key='-real-')],
            [sg.Button('Окно Переработки', key='-rework-')],
            [sg.Button('Выход', key='-exit-')]
           ]

    mainWindow = sg.Window('Главное окно', layout, size=(250, 250))

    '''Переменные активности'''
    addWindow_active = False
    realWindow_active = False
    reworkWindow_active = False

    while True:
        event, values = mainWindow.read()

        if event in (None, '-exit-'):
            break

        if event =='-add-' and not addWindow_active:
            addWindow_active = True
            mainWindow.Hide()
            #w = AddWindow(mainWindow, 100)
            w = AddWindow(mainWindow)
            w.startWindow()
            addWindow_active = False
            print('add')

        if event =='-real-' and not realWindow_active:
            realWindow_active = True
            #pass
            print('real')
        if event =='-rework-' and not reworkWindow_active:
            realWindow_active =True
            #pass
            print('rework')


    mainWindow.close()