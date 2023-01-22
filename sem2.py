import json
import yaml

def open_files():  #Функция преобразования файлов json в словари
    try:
        with open('first.json') as file1:
            dict_1 = json.load(file1)   #открываем первый файл и преобразуем в словарь. Чтобы поддерживались файлы типа не только json, но и yaml, используем try except.
        dict_1 = dict(sorted(dict_1.items(), key=lambda x: x[0]) )


    except FileNotFoundError:
        with open('first.yaml') as file1:
            dict_1 = yaml.safe_load(file1)   
        dict_1 = dict(sorted(dict_1.items(), key=lambda x: x[0]) )


    try:
        with open('second.json') as file2:
            dict_2 = json.load(file2)        # точно так же делаем со вторым файлом
        dict_2 = dict(sorted(dict_2.items(), key=lambda x: x[0]) )    


    except FileNotFoundError:
        with open('second.yaml') as file2:
            dict_2 = yaml.safe_load(file2)
        dict_2 = dict(sorted(dict_2.items(), key=lambda x: x[0]) )
    return(dict_1,dict_2)


def difference(dict_1,dict_2): #функция нахождения различий
    result = ''
    for key in dict_1:  #с помощью рекурсии мы проверяем изменения вложенных ключей 
        if key in dict_2:
            if type(dict_1[key]) is dict:
                result += difference(dict_1[key],dict_2[key])
                
    for key in list(dict_1): #проверяем какие ключи были удалены из первого  файла
        if key not in dict_2:
            result += f'Ключ {key} удален\n'
            dict_1.pop(key)

    for key in dict_2:  # проверяем какие ключи были добавлены во второй  файл
        if key not in dict_1 and type(dict_2[key]) is not dict:
            result += f'Ключ {key} добавлен: {dict_2.get(key)}\n'

    for key in dict_1:    # проверяем какие ключи были изменены
        if dict_1.get(key)!=dict_2.get(key) and type(dict_1[key]) is not dict:
            result += f'Ключ {key} изменён. Было {dict_1.get(key)}. Стало {dict_2.get(key)}\n' # после выполнения данных циклов мы получаем строку в которой написаны все изменения наших файлов
                                                                                        
    while result.__contains__('\n\n'):                                                 
        result = result.replace('\n\n','\n') 
    result = result.split('\n')
   
    result = '\n'.join(result)       
    return result


def create_file(result):           # данная функция преобразовывает нашу строку в txt файл
    result_list = sorted(list(result.split('\n'))) # сортируем наши изменения по ключам
    result = '\n'.join(result_list)
    result_str = "" 
   
    for i in range(1, len(result)): 
        result_str = result_str + result[i] 

    result_file = open('result.txt', 'w')
    result_file.write(result_str)           # создаем txt файл
    result_file.close()
    return result_file

dict_1,dict_2 = open_files()
result = difference(dict_1,dict_2)
print(create_file(result))


