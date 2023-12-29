import random


def number_check():
    print('ты угадал {cows} коров и {bulls} быков'.format(cows = cows, bulls = bulls))


range_set = 4 # Длина загадываемого числа. Сейчас корректно работает только со значением 4.
set_of_numbers = set() # Переменные для множества, списков и подсчета коров и быков.
list_of_numbers = []
temp_number = []
cows = 0
bulls = 0


def guessinglist(): # Функция, которая добавляет случайные числа в количестве равном
    global list_of_numbers          # range_set в множество и переводит его в список.
    while len(set_of_numbers) != range_set:
        set_of_numbers.add(random.randint(1, 9))
    list_of_numbers = list(set_of_numbers)


if input('хотите установить длину загадываемого числа? да/нет ') == 'да'.lower():
    print('введите цифру от 4 до 9')
    range_set = int(input())
guessinglist()

print('вывод списка для облегчения работы - ', list_of_numbers)

while True:
    temp_number = input('ввод цифр через пробел - ').split()
    for h in range(len(temp_number)): # Циклы для поиска соответсвий и подсчета.
        temp_number[h] = int(temp_number[h])
    for k in range(range_set):
        if temp_number[k] == list_of_numbers[k]:
            bulls += 1
    for i in range(range_set):
        if temp_number[i] in list_of_numbers and temp_number[i] != list_of_numbers[i]:
            cows += 1
    number_check()
    if bulls == range_set: # Если число быков совпадает с длиной списка, то мы выиграли.
        if input('отгадал. заново? да/нет ') == 'да'.lower():
            set_of_numbers = set()
            list_of_numbers = []
            guessinglist()
            print(list_of_numbers)
            cows = 0
            bulls = 0
        else:
            break
    cows = 0
    bulls = 0