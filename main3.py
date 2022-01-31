
# 1 Работа с переменными..............
a = int(input('Введите число: '))
b = str(input('Введите строку: '))

print(f'Ваша число = {a} и ваша сторка = {b}')

# 2 Работаем со временем...........
time_in_second = int(input('Введите в секунды: '))
job = time_in_second // 3600
remainder = time_in_second % 3600
minute = remainder // 60
second = minute % 60

print(f'{job} : {minute} : {second}')

# 3 Узнаем число n.......
n = int(input("Введите число: "))
z = n + int(str(n) + str (n)) + int(str( n ) + str(n) + str(n))

print(f'Сумма чисел: {z}')



# 4 Найти значение в сумме.....
i = input("Введите число: ")

my_array = []
my_array = list(i)
max = 0
counter = 0
while counter < len(my_array):
    if max < int(my_array[counter]):
        max = int(my_array[counter])
    else:
        continue
    counter += 1
print(max)

# 5 выручки и издержки
revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    profit = revenue - costs
    print(f'Фирма в прибыле! Прибыль состоваляет {profit}')
    print(f'Рентабильнроость выручки = {profit / revenue * 100}%')
    number_of_employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы с расчетом на одного сотрудника = {profit / number_of_employees}')
elif revenue < costs:
    print(f'Фирма в убытке!')
else: revenue = costs
print(f'Фирма в нуле!')

# 6 Спорцмен и пробжки
km = int(input('Сколько спортсмен пробежал в первый день: '))
purpose = int(input('Цель в километрах: '))
day = 1
while km <= purpose:
    km = km + (km * 0.1)
    day = day + 1
print(f'Спротсмену нужно бегать {day} дней, чтобы достичь цели в {purpose} км')