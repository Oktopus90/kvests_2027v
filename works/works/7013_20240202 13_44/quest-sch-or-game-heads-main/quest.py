print(' Приветствую вас в моем квесте,')
print(' Ваша задача не только сдать зачеты,')
print(' Но и развлечся')
print(' Нажмите 1 для старта')
o0 = 0
eng = 0
russ = 0
geom = 0
chem = 0
phis = 0
kod = 0
qweewq = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
a = input()
if a == '1':
    print(' Выберите 2 предмета на игру')
    print(' 1 - калькулятор')
    print(' 2 - суперподушка')
    print(' 3 - набор химика')
    print(' 4 - переводчик')
    print(' 5 - кофе')
    y1 = input()
    y2 = input()
    if a == '1':
        print(' ПК или учеба')
        print(' 1 - ПК')
        print(' 2 - Учеба')
        a1 = input()
        if a1 == '1':
            print(' Выберите что вы будете делать?')
            print(' 1 - играть')
            print(' 2 - смотреть фильм')
            a2 = input()
            if a2 == '1':
                print(' 1 - VR')
                print(' 2 - PC GAME')
                a3 = input()
                if a3 == '1':
                    x222 = 0
                    x111 = 0
                    print(' Вам нужно писать 1 или 2')
                    print(' В зависимости от того что вы хотите выбрать')
                    for i in range(5):
                        i1 = i % 2
                        if i == 0 or i1 == 0:
                            print('*** front / back ***')
                            x = input()
                            if x == '1':
                                x222 += 1
                        else:
                            print('*** right / left ***')
                            x = input()
                            if x == '2':
                                x111 += 1
                    if x222 == 3:
                        if x111 == 2:
                            if y1 != '2' and y2 != '2':
                                print('!!!!! Вы вышли из сооружения и заснули, но')
                                print('!!!!! После вы проснулись в лучшем мире')
                                print('END END END END END END')
                                input()
                            else:
                                print('!!!!! Вы вышли из сооружения и заснули, но')
                                print('!!!!! Вы упали на суперподушку которая дала вам знаний,')
                                print('!!!!! С помощью нее вы все сдали на 5')
                                print('END END END END END END')
                                input()
                            qweewq = 1
                    if x222 == 0 and x111 == 0 or x111 == 1:
                        print('Вам доступен супер учебник по геометрии')
                        geom = 1
                    if x222 == 0 and x111 == 2:
                        print('Вам доступен супер учебник по русскому')
                        russ = 1
                    if qweewq == 0:
                        print('Что будете делать дальше')
                        print(' 1 - пойду спать')
                        print(' 2 - пойду учить уроки')
                        a4 = input()
                        if a4 == '1':
                            print('!!!!! Вы пошли поспать, но когда проснулись')
                            print('!!!!! Подумали что вы в VR и долго пытались')
                            print('!!!!! Понять на какую кнопку встать с кровати')
                            print('!!!!! В итоге вы опздали на экзамены')
                            print('END END END END END END')
                            input()
                        if a4 == '2':
                            o0 = 1
                elif a3 == '2':
                    print(' Выберите игру')
                    print(' 1 - CS2')
                    print(' 2 - Fortnite')
                    print(' 3 - GTA V')
                    a4 = input()
                    if a4 == '1' or a4 == '2':
                        print(' Вы поиграли 2 часа')
                        if a4 == '1' and y1 != 4 and y2 != 4:
                            print(' Вы получили навык английского языка')
                            eng = 1
                        print(' 1 - пойти спать')
                        print(' 2 - пойти играть дальше')
                        print(' 3 - пойти учить уроки')
                        a5 = input()
                        if a5 == 1:
                            if y1 == 1 or y2 == 1:
                                print(' Вы сдали хорошо')
                                print(' Только алгебру, из-за калькулятора')
                                print(' Остальное вы сдали на 3')
                                print('END END END END END END')
                                input()
                            else:
                                print(' Вы сдали все на 3')
                                print('END END END END END END')
                                input()
                    elif a4 == '3':
                        print('!!!!! Вы стали жестоким и не пошли')
                        print('!!!!! Сдавать зачеты')
                        print('END END END END END END')
                        input()
            elif a2 == '2':
                print(' ФИЛЬМ / СЕРИАЛ ')
                a3 = input()
                if a3 == '1':
                    print(' Выберите фильм:')
                    print(' 1 - Социальная сеть')
                    print(' 2 - БОБРЫ-ЗОМБИ')
                    print(' 3 - Властелин колец')
                    a4 = input()
                    if a4 == '1':
                        print(' Вам доступен новый код')
                        kod = 1
                    elif a4 == '2':
                        print(' Тебе выдан штраф')
                        print(' За этот ответ')
                        y1 = 0
                        y2 = 0
                        eng = 0
                        russ = 0
                        geom = 0
                    elif a4 == '3':
                        print(' Вы заснули и проспали')
                        print('END END END END END END')
                        input()
                    if a4 == '1' or a4 == '2':
                        print(' Пойти спать / делать уроки')
                        a5 = input()
                        if a5 == '1':
                            if kod == 1:
                                if y1 == 1 or y2 == 1:
                                    print(' Вы сдали алгебру и информатику')
                                    print(' На 5, остальное на 3')
                                    print('END END END END END END')
                                    input()
                                else:
                                    print(' Вы сдали информатику на 5,')
                                    print(' Остальное на 3')
                                    print('END END END END END END')
                                    input()
                            elif y1 == 1 or y2 == 1:
                                print(' Вы сдали математику на 5,')
                                print(' Остальное на 3')
                                print('END END END END END END')
                            else:
                                print(' Вы сдали все предметы на 3')
                                print('END END END END END END')
                                input()
                        else:
                            o0 == 1
                elif a3 == '2':
                    print(' Выберите сериал')
                    print(' 1 - Breaking Bad')
                    print(' 2 - Теория большого взрыва')
                    print(' 3 - Слово пацана')
                    a4 = input()
                    if a4 == '1':
                        if y1 == 3 or y2 == 3:
                            print(' Вы улучшили свои навыки в химии')
                            chem = 2
                        else:
                            print(' Вы улучшили свои навыки в химии')
                            chem = 1
                    elif a4 == '2':
                        print(' Вы улучшили свои навыки в физике')
                        phis = 1
                    elif a4 == '3':
                        print(' Ну это просто...')
                        print('END END END END END END')
                    if a4 != '3':
                        print(' Пойти спать / пойти учиться')
                        a5 = input()
                        if a5 == '1':
                            if y1 == 1 or y2 == 1:
                                print(' Вы сдали алгебру и химию')
                                print(' На 5, остальное на 3')
                                print('END END END END END END')
                                input()
                            else:
                                print(' Вы сдали химию на 5,')
                                print(' Остальное на 3')
                                print('END END END END END END')
                                input()
                        else:
                            if y1 == 1 or y2 == 1:
                                print(' Вы сдали алгебру и физику')
                                print(' На 5, остальное на 3')
                                print('END END END END END END')
                                input()
                            else:
                                print(' Вы сдали физику на 5,')
                                print(' Остальное на 3')
                                print('END END END END END END')
                                input()
        if a1 == '2' or o0 == 1:
            a2 = input()
            print(' 1 - Математика')
            print(' 2 - Языки')
            print(' 3 - Остальное')
            if a2 == '1':
                a3 = input()
                print(' 1 - Геометрия')
                print(' 2 - Алгебра')
                print(' 3 - Информатика')
                if a3 == '1':
                    if geom == 1:
                        print(' У вас есть супер учебник по геометрии,')
                        print(' Вы полностью выучили геометрию')
                        b1 = 1
                    else:
                        print(' Катит это ...')
                        print('1 - прилегающая к прямому углу')
                        print('2 - сторона лежащая против прямого угла')
                        print('3 - катет - сторона прлегающая к прямому углу')
                        a4 = input()
                        if a4 == '1':
                            print(' Вы выучили геометрию')
                            b1 = 1
                        elif a4 == '2':
                            print('гений')
                        elif a4 == '3':
                            print(' Вы выучили геометрию')
                            print(' Вы выучили Русский')
                            b1 = 1
                            b2 = 1
