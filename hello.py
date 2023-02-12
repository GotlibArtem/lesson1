# Файлы*.py
print('Привет мир!')

print('Привет программист!')
print(2 + 2)
print(10 / 3)

# Переменные
name = 'Артем'
print(name)

# Простые типы данных
v = input('Введите число от 1 до 10: ')
print(int(v) + 10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

print("float('1'):", float('1'))
try:
    print("int('2.5'):", int('2.5'))
except ValueError as err:
    print("ValueError for int('2.5'):", err)
print("bool(1):", bool(1))
print("bool(''):", bool(''))
print("bool(0):", bool(0))

# Комплексные типы данных: списки
x = [3, 5, 7, 9, 10.5]
print(f'Изначальный список: {x}')
x.append('Python')
print(f'Длина нового списка: {len(x)}')
print(f'Начальный элемент списка: {x[0]}')
print(f'Последний элементи списка: {x[-1]}')
print(f'Элементы списка со 2-го по 4-й включительно: {x[1:4]}')
x.remove('Python')

# Комплексные типы данных: словари
x = {'city': 'Москва', 'temperature': '20'}
print(f"Зачение ключа 'city': {x['city']}")
x['temperature'] = int(x['temperature']) - 5
print(f'Словарь: {x}')
print(f"Ключ 'country': {x.get('country', 'Такой ключ отсутствует!')}")
x['country'] = 'Россия'
x['date'] = '27.05.2019'
print(f'Длина словаря: {len(x)}')