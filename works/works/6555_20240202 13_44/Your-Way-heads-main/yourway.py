import random
import time
import math
from datetime import datetime
if __import__("platform").system() == "Windows":
    kernel32 = __import__("ctypes").windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    del kernel32


def job100000(money):
    for i in range(9):
        tusk_1 = random.randint(100, 999)
        tusk_2 = random.randint(100, 999)
        print("Решите задачу.")
        print(tusk_1, "*", tusk_2, "= ?")
        answer = input()
        if answer == "/goon":
            break
        while answer != str(tusk_1 * tusk_2):
            print("Введите число - ответ на задачу.")
            answer = input()
            if answer == "/goon":
                break
        money += 100000
        print("Вы заработали 100 тыс. рублей!")
        print("\n")


def it_job(money):
    while money < 10000000:
        a = random.randint(-1000, 1000)
        while a == 0:
            a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        c = random.randint(-1000, 1000)
        asi = ""
        bs = ""
        cs = ""
        if b > -1:
            bs = "+"
        if c > -1:
            cs = "+"
        print(asi + str(a) + "x\u00b2" + bs + str(b) + "x" + cs + str(c))
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b - discriminant ** 0.5) / (2 * a)
            x2 = (-b + discriminant ** 0.5) / (2 * a)
            x1 = round(x1, 3)
            x2 = round(x2, 3)
            x1 = str(x1)
            x2 = str(x2)
        else:
            x1 = "нет корней"
            x2 = "нет корней"
        xset = {x1, x2}
        print("Введите два числа - корни уравнения, " +
              "округлив их до тысячных (если они есть) и" +
              " \"нет корней\" строчными буквами, если их нет.")
        x1i = input()
        x2i = input()
        if x1i == "/goon" or x2i == "/goon":
            break
        while x1i not in xset and x2i not in xset:
            print("Введите два числа - корни уравнения (если они есть) и" +
                  " \"нет корней\" строчными буквами, если их нет.")
            if x1i == "/goon" or x2i == "/goon":
                break
            x1i = input()
            x2i = input()
        print("Вы заработали 350 тыс. рублей!")
        print("\n")
        money += 350000


def job_shop(money):
    money_count = 0
    for i in range(7):
        cost = random.randint(1, 1000000)
        money_count += cost
        print("Покупка: +", cost, sep="")
        print("Выведите число - количество денег в кассе.")
        shop_money = input()
        if shop_money == "/goon":
            break
        while shop_money != str(money_count):
            print("Выведите число - количество денег в кассе.")
            shop_money = input()
            if shop_money == "/goon":
                break
        money += 42000
        print("Вы заработали 42 тыс. рублей!")
        print("\n")
    return money


def Germany(money):
    while money < 10000000:
        a = random.randint(-1000, 1000)
        while a == 0:
            a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        c = random.randint(-1000, 1000)
        asi = ""
        bs = ""
        cs = ""
        if b > -1:
            bs = "+"
        if c > -1:
            cs = "+"
        print(asi + str(a) + "x\u00b2" + bs + str(b) + "x" + cs + str(c))
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b - discriminant ** 0.5) / (2 * a)
            x2 = (-b + discriminant ** 0.5) / (2 * a)
            x1 = round(x1, 3)
            x2 = round(x2, 3)
            x1 = str(x1)
            x2 = str(x2)
        else:
            x1 = "keine Gleichungswurzeln"
            x2 = "keine Gleichungswurzeln"
        xset = {x1, x2}
        print("Geben Sie zwei Zahlen ein – die Wurzeln der Gleichung, " +
              " und runden Sie sie auf Tausendstel (falls vorhanden)" +
              " \"keine Gleichungswurzeln\" Kleinbuchstaben," +
              " wenn keine vorhanden sind.")
        x1i = input()
        x2i = input()
        if x1i == "/goon" or x2i == "/goon":
            break
        while x1i not in xset and x2i not in xset:
            print("Geben Sie zwei Zahlen ein – die Wurzeln der Gleichung," +
                  " und runden Sie sie auf Tausendstel (falls vorhanden)" +
                  " \"keine Gleichungswurzeln\" Kleinbuchstaben," +
                  " wenn keine vorhanden sind.")
            if x1i == "/goon" or x2i == "/goon":
                break
            x1i = input()
            x2i = input()
        print("Sie haben 4123 Euro verdient!")
        print("\n")
        money += 350000


def France(money):
    while money < 10000000:
        a = random.randint(-1000, 1000)
        while a == 0:
            a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        c = random.randint(-1000, 1000)
        asi = ""
        bs = ""
        cs = ""
        if b > -1:
            bs = "+"
        if c > -1:
            cs = "+"
        print(asi + str(a) + "x\u00b2" + bs + str(b) + "x" + cs + str(c))
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b - discriminant ** 0.5) / (2 * a)
            x2 = (-b + discriminant ** 0.5) / (2 * a)
            x1 = round(x1, 3)
            x2 = round(x2, 3)
            x1 = str(x1)
            x2 = str(x2)
        else:
            x1 = "pas de racines"
            x2 = "pas de racines"
        xset = {x1, x2}
        print("Entrez deux nombres - les racines de" +
              " l'équation arrondies au millième " + 
              "(le cas échéant) et \"pas de racines\" en" +
              " lettres minuscules s'il n'y en a pas.")
        x1i = input()
        x2i = input()
        if x1i == "/goon" or x2i == "/goon":
            break
        while x1i not in xset and x2i not in xset:
            print("Entrez deux nombres - les racines de" +
                  " l'équation arrondies au millième " + 
                  "(le cas échéant) et \"pas de racines\" en" +
                  " lettres minuscules s'il n'y en a pas.")
            if x1i == "/goon" or x2i == "/goon":
                break
            x1i = input()
            x2i = input()
        print("Vous avez gagné 4123 euros!")
        print("\n")
        money += 350000


def miner(name, inventory):
    win = True
    flag_count = 30
    inventory.append(flag_count)
    print("Вам выдано 30 флажков.")

    field = [0] * 20
    for i in range(20):
        field[i] = [0] * 16

    output_field = ["#"] * 18
    for i in range(18):
        output_field[i] = ["#"] * 14

    for i in range(30):
        nmines = random.randint(1, 18)
        mmines = random.randint(1, 14)
        while field[nmines][mmines] == "*":
            nmines = random.randint(1, 18)
            mmines = random.randint(1, 14)
        field[nmines][mmines] = "*"
        if name == "dev0826":
            print(mmines - 1, nmines - 1, sep=" ")
            output_field[nmines - 1][mmines - 1] = chr(128681)
    
    for i in range(1, 19):
        for j in range(1, 15):
            mine_count = 0
            if field[i][j] != "*":
                if field[i + 1][j] == "*":
                    mine_count += 1
                if field[i + 1][j + 1] == "*":
                    mine_count += 1
                if field[i - 1][j] == "*":
                    mine_count += 1
                if field[i - 1][j - 1] == "*":
                    mine_count += 1
                if field[i - 1][j + 1] == "*":
                    mine_count += 1
                if field[i + 1][j - 1] == "*":
                    mine_count += 1
                if field[i][j + 1] == "*":
                    mine_count += 1
                if field[i][j - 1] == "*":
                    mine_count += 1
                field[i][j] = mine_count
                if mine_count == 0:
                    fx = i - 1
                    fy = j - 1
        
    output_field[fx][fy] = 0

    for i in range(18):
        for j in range(14):
            if output_field[i][j] == 1:
                print('\033[94m' + "1", end="\t")
            elif output_field[i][j] == 2:
                print('\033[92m' + "2", end="\t")
            elif output_field[i][j] == 3:
                print('\033[91m' + "3", end="\t")
            elif output_field[i][j] == 4:
                print('\033[95m' + "4", end="\t")
            elif output_field[i][j] == 5:
                print("\033[0;33m" + "5", end="\t")
            elif output_field[i][j] == 6:
                print("\033[0;36m" + "6", end="\t")
            elif output_field[i][j] == 7:
                print("\033[0;90m" + "7", end="\t")
            elif output_field[i][j] == 8:
                print("\033[0;41m" + "8", end="\t")
            elif output_field[i][j] == 0:
                print("\033[0m" + "0", end="\t")
            else:
                print("\033[0;90m" + str(output_field[i][j]), end="\t")
        print()

    end_count = 0
    for i in range(19):
        for j in range(15):
            if field[i][j] == "*":
                if output_field[i - 1][j - 1] == chr(128681):
                    end_count += 1
    
    coordx_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "11", "12", "13", "14", "15", "16", "17"]
    coordy_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "11", "12", "13"]
    while end_count < 30:
        print("\033[0mВведите координаты.")
        y = input()
        x = input()
        if x == "/goon" or y == "/goon":
            return
        while x not in coordx_list or y not in coordy_list:
            print("\033[0mВведите координаты.")
            y = input()
            x = input()
            if x == "/goon" or y == "/goon":
                return
        x = int(x)
        y = int(y)
        print("\033[0mВыберите действие.")
        print("1. Копать")
        print("2. Поставить флажок")
        print("3. Убрать флажок")
        miner_choise = input()
        while (miner_choise != "1" and miner_choise != "2" and 
               miner_choise != "3"):
            print("\033[0mВведите 1, 2 или 3.")
            miner_choise = input()
        if miner_choise == "3":
            if output_field[x][y] == chr(128681):
                flag_count += 1
            output_field[x][y] = "#"
            print("Флажков осталось:", flag_count)
        if miner_choise == "2":
            if output_field[x][y] != chr(128681):
                flag_count -= 1
            if flag_count > 0:
                output_field[x][y] = chr(128681)
            print("Флажков осталось:", flag_count)
            
        if miner_choise == "1":
            if field[x + 1][y + 1] == "*":
                print("\033[0mВы наступили на мину.")
                win = False
                break
            elif field[x + 1][y + 1] > 0:
                output_field[x][y] = field[x + 1][y + 1]
            elif field[x + 1][y + 1] == 0:
                zeroes_x = [x]
                zeroes_y = [y]
                while len(zeroes_x) > 0:
                    output_field[x][y] = field[x + 1][y + 1]
                    a = zeroes_x[0]
                    b = zeroes_y[0]
                    if a < 17:
                        openCell(a + 1, b, a + 2, b + 1, field, output_field, zeroes_x, zeroes_y)
                    if a < 17 and b < 13:
                        openCell(a + 1, b + 1, a + 2, b + 2, field, output_field, zeroes_x, zeroes_y)
                    if a < 17 and b > 0:
                        openCell(a + 1, b - 1, a + 2, b, field, output_field, zeroes_x, zeroes_y)
                    if a > 0:
                        openCell(a - 1, b, a, b + 1, field, output_field, zeroes_x, zeroes_y)
                    if a > 0 and b < 13:
                        openCell(a - 1, b + 1, a, b + 2, field, output_field, zeroes_x, zeroes_y)
                    if a > 0 and b > 0:
                        openCell(a - 1, b - 1, a, b, field, output_field, zeroes_x, zeroes_y)
                    if b < 13:
                        openCell(a, b + 1, a + 1, b + 2, field, output_field, zeroes_x, zeroes_y)
                    if b > 0:
                        openCell(a, b - 1, a + 1, b, field, output_field, zeroes_x, zeroes_y)
                    zeroes_x.pop(0)
                    zeroes_y.pop(0)                              

        for i in range(18):
            for j in range(14):
                if output_field[i][j] == 1:
                    print('\033[94m' + "1", end="\t")
                elif output_field[i][j] == 2:
                    print('\033[92m' + "2", end="\t")
                elif output_field[i][j] == 3:
                    print('\033[91m' + "3", end="\t")
                elif output_field[i][j] == 4:
                    print('\033[95m' + "4", end="\t")
                elif output_field[i][j] == 5:
                    print("\033[0;33m" + "5", end="\t")
                elif output_field[i][j] == 6:
                    print("\033[0;36m" + "6", end="\t")
                elif output_field[i][j] == 7:
                    print("\033[0;90m" + "7", end="\t")
                elif output_field[i][j] == 8:
                    print("\033[0;41m" + "8", end="\t")
                elif output_field[i][j] == 0:
                    print("\033[0m" + "0", end="\t")
                else:
                    print("\033[0;90m" + str(output_field[i][j]), end="\t")
            print()

        end_count = 0
        for i in range(19):
            for j in range(15):
                if field[i][j] == "*":
                    if output_field[i - 1][j - 1] == chr(128681):
                        end_count += 1
    if win:
        print("Вы разминировали поле.")
    return win
        
        
def openCell(outX, outY, x, y, field, output_field, zeroes_x, zeroes_y):
    if field[x][y] == 0 and output_field[outX][outY] in ["#", chr(128681)]:
        zeroes_x.append(outX)
        zeroes_y.append(outY)
    output_field[outX][outY] = field[x][y]


def Azerbaijan(money):
    money_count = 0
    for i in range(63):
        cost = random.randint(1, 1000000)
        money_count += cost
        print("Aliş: +", cost, sep="")
        print("Nömrəni çap edin - kassadaki pul məbləği.")
        shop_money = input()
        if shop_money == "/goon":
            break
        while shop_money != str(money_count):
            print("Nömrəni çap edin - kassadaki pul məbləği.")
            shop_money = input()
            if shop_money == "/goon":
                break
        money += 42000
        print("947 manat qazandiniz!")
        print("\n")
    return money


def sea_battle():
    win = False
    bot_field = ["~"] * 11
    for i in range(11):
        bot_field[i] = ["~"] * 11

    obf = ["*"] * 12
    for i in range(12):
        obf[i] = ["*"] * 12
        for k in range(1, 11):
            obf[i][k] = "~"

    player_field = ["~"] * 11
    for i in range(11):
        player_field[i] = ["~"] * 11

    opf = ["*"] * 12
    for i in range(12):
        opf[i] = ["*"] * 12
        for k in range(1, 11):
            opf[i][k] = "~"

    coord_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    print("Расставить корабли самостоятельно?")
    print("1. Да")
    print("2. Нет")
    place_choice = input()
    while place_choice not in ["1", "2"]:
        print("Введите 1 или 2")
        place_choice = input()

    if place_choice == "1":
        ship_place(4, coord_list, opf)
        ship_place(3, coord_list, opf)
        ship_place(3, coord_list, opf)
        ship_place(2, coord_list, opf)
        ship_place(2, coord_list, opf)
        ship_place(2, coord_list, opf)
        ship_place(1, coord_list, opf)
        ship_place(1, coord_list, opf)
        ship_place(1, coord_list, opf)
        ship_place(1, coord_list, opf)
    else:
        bot_ship_place(4, opf)
        bot_ship_place(3, opf)
        bot_ship_place(3, opf)
        bot_ship_place(2, opf)
        bot_ship_place(2, opf)
        bot_ship_place(2, opf)
        bot_ship_place(1, opf)
        bot_ship_place(1, opf)
        bot_ship_place(1, opf)
        bot_ship_place(1, opf)

    bot_ship_place(4, obf)
    bot_ship_place(3, obf)
    bot_ship_place(3, obf)
    bot_ship_place(2, obf)
    bot_ship_place(2, obf)
    bot_ship_place(2, obf)
    bot_ship_place(1, obf)
    bot_ship_place(1, obf)
    bot_ship_place(1, obf)
    bot_ship_place(1, obf)

    show_fields(obf, opf)

    pl = 0
    bot = 0
    while pl < 20 and bot < 20:
        bot = bot_step(opf, bot)
        pl = player_step(obf, opf, pl, coord_list)
        # pl = bot_step(obf, pl)
        show_fields(obf, opf)

    if pl == 20:
        win = True
        print("Вы выиграли сражение!")
    else:
        print("Вы потерпели поражение.")
    return win


def show_fields(obf, opf):
    print("   1 2 3 4 5 6 7 8 9 10           1 2 3 4 5 6 7 8 9 10")
    for i in range(1, 11):
        print(f'{i:2d}', end=" ")
        for j in range(1, 11):
            print(opf[i][j], end=" ")
        print(f'        {i:2d}', end=" ")
        for j in range(1, 11):
            if obf[i][j] == chr(9634):
                print("~", end=" ")
            else:
                print(obf[i][j], end=" ")          
    
        print()
           

def ship_place(lenght, coord_list, field):

    while True:
        x = 0
        y = 0
        ships = False

        while x not in coord_list or y not in coord_list:
            print("Введите координаты.")
            y = input()
            x = input()

        x = int(x)
        y = int(y)
        print("Как поставить корабль?")
        print("1. Вертикально")
        print("2. Горизонтально")

        ship_choice = input()
        while ship_choice not in ["1", "2"]:
            print("Введите 1 или 2.")
            ship_choice = input()

        if ship_choice == "1":

            if x + lenght > 10:
                print("Корабль не помещается. Введите корректные координаты.")
                continue

            for i in range(x - 1, x + lenght + 1):
                for j in range(y - 1, y + 2):
                    if field[i][j] == chr(9634):
                        ships = True
        else:
            if y + lenght > 10:
                print("Корабль не помещается. Введите корректные координаты.")
                continue

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + lenght + 1):
                    if field[i][j] == chr(9634):
                        ships = True

        if ships:
            print("Нельзя ставить корабли так близко друг к другу.")
            continue
        
        if ship_choice == "1":
            for i in range(x, x + lenght):
                field[i][y] = chr(9634)
        else:
            for i in range(y, y + lenght):
                field[x][i] = chr(9634)
        
        print("   1 2 3 4 5 6 7 8 9 10")
        for i in range(1, 11):
            print(f'{i:2d}', end=" ")
            for j in range(1, 11):
                print(field[i][j], end=" ")
            print()
        break


def bot_ship_place(lenght, field):

    while True:
        ships = False

        y = random.randint(1, 10)
        x = random.randint(1, 10)

        ship_choice = random.randint(1, 2)

        if ship_choice == 1:

            if x + lenght > 10:
                continue

            for i in range(x - 1, x + lenght + 1):
                for j in range(y - 1, y + 2):
                    if field[i][j] == chr(9634):
                        ships = True
        else:
            if y + lenght > 10:
                continue

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + lenght + 1):
                    if field[i][j] == chr(9634):
                        ships = True

        if ships:
            continue
        
        if ship_choice == 1:
            for i in range(x, x + lenght):
                field[i][y] = chr(9634)
        else:
            for i in range(y, y + lenght):
                field[x][i] = chr(9634)
        
        print("   1 2 3 4 5 6 7 8 9 10")
        for i in range(1, 11):
            print(f'{i:2d}', end=" ")
            for j in range(1, 11):
                print(field[i][j], end=" ")
            print()
        break


def bot_step(field, count):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    while field[x][y] in ["X", "*"]:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
    
    return bot_shot(field, count, x, y)


def bot_shot(field, count, x, y):
    if field[x][y] == "~":
        field[x][y] = "*"
        return count
        
    field[x][y] = "X"
    field[x - 1][y - 1] = "*"
    field[x - 1][y + 1] = "*"
    field[x + 1][y - 1] = "*"
    field[x + 1][y + 1] = "*"
    count += 1

    cells_list = []
    if field[x][y + 1] not in ["X", "*"]:
        cells_list.append((x, y + 1))
    if field[x][y - 1] not in ["X", "*"]:
        cells_list.append((x, y - 1))
    if field[x + 1][y] not in ["X", "*"]:
        cells_list.append((x + 1, y))
    if field[x - 1][y] not in ["X", "*"]:
        cells_list.append((x - 1, y))

    if len(cells_list) == 0:
        return bot_step(field, count)
    else:
        a, b = random.choice(cells_list)
        return bot_shot(field, count, a, b)


def player_step(field, bot_field, count, coord_list):
    print("Введите координаты")
    y = input()
    x = input()
    while x not in coord_list or y not in coord_list:
        print("Введите координаты.")
        y = input()
        x = input()
    x = int(x)
    y = int(y)
    
    if field[x][y] == chr(9634):
        field[x][y] = "X"
        count += 1
        if count < 20:
            show_fields(field, bot_field)
            return player_step(field, bot_field, count, coord_list)
    elif field[x][y] == "~":
        field[x][y] = "*"
        
    return count


def tank_test():
    win = False
    for i in range(10):
        probitie = random.randint(100, 1000)
        normalization = random.randint(0, 15)
        armor = random.randint(100, 1000)
        ugol = random.randint(0, 80)
        print("Пробитие:", probitie)
        print("Нормализация:", normalization)
        print("Толщина брони:", armor)
        print("Угол наклона:", ugol)
        prob = "2"
        if probitie > armor * (1 / math.cos((ugol - normalization) / 57)):
            prob = "1"
        print("Есть пробитие?")
        print("1. Да")
        print("2. Нет")
        ans_wer = input()
        while ans_wer not in ["1", "2"]:
            print("Введите 1 или 2.")
            ans_wer = input()
        if ans_wer == prob:
            print("Верно!")
            win = True
        else:
            print("Неверно.")
            win = False
            break
    return win


def avia_mech():
    inventory = []
    cr73 = 0
    cr27 = 0
    ckab = 0
    cen = 0
    cw = 0
    eng = False
    eng2 = False
    wng = False
    wng2 = False
    crp = False
    cab = False
    r731 = False
    r732 = False
    r733 = False
    r734 = False
    r271 = False
    r272 = False
    r273 = False
    r274 = False
    kab1 = False
    kab2 = False
    pod = False
    engine = ["Воздухозаборник", "Компрессор", "Турбина",
              "Камера сгорания", "Форсажная камера", "Система охлаждения",
              "Система управления вектором тяги", "Масляный бак"]

    r73 = ["ИК-головка самонаведения", "Оперение", "Двигатель ракеты",
           "Обшивка ракеты"]

    r27et = ["РЛ ГСН", "Оперение", "Двигатель ракеты", "Обшивка ракеты"]

    kab500 = ["Взрыватель", "Взрывчатое вещество", "ГСН", "Корпус бомбы"]

    wing = ["Закрылок", "Топливный бак", "Стабилизаторы", "Стойка шасси"]
    
    podvesi = ["Ракета Р-73-1", "Ракета Р-73-2", "Ракета Р-73-3",
               "Ракета Р-73-4", "Ракета Р-27ЭТ-1", "Ракета Р-27ЭТ-2",
               "Ракета Р-27ЭТ-3", "Ракета Р-27ЭТ-4", "Бомба КАБ-500-1",
               "Бомба КАБ-500-2"]

    cabine = ["Кресло-катапульта", "Панель управления", "Бронестекло", "РЛС"]

    corpus = ["Обшивка", "Центральная стойка шасси", "Кабина", "Пушка",
              "Воздушный тормоз"]

    su35s = ["Двигатель-1", "Двигатель-2", "Крыло-1", "Крыло-2", "Корпус",
             "Подвесное вооружение"]
    
    words = ["Карбюратор", "Пропеллер", "Радиатор", "Конденсатор",
             "Ковш", "Фанерная доска", "Артём?",
             "Турбореактивный вертолётный двигатель",
             "Электронейтральный гусь Вася"]
    
    sklad = []
    for i in range(37):
        sklad.append(random.choice(words))

    for i in engine:
        sklad.append(i)
    for i in engine:
        sklad.append(i)
    for i in r73:
        sklad.append(i)
    for i in r73:
        sklad.append(i)
    for i in r73:
        sklad.append(i)
    for i in r73:
        sklad.append(i)
    for i in r27et:
        sklad.append(i)
    for i in r27et:
        sklad.append(i)
    for i in r27et:
        sklad.append(i)
    for i in r27et:
        sklad.append(i)
    for i in kab500:
        sklad.append(i)
    for i in kab500:
        sklad.append(i)
    for i in wing:
        sklad.append(i)
    for i in wing:
        sklad.append(i)
    for i in corpus:
        sklad.append(i)
    for i in cabine:
        sklad.append(i)
    x = sklad.index("Кабина")
    sklad.pop(x)
    random.shuffle(sklad)
    su = set()
    su.update(su35s)
    inv = set()
    inv.update(inventory)
    while inv != su:
        for i in sklad:
            print(i, end=" ")
        print()
        print("Что берем?")
        thing = input()
        while thing not in sklad:
            print("На складе этого нет")
            thing = input()
        if thing in words:
            print("Это нам не нужно.")
        else:
            sklad.pop(sklad.index(thing))
            inventory.append(thing)

            if create(engine, eng, inventory):
                delete(engine, inventory)
                print("Двигатель собран.")
                cen += 1
                inventory.append("Двигатель-" + str(cen))
            if create(engine, eng2, inventory):
                delete(engine, inventory)
                print("Двигатель собран.")
                cen += 1
                inventory.append("Двигатель-" + str(cen))
            if create(wing, wng, inventory):
                delete(wing, inventory)
                cw += 1
                print("Крыло собрано.")
                inventory.append("Крыло-" + str(cw))
            if create(wing, wng2, inventory):
                delete(wing, inventory)
                cw += 1
                print("Крыло собрано.")
                inventory.append("Крыло-" + str(cw))
            if create(corpus, crp, inventory):
                delete(corpus, inventory)
                print("Корпус собран.")
                inventory.append("Корпус")
            if create(cabine, cab, inventory):
                delete(cabine, inventory)
                print("Кабина собрана.")
                inventory.append("Кабина")
            if create(r73, r731, inventory):
                delete(r73, inventory)
                cr73 += 1
                print("Р-73 собрана.")
                inventory.append("Ракета Р-73-" + str(cr73))
            if create(r73, r732, inventory):
                delete(r73, inventory)
                cr73 += 1
                print("Р-73 собрана.")
                inventory.append("Ракета Р-73-" + str(cr73)) 
            if create(r73, r733, inventory):
                delete(r73, inventory)
                cr73 += 1
                print("Р-73 собрана.")
                inventory.append("Ракета Р-73-" + str(cr73))
            if create(r73, r734, inventory):
                delete(r73, inventory)
                cr73 += 1
                print("Р-73 собрана.")
                inventory.append("Ракета Р-73-" + str(cr73))
            if create(r27et, r271, inventory):
                delete(r27et, inventory)
                cr27 += 1
                print("Р-27ЭТ собрана.")
                inventory.append("Ракета Р-27ЭТ-" + str(cr27))
            if create(r27et, r272, inventory):
                delete(r27et, inventory)
                cr27 += 1
                print("Р-27ЭТ собрана.")
                inventory.append("Ракета Р-27ЭТ-" + str(cr27))
            if create(r27et, r273, inventory):
                delete(r27et, inventory)
                cr27 += 1
                print("Р-27ЭТ собрана.")
                inventory.append("Ракета Р-27ЭТ-" + str(cr27))
            if create(r27et, r274, inventory):
                delete(r27et, inventory)
                cr27 += 1
                print("Р-27ЭТ собрана.")
                inventory.append("Ракета Р-27ЭТ-" + str(cr27))
            if create(kab500, kab1, inventory):
                delete(kab500, inventory)
                ckab += 1
                print("КАБ-500 собрана.")
                inventory.append("Бомба КАБ-500-" + str(ckab))
            if create(kab500, kab2, inventory):
                delete(kab500, inventory)
                ckab += 1
                print("КАБ-500 собрана.")
                inventory.append("Бомба КАБ-500-" + str(ckab))   
            if create(podvesi, pod, inventory):
                delete(podvesi, inventory)
                print("Подвесное вооружение собрано.")
                inventory.append("Подвесное вооружение")
    
    print("Самолёт готов. Лететь можно.")


def create(elem, check, inv):
    for i in elem:
        if i in inv:
            check = True
        else:
            check = False
            break
    return check
    

def delete(elem, inv):
    for i in elem:
        inv.pop(inv.index(i))


army = False
burn = False
not_enough = False
win = True
money = 3000
inventory = [money]
print("Как вас зовут?")
name = input()
if name == "/money":
    money += 1000000
dream_var = ["автомобиль", "частный вертолет", "вилла в Испании", "компьютер"]
dream = random.choice(dream_var)
print("\n")
print("Ваша мечта - ", dream, 
      ", за неё придется заплатить 10 млн рублей.\n", sep="")

print("Из воспоминаний ", name, ":", sep="")
print("\n08.08.2007, Утро")
print("Это был обычный летний день. Я, как обычно, встал в 7 часов утра, " +
      "позавтракал и вышел на улицу. Предо мной встал выбор: " +
      "как и все пойти на работу или, махнув на все рукой, " +
      "вернуться домой.")
print("1. Пойти на работу")
print("2. Вернуться домой")

first_choise = input()
while first_choise != "1" and first_choise != "2":
    print("Введите 1 или 2.")
    first_choise = input()

if first_choise == "1":
    job100000(money)
elif first_choise == "2":
    print("Вы приходите домой. Внезапно раздаётся телефонный звонок. " +
          "Вам звонит Тимур Фархадович - ваш начальник.")
    print("1. Ответить")
    print("2. Сбросить")
    burn_choise = input()
    while burn_choise != "1" and burn_choise != "2":
        print("Введите 1 или 2.")
        burn_choise = input()
    if burn_choise == "1":
        print("Необходимо сначала подключить тариф. Подключить?")
        print("1. Да")
        print("2. Нет")
        no_choise = input()
        print("Поздно. У вас уже нет выбора. Подключение...")
        time.sleep(3)
        print("Подключено.")
        print("К сожалению, вы не успели ответить," +
              "и принимаете решение перезвонить.")
        print("Звонок...")
        time.sleep(5)
        print("Соединение")
        time.sleep(5)
        print("Тимур Фархадович: Почему не на работе? Сколько можно уже? Ты уволен.")
        time.sleep(5)
        print("Вы уволены с работы. Вам предоставлена " +
              "выплата в размере 50 тыс. рублей")
        money += 50000
    else:
        print("Вы уволены с работы.")
    burn = True

print("Из воспоминаний ", name, ":", sep="")
print("\n")
print("08.08.2007, Вечер")
print("Я помню, как сидел на кухне и смотрел телевизор, когда " +
      "мой покой прервал телефонный звонок. Это был мой лучший " +
      "друг Иван. Он пригласил меня в гости, ведь у него сегодня " +
      "День рождения, а отметить не с кем.")

print("1. Согласиться и пойти за подарком")
if not burn:
    print("2. Не согласиться и не идти за подарком")
gift_choise = input()
while gift_choise != "1" and gift_choise != "2" or gift_choise == "2" and burn:
    if not burn:
        print("Введите 1 или 2.")
    else:
        print("Введите 1.")
    gift_choise = input()

if gift_choise == "1":
    print("Выбор за вами:")
    print("1. Заказать на Homeberries")
    print("2. Сходить в магазин")
    buy_choise = input()
    while buy_choise != "1" and buy_choise != "2":
        print("Введите 1 или 2.")
        buy_choise = input()
    if buy_choise == "1":
        print("С вас 1800 рублей.")
        if money >= 1800:
            money -= 1800
            print("Homeberries: оплата. -1800 рублей.")
        else:
            print("Недостаточно средств")
            exit()
        if not burn:
            print("Раздался звонок в дверь. Вы видите курьера, стоящего у двери." +
                  " Он вручает вам ваш заказ и рассказывает жестокую правду.")
            print("* КУРЬЕР БЫЛ ВОЕНКОМОМ *")
            army = True
    else:
        print("Зайдя в магазин, вы сразу приметили нужную вещь.")
        print("Кассир: С вас 1500 рублей.")
        money -= 1500
        if not burn:
            print("Как только вы выходите из магазина," +
                  " вас останавливают двое людей в военной форме," +
                  " и вы сразу понимаете, насколько вы невезучий.")
            army = True

    if not burn:
        print("Из воспоминаний ", name, ":", sep="")
        print("\n")
        print("09.08.2007, Раннее утро")
        print("Я стоял и ждал решения комиссии. Разумеется, мне не хотелось " +
              "идти в армию, и в моей голове начали" +
              " появляться нехорошие мысли...")
        print("1. Подкупить комиссию")
        print("2. Смириться со своей судьбой")
        corr_choise = input()
        while corr_choise != "1" and corr_choise != "2":
            print("Введите 1 или 2.")
            corr_choise = input()
        if corr_choise == "1":
            print("\"Ай-ай-ай, как же так?\" - говорит военком." +
                  " \"Молодой человек, вы знаете," +
                  " что коррупция - это плохо?\"")
            print("Вас настигает мгновенная карма, вы отправляетесь в армию.")
        else:
            print("Вы отправляетесь в армию.")
        army = True
else:
    print("Вас настигает мгновенная карма и вы попадаете в армию")
    army = True

if burn:
    print("Вас уволили с работы и вы понимаете, что нужно найти новую.")
    print("1. Найти новую работу")
    print("2. Остаться безработным")
    job_choice = input()
    while job_choice != "1" and job_choice != "2":
        print("Введите 1 или 2.")
        job_choice = input()
    if job_choice == "1":
        print("Из воспоминаний ", name, ":", sep="")
        print("\n09.08.2007, День")
        print("Я всегда думал, что работа в IT - это интересно," +
              " высокооплачиваемо, безобидно и просто классно." +
              " И вот, у меня появился шанс туда попасть.")
        print("1. Пойти работать в IT по плотному графику")
        print("2. Пойти работать продавцом")
        it_choice = input()
        while it_choice != "1" and it_choice != "2":
            print("Введите 1 или 2.")
            it_choice = input()
        if it_choice == "1":
            it_job(money)
        else:
            money = job_shop(money)
            print("Из воспоминаний ", name, ":", sep="")
            print("\n16.08.2007, Утро")
            print("Я, как обычно, шёл на работу, но на крыльце магазина " +
                  "меня ждал неприятный сюрприз - там стоял военком.")
            print("Я тогда подумал: единственным моим " +
                  "шансом остаётся выезд из страны.")
            print("1. Уехать из страны")
            print("2. Остаться")
            country_choice = input()
            while country_choice != "1" and country_choice != "2":
                print("Введите 1 или 2.")
                country_choice = input()
            if country_choice == "1":
                if money >= 270000:
                    print("Куда едем?")
                    print("1. Германия")
                    print("2. Франция")
                    euro_choice = input()
                    while euro_choice != "1" and euro_choice != "2":
                        print("Введите 1 или 2.")
                        euro_choice = input()
                    if euro_choice == "1":
                        Germany(money)
                    else:
                        France(money)
                else:
                    print("После подсчета средств вы понимаете," +
                          " что денег на поездку вам не хватит.")
                    not_enough = True
            if country_choice == "2" or not_enough:
                print("Вас забирают в армию.")
                army = True

    if job_choice == "2":
        print("1. Устроиться продавцом")
        print("2. Стать контрактником")
        part1_last_choise = input()
        while part1_last_choise != "1" and part1_last_choise != "2":
            print("Введите 1 или 2.")
            part1_last_choise = input()
        if part1_last_choise == "1":
            money = job_shop(money)
            print("Из воспоминаний ", name, ":", sep="")
            print("\n16.08.2007, Утро")
            print("Я, как обычно, шёл на работу, но на крыльце магазина " +
                  "меня ждал неприятный сюрприз - там стоял военком.")
            print("Я тогда подумал: единственным моим " +
                  "шансом остаётся выезд из страны.")
            print("1. Уехать из страны")
            print("2. Остаться")
            country_choice = input()
            while country_choice != "1" and country_choice != "2":
                print("Введите 1 или 2.")
                country_choice = input()
            if country_choice == "1":
                if money >= 270000:
                    print("Куда едем?")
                    print("1. Германия")
                    print("2. Франция")
                    euro_choice = input()
                    while euro_choice != "1" and euro_choice != "2":
                        print("Введите 1 или 2.")
                        euro_choice = input()
                    if euro_choice == "1":
                        Germany(money)
                    else:
                        France(money)
                else:
                    print("После подсчета средств вы понимаете," +
                          " что денег на поездку вам не хватит.")
                    not_enough = True
            if country_choice == "2" or not_enough:
                print("Вас забирают в армию.")
                army = True
        
        if part1_last_choise == "2":
            print("Вы добровольно идете в армию, получив выплату" + 
                  " размером 600 тыс. рублей.")
            army = True
            
if army:
    print("Из воспоминаний " + name + ":")
    print("\n17.08.2007")
    print("Нас в тот день распределяли. Я конечно же выбрал...")
    print("1. Стать сапёром")
    print("2. Стать командиром")
    print("3. Стать капитаном корабля")
    print("4. Стать авиамехаником")
    print("5. Стать механиком для гусеничной техники")
    army_choice = input()
    while (army_choice != "1" and army_choice != "2" and army_choice != "3" 
           and army_choice != "4" and army_choice != "5"):
        print("Нужно было выбрать только одну из перечисленных.")
        army_choice = input()
    
    if army_choice == "1":
        print("Ваша задача, саперы - разминировать поле.")
        print("Чтобы начать взаимодействие с какой-либо клеткой поля," +
              " необходимо ввести её координаты (начинаются с нуля).")
        print("Далее вы должны выбрать: копать здесь или пометить флажком," +
              " то есть как заминированную.")
        print("Если вы решили копнуть и мины там не оказалось, то в клетке" +
              " появится число - количество мин в соседних клетках.")
        print("Если вы поставили флажок и не уверены, что он стоит там" +
              " где надо, не волнуйтесь, вы можете его" +
              " убрать в любой момент.")
        print("Не думаю, что стоит объяснять, что произойдёт," +
              " если вы наступите на мину.")
        print("Введите что-либо для продолжения")
        continue_input = input()
        print("Предмет выдан: справка об обучении на сапера.")
        inventory.append("Справка на сапёра")

    if army_choice == "2":
        print("Обучение вам не понадобится.")

    if army_choice == "3":
        print("Ваша задача, капитаны, уничтожить флот противника.")
        print("Чтобы начать взаимодействие с какой-либо клеткой поля," +
              " необходимо ввести её координаты (начинаются с 1).")
        print("Убедившись, что вы указали правильные координаты, стреляйте.")
        print("Напоминаю, вы командуете эскадрой из 10 кораблей:" +
              " 1 линейный, 2 крейсера, 3 эсминца и 4 катера.")
        print("Идите и без победы не возвращайтесь!")
        print("Введите что-либо для продолжения")
        continue_input = input()
        print("Предмет выдан: справка об обучении на" +
              " капитана морского судна.")
        inventory.append("Справка на капитана")

    if army_choice == "4":
        print("Вы - авиамеханики. Вы должны чинить самолеты." +
              " Обучение вы будете проходить на Су-35С.")
        print("Полное название данного самолета - Single-seat twin-engine" +
              " supermaneuverable Sukhoi Su-35S \"Flanker-E+\" 4++" +
              " generation super fighter jet.")
        print("Какие основные части самолета? Кабина, крылья, двигатели," +
              " шасси, фюзеляж... Но в самолете важно все!" +
              " Поэтому записывайте:")
        print("Для сборки самолёта Су-35С вам потребуются два двигателя" +
              ", 2 крыла, 3 стойки шасси, 1 кабина, 4 инфракрасных ракеты," +
              " 4 радарных ракеты и 2 бомбы.")
        print("Не стоит забывать про обшивку, выполненную" +
              " из титана и алюминия.")
        print("Помните: неправильно соберете самолет, и он упадет.")
        print("Введите что-либо для продолжения")
        input()
        print("Предмет выдан: справка об обучении на авиамеханика.")
        inventory.append("Справка на А-М")

    if army_choice == "5":
        print("Вы - механики для гусеничной техники. Большую часть времени" +
              " вы будете работать с танками, поэтому и" +
              " обучаться будете на них.")
        print("Ваша первостепенная задача - определить, была ли броня" +
              " пробита. По данным о боеприпасе и броне" +
              " вам нужно будет это определить.")
        print("Приведеная толщина брони считается по формуле Z = X *" +
              " (1 / cos(Y)), где X - фактическая толщина брони, Y -" +
              " эффективный угол наклона брони.")
        print("Y равен разности фактического угла наклона брони" +
              " и угла нормализации снаряда.")
        print("Неправильно оценив повреждения, вы " +
              "неправильно отремонтируете технику.")
        print("Введите что-либо для продолжения")
        input()
        print("Предмет выдан: справка об обучении на" +
              " механика для гусеничной техники.")
        inventory.append("Справка на МдГТ")

    print("Из воспоминаний", name, end=":")
    print()
    print("08.08.2008, Утро")
    print("На этот раз я прекрасно помнил, что сегодня у Ивана День" +
          " рождения. Я уже все спланировал: куда пойду, что куплю и т.д...")
    print("...но все мои планы оборвал звук сирены.")
    print("К нам в казарму зашел командир и сказал, что" +
          " началась война и нас отправляют на фронт.")
    print("Конечно, все были в шоке от такого поворота событий," +
          " никто не хотел ехать на войну, и мы стали подумывать о бегстве.")
    
    print("Дезертировать?")
    print("1. Да")
    print("2. Нет")
    run_choice = input()
    while run_choice not in ["1", "2"]:
        print("Введите 1 или 2.")
        run_choice = input()
    
    if run_choice == "1":
        print("Вариантов было немного и мы бежали в Азербайджан," +
              " где нашли дом и работу.")
        Azerbaijan(money)
    else:
        print("Никто не хотел ждать и в этот же день нас" +
              " отправили на задание.")
        if army_choice == "1":
            win = miner(name, inventory)
        if army_choice == "2":
            print("Для командования войсками необходимо было иметь звание" +
                  " Капитана, поэтому нас отправили" +
                  " обычными солдатами на фронт.")
            alive = random.random()
            if alive == 0:
                print("Вы погибли.")
                win = False
            else:
                print("Вы выжили.")
                win = True
        if army_choice == "3":
            win = sea_battle()
        if army_choice == "4":
            avia_mech()
        if army_choice == "5":
            win = tank_test()
    
    if win:
        print("Задание выполнено!")

if win:
    print("Из воспоминаний", name, end=":")
    print("\n13.08.2008")
    print("Нам наконец объявили о конце наших мучений - война закончилась." +
        " За год (с 08.08.2007 до 13.08.2008) на моём банковском счету " +
        "накопилось достаточно денег, чтобы я мог исполнить свою мечту.")
    print(datetime.now())
    print("И сейчас у меня есть", dream, "и я счастлив.")
else:
    print("К сожалению, вы провалили задание, и" +
          " не сможете купить себе", dream, end=".")
