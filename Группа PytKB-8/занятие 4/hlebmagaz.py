#Хлебобосс открывает магаз. В 3002 году очень туго с 🧠 и приходится обращаться к змеям(🐍)
#Хлебное рабство стало слишком популярно. И теперь каждый богатый хлеб может купить себе парочку рабочих
#Вводится цвет раба. 1) Чёрный хлеб 2) Белый хлеб
#Вводится категория в зависимости от выбора: для ч. х. : 1) С семечками - 3😻 2) Бородинский - 2😻 3) Сверх Мягкий -3😻
# для б. х. : 1) Чиабатта -1😻 2) Багет -1 😻 3) Круасан - 4😻
#Далее вводится количство, и выводится необходимая выплата.

choice = input('Введите номер категории: 1) Чёрный хлеб 2) Белый хлеб ->')

if choice == '1':
    hlebrab = input('Введите номер вывбора: 1) С семечками - 3😻 2) Бородинский - 2😻 3) Сверх Мягкий -3😻->')
    kolvo = int(input('Введите кол-во: '))
    if hlebrab == '1' or hlebrab == '3':
        print(f'С вас {kolvo*3}😻')
    elif hlebrab == '2':
        print(f'С вас {kolvo*2}😻')
    else:
        print('Извинись и переделай! 😾😾😾')
elif choice == '2':
    hlebrab = input('Введите номер вывбора: 1) Чиабатта -1😻 2) Багет -1 😻 3) Круасан - 4😻->')
    kolvo = int(input('Введите кол-во: '))
    if hlebrab == '1' or hlebrab == '2':
        print(f'С вас {kolvo}😻')
    elif hlebrab == '3':
        print(f'С вас {kolvo*4}😻')
    else:
        print('Извинись и переделай! 😾😾😾')
else:
    print('У вас выпало 🧠, так что будет мягким лапушкой и переделай, БЫСТРО! Пока из тебя 🍔 не сделали')