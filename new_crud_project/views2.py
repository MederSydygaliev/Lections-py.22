import json

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def get_one_product():
    data = get_data()
    id = int(input('введите id продукта: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'нет такого продукта!'
    else:
        return product [0]


def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id

def create_product():
    data = get_data()
    product = {
        'id':get_id(),
        'title': input('введите название продукта: '),
        'price': float(input('введите цену: '))
    }
    data.append(product)
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'CREATED'

def update_product():
    data = get_data()
    flag = False
    id = int(input('введите id продукта: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'нет такого продукта!'
    index_ = data.index(product[0])
    choice = input('что вы хотите изменить: 1 - title, 2 - price')
    if choice == '1':
        data[index_]['title'] = input('введите новое название продукта: ')
        flag = True
    elif choice == '2':    
        data[index_]['price'] = float(input('введите новую цену: '))
        flag = True
    else:
        print('вы ввели неверные данные!')

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    if flag:
        return 'UPDATED'
    else:
        return 'UPDATE FAIL'

def delete_product():
    data = get_data()
    id = int(input('введите id для удаления: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'нет такого продукта!'
    index_ = data.index(product[0])
    data.pop(index_)
    json.dump(data, open(FILE_PATH, 'w'))
    return 'DELETED'