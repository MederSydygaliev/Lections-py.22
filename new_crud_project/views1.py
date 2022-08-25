# CRUD
# C - create
# R - retrieve
# U - update
# D - delete


data = [
    {'id': 1, 'title': 'Redmi Note 10', 'price': 25000, 'description': 'shit phone'},
    {'id': 2, 'title': 'Samsung Galaxy Fold', 'price': 55000,'description': 'good phone'},
    {'id': 3, 'title': 'Iphone 13 pro', 'price': 220000,'description': 'great phone'}
]

def get_id():
    id = data[-1]['id']
    id += 1
    return id
print(get_id())
# def create_product():
#     product = {
#         'id': get_id(), 'title': input('Введите название продукта: '), 'price': float(input('Введите цену: ')), 
#         'description': input('Введите описание: ')
#     }
#     data.append(product)
#     print('Created!')

# def list_of_products():
#     for product in data:
#         print('Id of product: ', product['id'])
#         print('Title: ', product['title'])
#         print()

# def detail_retrieve():
#     id_product = int(input('Введите id продукта: '))
#     try:
#         product = list(filter(lambda x: x['id'] == id_product, data )) [0]
#     except IndexError:
#         print('Такого продукта нет!')
#     else:
#         print('Id: ', product['id'])
#         print('Title: ', product['title'])    
#         print('Price: ', product['price'])    
#         print('Description: ', product['description'])
#         print()    

        
# def update_product():
#     id_product = int(input('Введите id продукта: '))
#     flag = False
#     try:
#         product = list(filter(lambda x: x['id'] == id_product, data))[0]
#     except IndexError:
#         print('Такого продукта нет!')
#     else:
#         index = data.index(product)
#         choice = int(input('Что изменить? (1- title, 2- price, 3- description): '))
#         if choice == 1:
#             data[index]['title'] = input('введите новый title: ')
#             flag = True
#         elif choice == 2:
#             data[index]['price'] = input('введите новый price: ')
#             flag = True
#         elif choice == 3:
#             data[index]['description'] = input('введите новый description: ')
#             flag = True
#         else:
#             print('Некорректный выбор!')
#     if flag:
#         print('successfully updated!')
#     else: 
#         print('not updated!')

# def delete_product():
#     id_product = int(input('Введите id продукта: '))
#     flag = False
#     try:
#         product = list(filter(lambda x: x['id'] == id_product, data))[0]
#     except IndexError:
#         print('Такого продукта нет!')
    
#     else:
#         index = data.index(product)
#         deleted = data.pop(index)
#         flag = True
#     if flag:
#         print('successfully deleted!')
#     else:
#         print('not deleted!')