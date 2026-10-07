WATER_PER_KG = 30  # 30 миллилитров на килограмм

user_name = input("Здравствуйте, подскажите как вас зовут? ")
user_name = user_name.title()  # Выводим имя с заглавной буквы
print("Приятно познакомится", user_name)

while True:  # Проверяем ввел ли пользователь число, а не текст
    age = input("Cколько вам лет? ")
    try:
        user_age = int(age)
        break
    except ValueError:  # При ошибке, росим попробовать ввести возраст числом
        print("Попробуй еще раз, введи число")

weight = input("Какой у вас вес в килограммах? ")
user_weight = int(weight)  # Переводим текс в число

height = input("Какой у вас рост в сантиметрах? ")
user_height_cm = int(height)  # Переводим текс в число
user_height_m = user_height_cm / 100  # Переводим в метры

bmi = user_weight / (user_height_m ** 2)  # Рассчет индекса массы тела
user_bmi = round(bmi, 1)  # Округляем результат

water_ml = user_weight * 30  # Рассчитываем норму воды
water_l = water_ml / 1000  # Переводим в литры
user_water = round(water_l, 1)  # Округляем

print()
print("Отчет на основе ваших данных:")
print()
print(f"Ваше имя: {user_name}")
print(f"Возраст: {user_age}")
print(f"Ваш индекс массы тела: {user_bmi}")
print(f"Рекомендованное потребление воды: {water_l} в день")
print()
print("Отчет полностью готов, следите за здоровьем и будте здоровы!")
