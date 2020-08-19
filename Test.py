


class TestDict():

    '''Конструктор'''
    def __init__(self, myDict):
        self.myDict = myDict

    '''Возвращение Массива ключей'''
    def returnKey(self):
        arrKeys = []
        for key in self.myDict:
            arrKeys.append(key)
        return arrKeys

    '''Возврашение массива данных'''
    def returnData(self):
        arrData = []
        for key in self.myDict:
            arrData.append(self.myDict[key])
        print(arrData)

    '''Добавление в словарь элемента'''
    def addElementDict(self):
        pass

    ''' Удаление элементо Словаря '''
    def delitElemrntDict(self):
        pass


a ={'Name':'Mark', 'Фамиля':'Иванов', 'Sex':'man'}


first = TestDict(a)
first.returnKey()
first.returnData()
