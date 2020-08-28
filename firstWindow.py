import PySimpleGUI as sg
from mainWindow import openMineWindow
strA ='tt1'
strB ='tt'


eventArr = ['vesN1', 'vesN2']
valuesKeys = ['ves', 'zasor']

def getAvailableLetters(s, lettersGuessed):
    k = list(s)
    # print('List ', k)
    # print(lettersGuessed)
    for c in lettersGuessed:
        try:
            k.remove(c)
        except ValueError:
            pass
    print(''.join(k))
    return ''.join(k)

def mySumm(a,b):
    c =int(a) + int(b)
    return str(c)

def findEvent(findElement):
    for i in eventArr:
        if i == findElement:
            print('Yes', findElement)
            return findElement

def createVal(res):
    a = []
    for i in res:
        a.append(values[i])
    res = mySumm(a[0],a[1])
    return res

def abcd(findElement):
    print('Функция ABCD - запущена')
    s = getAvailableLetters(findElement, 'vesN')
    res = []
    for i in valuesKeys:
        res.append(i + s)
    print(createVal(res))
    a = createVal(res)
    print('ключь', findElement)
    firstWindow[findElement].Update(a)
    return res




layout = [
          [sg.Text('Начало работы приложеия')],
          [sg.Text('Вес Брутто'), sg.Text('Засор'), sg.Text('Вес Нетто')],
          [sg.InputText('', key='ves1', size=(25, 1)),
           sg.InputText('0', key='zasor1', size=(25, 1)),
           sg.Text('', enable_events=True, background_color='white',text_color='black', key='vesN1', size=(25, 1))],
          [sg.InputText('', key='ves2', size=(25, 1)), sg.InputText('0', key='zasor2', size=(25, 1)),
           sg.Text('', enable_events=True, background_color='white',text_color='black', key='vesN2', size=(25, 1))],
          [sg.Button('Поехали', key='-ok-'), sg.Button('Выход', key='-exit-'), sg.Button('Подсчет', key='sum')]
         ]


firstWindow = sg.Window('Первое окно', layout)


while True:
    event, values = firstWindow.read()


    if event in (None, '-exit-'):
        break

    if event =='-ok-':
        firstWindow.close()
        openMineWindow()
    if event == findEvent(event):
        print('Работаем')
        abcd(event)
        #firstWindow['vesN1'].Update('254')


    print(event)

firstWindow.close()


