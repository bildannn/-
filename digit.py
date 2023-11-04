#1
# import random
#
#
# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def play_random_track(self):
#         random_track = random.choice(self.tracklist)
#         print("Рандомный трек:", random_track)
#
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# print("Название:", album4.title)
# print("Исполнитель:", album4.artist)
# print("Год:", album4.release_year)
# print("Жанр:", album4.genre)
# print("Треки:", album4.tracklist)
# album4.play_random_track()



#2
# class Student:
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
#
# student2 = Student("Влад", 15, "6", [5, 4, 4, 3, 5])
# print("Имя:", student2.name)
# print("Возраст:", student2.age)
# print("Класс:", student2.grade)
# print("Оценки:", *student2.scores)
# print("Средний балл:", student2.average_score())



#3
# class Recipe:
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         print("Список ингредиентов для блюда: ", self.name)
#         for ingredient in self.ingredients:
#             print(ingredient)
#
#     def cook(self):
#         print("Готовим блюдо", self.name)
#         print("Блюдо", self.name, "готово!" '\n')
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# spaghetti.print_ingredients()
# spaghetti.cook()
#
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
# cake.print_ingredients()
# cake.cook()


#4
# class Publisher:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#
#     def get_info(self):
#         print(f'Издательство: {self.name}')
#         print(f'Расположение: {self.location}')
#
#     def publish(self, message):
#         print(f'Готовим \"{message}\" к публикации в {self.name} ({self.location})')
#
#
# class BookPublisher(Publisher):
#     def __init__(self, name, location, num_authors):
#         super().__init__(name, location)
#         self.num_authors = num_authors
#
#     def publish(self, title, author):
#         super().publish(title)
#         print(f"Передаем рукопись '{title}', написанную автором {author} в издательство {self.name} ({self.location})")
#
#
# class NewspaperPublisher(Publisher):
#     def __init__(self, name, location, num_pages):
#         super().__init__(name, location)
#         self.num_pages = num_pages
#
#     def publish(self, article):
#         super().publish('Свежий номер')
#         print(f'Печатаем {self.num_pages} страниц со статьей \"{article}\" на главной странице в издательстве {self.name} ({self.location})')
#
#
# publisher = Publisher('АБВГД Пресс', 'Москва')
# publisher.publish('Справочник писателя')
#
# book_publisher = BookPublisher('Важные Книги', 'Самара', 52)
# book_publisher.publish('Приключения Чебурашки', 'В.И. Пупкин')
#
# newspaper_publisher = NewspaperPublisher('Московские вести', 'Москва', 12)
# newspaper_publisher.publish('Новая версия Midjourney будет платной')



#5
# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.__balance = balance
#         self.__interest_rate = interest_rate
#         self.__transactions = []
#
#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append(f"Внесение наличных на счет: {amount}")
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f"Снятие наличных: {amount}")
#         else:
#             print("Недостаточно средств на счете")
#
#     def add_interest(self):
#         interest = self.__balance * self.__interest_rate
#         self.__balance += interest
#         self.__transactions.append(f"Начислены проценты по вкладу: {interest}")
#
#     def history(self):
#         for transaction in self.__transactions:
#             print(transaction)
#
# account = BankAccount(100000, 0.05)
# account.deposit(15000)
# account.withdraw(7500)
# account.add_interest()
# account.history()



#6
# class Employee:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#         self.__bonus = None
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_bonus(self, bonus):
#         self.__bonus = bonus
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def get_total_salary(self):
#         return self.__salary + self.__bonus
#
#
# employee = Employee('Марина Арефьева', 30, 90000)
# employee.set_bonus(15000)
#
# print('Имя:', employee.get_name())
# print('Возраст:', employee.get_age())
# print('Зарплата:', employee.get_salary())
# print('Бонус:', employee.get_bonus())
# print('Итого начислено:', employee.get_total_salary())



#7
# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(f'{self.name}: подает голос')
#
#     def move(self):
#         print(f'{self.name}: Двигается')
#
# class Dog(Animal):
#     def __init__(self, name, species, legs, breed):
#         super().__init__(name, species, legs)
#         self.breed = breed
#
#     def bark(self):
#         print(f'{self.breed} {self.name}: лает')
#
#
# class Bird(Animal):
#     def __init__(self, name, species, legs, wingspan):
#         super().__init__(name, species, legs)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(f'{self.species} {self.name}: летит')
#
# dog = Dog('Геральт', 'доберман', 4, 'доберман')
# bird = Bird('Вася', 'попугай', 2, 'средний')
#
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()



#9
# class Candy:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
# class Chocolate(Candy):
#     def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
#         super().__init__(name, price, weight)
#         self.cocoa_percentage = cocoa_percentage
#         self.chocolate_type = chocolate_type
#
# class Gummy(Candy):
#     def __init__(self, name, price, weight, flavor, shape):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.shape = shape
#
# class HardCandy(Candy):
#     def __init__(self, name, price, weight, flavor, filled):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.filled = filled
#
# chocolate = Chocolate(name='Швейцарские луга', price=325.50, weight=220, cocoa_percentage=40, chocolate_type='молочный')
# gummy = Gummy(name ='Жуй-жуй', price=76.50, weight=50, flavor='вишня', shape='медведь')
# hard_candy = HardCandy(name='Crazy Фрукт', price=35.50, weight=25, flavor='манго', filled=True)
#
# print('Шоколадные конфеты:')
# print(f'Название конфет: {chocolate.name}')
# print(f'Стоимость: {chocolate.price} руб')
# print(f'Вес брутто: {chocolate.weight} г')
# print(f'Процент содержания какао: {chocolate.cocoa_percentage}')
# print(f'Тип шоколада: {chocolate.chocolate_type}')
# print('\nМармелад жевательный:')
# print(f'Название конфет: {gummy.name}')
# print(f'Стоимость: {gummy.price} руб')
# print(f'Вес брутто: {gummy.weight} г')
# print(f'Вкус: {gummy.flavor}')
# print(f'Форма: {gummy.shape}')
# print('\nФруктовые леденцы:')
# print(f'Название конфет: {hard_candy.name}')
# print(f'Стоимость: {hard_candy.price} руб')
# print(f'Вес брутто: {hard_candy.weight} г')
# print(f'Вкус: {hard_candy.flavor}')
# print(f'Начинка: {hard_candy.filled}')



#10
# class Soldier:
#     def __init__(self, name, rank, service_number):
#         self.name = name
#         self.__rank = rank
#         self.__service_number = service_number
#
#     def get_rank(self):
#         print(f'Персонаж {self.name} имеет звание {self.__rank}')
#
#     def confirm_service_number(self):
#         print(f'Порядковый номер {self.__service_number} подтвержден')
#
#     def promote(self):
#         if self.__rank == 'рядовой':
#             self.__rank = 'ефрейтор'
#             print(f'{self.name} повышен в звании, он теперь {self.__rank}')
#         else:
#             print(f'{self.name} уже имеет высшее звание')
#
#     def demote(self):
#         if self.__rank == 'ефрейтор':
#             self.__rank = 'рядовой'
#             print(f'{self.name} понижен в звании, он теперь {self.__rank}')
#         else:
#             print(f'{self.name} уже имеет наивысшее звание')
#
#
# soldier1 = Soldier('Иван Сусанин', 'рядовой', '12345')
# print(f"Создан новый игровой персонаж типа Soldier с атрибутами: {vars(soldier1)}")
# soldier1.get_rank()
# soldier1.confirm_service_number()
# soldier1.promote()
# soldier1.demote()