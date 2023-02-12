# Задание 1
def get_summ(one, two, delimiter='&'):
    return (str(one) + delimiter + str(two))

result_summ = get_summ('Learn', 'python')
print(result_summ.upper())


# Задание 2
def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

new_price = format_price(56.24)
print(new_price)