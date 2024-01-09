import random

range_set = 4       # Длина загадываемого числа, по умолчанию - 4.
list_of_numbers = []       # Переменные для списков и подсчета коров и быков.
cows = 0
bulls = 0
temp_number = []
score = 0 # Количество очков в конце игры, которое записывается в текстовый файл.


class b_and_c:
    def NumberGenerator():
        global list_of_numbers
        def guessinglist_nr():  # Функция, которая добавляет случайные числа в количестве равном range_set.
            while len(list_of_numbers) < range_set: # Добавляет неповторяющиеся числа.
                digit = random.randint(1, 9)
                if digit not in list_of_numbers:
                    list_of_numbers.append(digit)
        def guessinglist_r():
            while len(list_of_numbers) != range_set:  # Добавляются случайные числа
                list_of_numbers.append(random.randint(1, 9))
        if input('могут ли числа повторяться? да/нет ') == 'да'.lower():
            guessinglist_r()
        else:
            guessinglist_nr()
        print('вывод списка для облегчения работы - ',list_of_numbers)


    def number_check(): # Функция вывода результата проверок и записи результата в файл.
        global cows
        global bulls
        global score
        print('ты угадал {cows} коров и {bulls} быков. всего очков {score}'.format(cows = cows, bulls = bulls, score = score))
        with open('resultat.txt', 'w') as result_file:
            result_file.write('всего очков {score}'.format(score = score))


    if input('хотите установить длину загадываемого числа? да/нет ') == 'да'.lower():
        global range_set
        range_set = int(input('введите цифру от 2 до 9 '))
    NumberGenerator()


    while True:
        global cows
        global bulls
        global list_of_numbers
        global score
        temp_number = [int(x) for x in input('ввод цифр через пробел - ').split()]
        for k in range(range_set): # Циклы для поиска соответсвий и подсчета.
            if temp_number[k] == list_of_numbers[k]:
                bulls += 1
        for i in range(range_set):
            if temp_number[i] in list_of_numbers and temp_number[i] != list_of_numbers[i]:
                cows += 1
        score += bulls
        number_check()
        if bulls == range_set: # Если число быков совпадает с длиной списка, то мы выиграли.
            if input('отгадал. заново? да/нет ') == 'да'.lower():
                list_of_numbers = []
                NumberGenerator()
                cows = 0
                bulls = 0
            else:
                break
        cows = 0
        bulls = 0
