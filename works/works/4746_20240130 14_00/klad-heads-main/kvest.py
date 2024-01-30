import os, time as t, random
i, fl, tp = 0, 0, [str, int, list]
clear = lambda: os.system('cls')
def loter_bil():
    r, ind = int(random.choices([0, 1], weights = [99, 1])[0], -1
    if r == 1:
        ind = random.randint(0, 19)
    for i in range(20):
        print("Билет " + str(i + 1) + "... ", end = "")
        if i != ind:
            print("Ничего.")
        else:
            print("Найдено!")
def store():
    global coins
    sale_flag, sale_string, s, es, choice = 0, "", 0, 0, ""
    while choice != "Хватит":
        clear()
        print("Денег: " + str(coins), end="\n\n")
        for i in range(len(products)):
            if sale_flag == 0 and available[i] > 0:
                s = float(random.choices([0, 0.1, 0.2, 0.3, 0.4, 0.5], weights = [90, 3, 3, 2, 1, 1])[0])
                if s == 0.0:
                    sale_string = ""
                else:
                    sale_string = " (скидка " + str(int(s * 100.0)) + "%)"
                    sale_flag = 1
            if i == 0:
                print("Товар" + " " * (len(max(products, key=len)) - len("Товар") + 20)  + "Стоимость" + " " * 15 + "Осталось", end="\n\n")
            print(products[i] + " " * (len(max(products, key=len)) - len(products[i]) + 20) + str(int(cost[i] * (1.0 - s))) + sale_string + " " * \
            (len(str(max(cost))) - len(str(int(cost[i] * (1.0 - s)))) + 20 - len(sale_string)) + str(available[i]) + " " * (len(str(max(available))) - \
            len(str(available[i])) + 5) + "(очень мало в наличии!)" * (available[i] <= 10 and available[i] > 0) + "(нет в наличии!)" * (available[i] == 0))
            sale_string = ""
            if s != 0:
                es = s
            s = 0
        print()
        print("Вводите в формате - количество позиций товара - пробел - наименование товара.")
        choice = input()
        if choice == "Хватит":
            break
        quant, good = int(choice.split()[0]), choice.split()[1]
        for i in range(len(products)):
            if products[i].lower() == good.lower():
                if quant > available[i]:
                    if coins >=  available[i] * (int(cost[i] * (1.0 - es))):
                        coins -= available[i] * (int(cost[i] * (1.0 - es)))
                        print("Извините, у нас только " + str(available[i]) + " позиций данного товара, их вам и продаем.")
                        if products[i] == "Лотерейный билет, по 20 шт.":
                            loter_bil()
                        t.sleep(1.5)
                        available[i] = 0
                    else:
                        print("Недостаточно денег.")
                        t.sleep(1.5)
                else:
                    if coins >=  quant * (int(cost[i] * (1.0 - es))):
                        coins -=  quant * (int(cost[i] * (1.0 - es)))
                        available[i] -= quant
                        if products[i] == "Лотерейный билет, по 20 шт.":
                            loter_bil()
                    else:
                        print("Недостаточно денег.")
                        t.sleep(1.5)
                es = 0
    clear()
products = ["Металлоискатель", "Фонарик", "Лопата", "Лотерейный билет, по 20 шт."]
available = [4, 11, 113, 55]
cost, coins = [4000, 1000, 500, 400], 20000

replies = ["Итак, наш герой летним вечером прогуливается по побережью. Он гуляет здесь почти каждый день (и зимой тоже), но только сейчас он обратил внимание на одиноко стоящую \
сосну и особенно на большое дупло в ней. Подойдя к дереву ближе, он заметил чуть выглядывающее из отверстия горлышко бутылки. Оно наглухо залито сургучом, а цвет \
стекла бутылки такой темный, что можно было только потрясти, чтобы хоть примерно определить ее содержимое (что наш герой и сделал). Конечно, если она была бы пуста, \
наш герой свернул бы на лесную тропку и пошёл бы дальше неспешно прогуливаться. Но нет, в бутыли что-то было, то ли бумажка, то ли нечто похожее на бумажку. Так \
бутылка еще оказалась сделанной из небьющегося стекла. Конечно, желание гулять у нашего героя пропало, схватив бутылку \
(и чуть не выронив ее в дельту моря), он побежал к своему маленькому домику.", "На троечку или на двоечку?", "На пятерочку или четверочку?", "Терпимо",
            "Ужас!", "Неплохо!", "Прекрасно!"]

links1 = [0, 1, 2, "f", "f", "f", "f"]
qu_fu = [[store, "hi"], ["На двоечку", "На троечку"], ["На пятерочку", "На четверочку"]] #qu_fu - сокращенно от questions and functions
links2 = [[1, 2], [4, 3], [6, 5]]
while fl != 1:
    print(replies[i])
    if input() == "":
        if links1[i] == "f":
            fl == 1
            break
        for j in range(0, len(qu_fu[links1[i]])):
            if type(qu_fu[links1[i]][j]) in tp:
                print(str(j + 1) + ".", qu_fu[links1[i]][j])
            else:
                qu_fu[links1[i]][j]()
        i = links2[i][int(input()) - 1]
