from views import *

def main():
    print('1- Показать весь список, 2- Внести в список новый товар, 3- Показать один продукт, 4- Обновить данные, 5- Удалить товар')
    choice = input('Что вы хотите сделать?: ')
    if choice == '1':
        print(get_data())
    elif choice == '2':    
        print(create())
    elif choice == '3':    
        print(retrieve())    
    elif choice == '4':    
        print(update()) 
    elif choice == '5':    
        print(delete())     
    else:
        print('Нет такой команды!')

main()
while True:
    question = input('Хотите продолжить? [yes/no]: ').lower()
    if question == 'yes':
        main()
    elif question == 'no':
        print('До свидания!')
        break
    else:
        print('Неверная команда!', question)
        