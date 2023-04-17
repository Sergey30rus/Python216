# Задание 1. Реализуйте класс «Автомобиль».
class Car:
    def __init__(self, model_name, year, manufacturer, volume, color, price):
        self.model_name = model_name
        self.year = year
        self.manufacturer = manufacturer
        self.volume = volume
        self.color = color
        self.price = price

    def set_info(self):
        self.model_name = input('Введите название модели: ')
        self.year = int(input('Введите год выпуска: '))
        self.manufacturer = input('Введите название производителя: ')
        self.volume = input('Введите объем двигателя: ')
        self.color = input('Введите цвет машины: ')
        self.price = input('Введите цену машины: ')

    def print_info(self):
        print(f'Название модели: {self.model_name}')
        print(f'Год выпуска: {self.year}')
        print(f'Название производителя: {self.manufacturer}')
        print(f'Объем двигателя: {self.volume}')
        print(f'Цвет машины: {self.color}')
        print(f'Цена машины: {self.price}')

hyundai = Car(model_name='Hyundai', year=2017, manufacturer='Hyundai Motor Corp.', volume='2.2', color='white',
              price='28750 USD')
print(hyundai.color)

# Задание 2. Реализуйте класс «Книга».
class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_info(self):
        self.name = input('Введите название книги: ')
        self.year = int(input('Введите год выпуска книги: '))
        self.publisher = input('Введите название издателя: ')
        self.genre = input('Введите жанр книги: ')
        self.author = input('Введите автора книги: ')
        self.price = input('Введите цену книги: ')

    def print_info(self):
        print(f'Название книги: {self.name}')
        print(f'Год выпуска книги: {self.year}')
        print(f'Название издателя: {self.publisher}')
        print(f'Жанр книги: {self.genre}')
        print(f'Автор книги: {self.author}')
        print(f'Цена книги: {self.price}')

book = Book(name='Ромео и Джульетта', year=1597, publisher='Неизвестен', genre='Трагедия', author='Уильям Шекспир',
              price='10 USD')

# Задание 3. Реализуйте класс «Стадион».
class Stadium:
    def __init__(self, name, date, country, city, capacity):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def set_info(self):
        self.name = input('Введите название стадиона: ')
        self.date = input('Введите дату открытия стадиона: ')
        self.country = input('Введите название страны: ')
        self.city = input('Введите город: ')
        self.capacity = int(input('Введите вместительность стадиона: '))

    def print_info(self):
        print(f'Название стадиона: {self.name}')
        print(f'Дата открытия стадиона: {self.date}')
        print(f'Страна: {self.country}')
        print(f'Город: {self.city}')
        print(f'Вместительность стадиона: {self.capacity}')

stadium = Stadium(name='Олд Траффорд', date='19.02.1910', country='Англия', city='Манчестер',
                  capacity=74310,)

def new_func():
    print('Hello world!')