a = input()
print(' 1 - калькулятор')
print(' 2 - подушка')
print(' 3 - набор химика')
print(' 4 - переводчик')
print(' 5 - кофе')
y1 = input()
y2 = input()
if a == '1': 
    a1 = input()
    if a1 == '1':  #PC
        a2 = input()
        if a2 == '1':  #GAME
            a3 = input()
            if a3 == '1':  #VR
                x222 = 0
                x111 = 0
                for i in range(5):
                    i1 = i % 2
                    if i == 0 or i1 == 0:
                        print('front / back')
                        x = input()
                        if x == '1':
                            x222 += 1
                    else:
                        print('right / left')
                        x = input()
                        if x == '2':
                            x111 += 1
                if x222 == 3:
                    if x111 == 2:
                        if y1 != '2' and y2 != '2':
                            print('end')  #END
                        else:
                            print('end')  #END
                if x222 == 0 and x111 == 0 or x111 == 1:
                    print ('вам доступен супер учебник по геометрии')
                    geom = 1
                if x222 == 0 and x111 == 2:
                    print('вам доступен супер учебник по русскому')
                    russ = 1
                a4 = input()
                if a4 == '1':
                    print('end')  #END
                elif a4 == '2':
                    o0 = 1
            elif a3 == '2':  #PCGAME
                a4 = input()
                if a4 == '1' or a4 == '2':  #CSFORT
                    a5 = input()
                    if a5 == '1':
                        print('end')  #END
                    elif a5 == '2':
                        o0 = 1
                elif a4 == '3':
                    a5 = input()
                    if a5 == '1':
                        print('end')  #END
                    elif a5 == '2':
                        o0 == 1
        elif a2 == '2':  #FILM
            a3 = input()
            if a3 == '1':  #FILM
                a4 = input()
                if a4 == '1':
                    print('доступен код')
                    kod = 1
                elif a4 == '2':
                    print('вы потеряли ...')
                    y2 = 0
                elif a4 == '3':
                    print('сон')  #END
                if a4 == '1' or a4 == '2':
                    a5 = input()
                    if a5 == '1':
                        print(end)  #END
                    else:
                        o0 == 1
            elif a3 == '2':  #series
                ...
    elif a2 == '2':  #SCH
        print('s')
