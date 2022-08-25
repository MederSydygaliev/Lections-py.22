import json

FILE_PATH = 'laptops.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id

def create():
    data = get_data()
    laptop = {
        'id':get_id(),
        'Brand': input('введите название бренда: '),
        'Model': input('введите модель ноутбука: '),
        'Year_of_release': int(input('введите год выпуска: ')),
        'Description': input('введите описание: '),
        'price': float(input('введите цену: '))
    }
    data.append(laptop)
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'Товар успешно добавлен в базу данных!'

def retrieve():
    data = get_data()
    id = int(input('введите id товара: '))
    laptop = list(filter(lambda x: x['id'] == id, data))
    if not laptop:
        return 'нет такого товара!'
    else:
        return laptop [0]

def update():
    data = get_data()
    flag = False
    id = int(input('введите id товара: '))
    laptop = list(filter(lambda x: x['id'] == id, data))
    if not laptop:
        return 'такого товара нет в нашем списке!'
    index_ = data.index(laptop[0])
    choice = input('что вы хотите изменить? \n1 - Бренд \n2 - Модель \n3 - Год выпуска \n4 - Описание товара \n5 - Цена \nВыберите операцию: ')
    if choice == '1':
        data[index_]['Brand'] = input('введите название бренда: ')
        flag = True
    elif choice == '2':    
        data[index_]['Model'] = (input('введите модель ноутбука: '))
        flag = True
    elif choice == '3':    
        data[index_]['Year_of_release'] = int(input('введите год выпуска: '))
        flag = True
    elif choice == '4':    
        data[index_]['Description'] = (input('введите описание ноутбука: '))
        flag = True
    elif choice == '5':    
        data[index_]['price'] = float(input('введите цену: '))
        flag = True
    else:
        print('вы ввели неверные данные!')

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    if flag:
        return 'Товар успешно обновлён!'
    else:
        return 'Ошибка обновления'

def delete(): 
    data = get_data()
    id = int(input('введите id для удаления: '))
    laptop = list(filter(lambda x: x['id'] == id, data))
    if not laptop:
        return 'нет такого товара!'
    index_ = data.index(laptop[0])
    data.pop(index_)
    json.dump(data, open(FILE_PATH, 'w'))
    return 'DELETED'