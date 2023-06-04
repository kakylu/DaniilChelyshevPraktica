def rubles_to_dollars(amount, rate):
    dollars = amount / rate
    return dollars

def dollars_to_rubles(amount, rate):
    rubles = amount * rate
    return rubles

# Ввод курса валют
rate = float(input("Введите текущий курс доллара к рублю: "))

# Ввод суммы и выбор операции
amount = float(input("Введите сумму: "))
operation = input("Выберите операцию (1 - рубли в доллары, 2 - доллары в рубли): ")

# Выполнение операции
if operation == '1':
    result = rubles_to_dollars(amount, rate)
    print(f"{amount} рублей равно {result} долларов")
elif operation == '2':
    result = dollars_to_rubles(amount, rate)
    print(f"{amount} долларов равно {result} рублей")
else:
    print("Некорректная операция. Пожалуйста, выберите 1 или 2.")