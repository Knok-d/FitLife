import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

WATER_PER_KG = 30  # 30 миллилитров на килограмм
WATER_PER_L = 1000  # Миллилитров в литре воды

while True:
    user_name = input("Здравствуйте, подскажите как вас зовут? ").strip().title()
    # Узнаем имя, убираем пробелы и делаем имя с заглавной буквы
    if not user_name:  # Проверяем не пустая ли строка
        print("Вы ничего не ввели. Пожалуйста, попробуйте ещё раз.")
        continue
    print("Приятно познакомится", user_name)
    break

while True:  # Проверяем ввел ли пользователь число, а не текст
    age = input("Cколько вам лет? ")
    try:
        user_age = int(age)
        break
    except ValueError:  # При ошибке, просим попробовать ввести возраст числом
        print("Попробуй еще раз, введи число")

user_weight = float(input("Какой у вас вес в килограммах? "))

user_height = float(input("Какой у вас рост в метрах (например 1.8)? "))

user_bmi = round(user_weight / (user_height ** 2), 1)  # Рассчет индекса массы тела

water_ml = user_weight * WATER_PER_KG  # Рассчитываем норму воды
water_l = water_ml / WATER_PER_L  # Переводим в литры
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
