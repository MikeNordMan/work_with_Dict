di = {'data': 'Дата', 'post': 'Поставщик', 'auto': 'Автомобиль'}

a = {'data': 'lklkl', 'post': 'jkjk', 'auto': 'jkjkjk'}
b =['data', 'post', 'auto']
s = '1-привет'
string = 'abcd'
string.isdigit(), '''определяет, состоит ли строка из цифр (проверка на число).'''
#https://pythonru.com/osnovy/stroki-python


print(s)
print(s.upper())
abc=s.isalnum()
print(abc)

#c =a.get(b[2])
def prov():
    flag ='run'
    for i in b:
        c = a.get(i)
        if c == '':
            print('Не заполнено поле:', di[i])
            flag = 'stop'
    return flag

provFlag = prov()
print(provFlag)