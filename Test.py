


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

class ElDict(TestDict):

    '''Конструктор'''
    def __init__(self, myDict, key, valEement):
        #super().__init__(self.myDict)
        self.myDict = myDict
        self.key = key
        self.valElement = valEement

    '''Добавление в словарь элемента'''
    def addElementDict(self):
        print('Получилось')
        pass

    ''' Удаление элементо Словаря '''
    def delitElemrntDict(self):
        pass


a ={'Name':'Mark', 'Фамиля':'Иванов', 'Sex':'man'}

#
# first = TestDict(a)
# first.returnKey()
# first.returnData()
twice = ElDict(a, 'Имя', 'Миша')
twice.returnData()