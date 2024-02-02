print("Hello, a funny quest welcomes you, choose numbers and try to complete the quest.")
print("How are you?")
print("1) Bad")
print("2) it's all right")
print("3) good")
answer = int(input())
if answer == 1:
    print("The level is decant)")
    print("What was Lenin's name?")
    print("1) Vladimir")
    print("2) Aleksey")
    a = int(input())
    if a == 1:
        print("When the Chernobyl disaster took plase?")
        print("1) 1990")
        print("2) 1986")
        b = int(input())
        if b == 2:
                print("How much is 37 + 15?")
                print("1) 52")
                print("2) 42")
                c = int(input())
                if c == 1:
                    print("Guess the puzzle:")
                    print("♕ vi russia")
                    print("1) Coronavirus")
                    print("2) Corova")
                    d = int(input())
                    if d == 1:
                        print("You' complited the quest")
                    else:
                        print("You haven't complited the quest")
                else:
                    print("You haven't complited the quest")
        else:
            print("You haven't complited the quest")
    else:
        print("You haven't complited the quest")
elif answer == 2:
    print("The level is average")
    print("Which girl was the first to fly into space?")
    print("1) Tereshkova")
    print("2) Savitscaya")
    a1 = int(input())
    if a1 == 1:
        print("How many bits are in a byte?")
        print("1) 10")
        print("2) 8")
        b1 = int(input())
        if b1 == 2:
            print("How many legs does a spider have?")
            print("1) 6")
            print("2) 8")
            c1 = int(input())
            if c1 == 2:
                print("who discovered the electron?")
                print("1) Tompson")
                print("2) Bor")
                d1 = int(input())
                if d1 == 1:
                    print("You' complited the quest")
                else:
                    print("You haven't complited the quest")
            else:
                print("You haven't complited the quest")
        else:
            print("You haven't complited the quest")
    else:
        print("You haven't complited the quest")
else:
    print("Difficult level")
    print("Who invented the computer?")
    print("1) Shicard")
    print("2) Djobs")
    a2 = int(input())
    if a2 == 2:
        print("Who discovered Antarctica?")
        print("1) Belingshausen and Lazarev")
        print("2) Cook")
        b2 = int(input())
        if b2 == 1:
            print("How many wonders of the world?")
            print("1) 7")
            print("2) 6")
            c2 = int(input())
            if c2 == 1:
                print("What was Mozart's name?")
                print("1) Sirius")
                print("2) Amadey")
                d2 = int(input())
                if d2 == 2:
                    print("You' complited the quest")
                else:
                    print("You haven't complited the quest")
            else:
                print("You haven't complited the quest")
        else:
            print("You haven't complited the quest")
    else:
        print("You haven't complited the quest")
print("Good bye!)")
