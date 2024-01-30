def start():
    print("I invite you to plunge into a wonderful world in which all events, "
          "names and characters are fictional, any coincidences are random, "
          "the game is purely entertaining by clicking continue you agree to the "
          "Terms of Use (https://imgur.com/a/78iYaMk)")
    startgame = input("Continue? (Yes/No) ")

    while startgame.lower() not in ["yes", "no"]:
        if startgame.lower() == "yes":
            entrance()
        elif startgame.lower() == "no":
            print("Goodbye, have a nice day.")
            break
        else:
            print("Invalid input. Please answer 'Yes' or 'No'.")
        startgame = input("Continue? (Yes/No) ")


def library():
    print("You find yourself in a dusty library. "
          "Do you search for secret passages? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return secret_room()
    return armory()


def armory():
    print("You enter the armory, full of ancient weapons. "
          "Climb to the tower? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return tower()
    return great_hall()


def tower():
    print("Atop the tower, you see a locked chest. "
          "Try to open it? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return throne_room()
    return dining_hall()


def throne_room():
    print("You've reached the Throne Room, where the final challenge awaits. "
          "Take the throne? (Yes/No)")
    if get_user_input("> ") == 'yes':
        print("You are now the ruler of the castle! You've won the game!")
    else:
        print("You respectfully decline the throne and exit the castle. Game over.")


def get_user_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response
        print("Invalid input. Please answer 'Yes' or 'No'.")


def entrance():
    print("You stand before a grand old castle. Do you enter? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return great_hall()
    print("You decide not to enter the castle. Game over.")


def great_hall():
    print("You are in the Great Hall. Go to the library? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return library()
    return dining_hall()


def dungeon():
    print("You find yourself in a dungeon. There's a hidden passage. "
          "Enter it? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return secret_room()
    print("You choose to stay. Game over.")


def secret_room():
    print("You've discovered a secret room! You've won the game!")


def gardens():
    print("You walk into the serene gardens. Do you rest by the fountain? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return chapel()
    return observatory()


def observatory():
    print("You're in the observatory. Gaze into the telescope? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return secret_room()
    return servants_quarters()


def chapel():
    print("Inside the chapel, a light glows mysteriously. Investigate? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return underground_tunnel()
    return royal_bedroom()


def servants_quarters():
    print("In the quarters, you hear whispers. Follow the sound? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return kitchen()
    return dining_hall()


def royal_bedroom():
    print("The Royal Bedroom holds many secrets. Search the room? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return alchemists_lab()
    return throne_room()


def kitchen():
    print("You smell delicious food in the kitchen. Eat something? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return stables()
    return gardens()


def dining_hall():
    print("A grand feast is laid out in the Dining Hall. Join the feast? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return royal_bedroom()
    return tower()


def alchemists_lab():
    print("The Alchemist's Lab is full of strange potions. Drink a potion? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return underground_tunnel()
    return observatory()


def stables():
    print("In the stables, a horse is saddled up. Ride the horse? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return gardens()
    return chapel()


def underground_tunnel():
    print("You've discovered an underground tunnel! Follow it? (Yes/No)")
    if get_user_input("> ") == 'yes':
        return secret_room()
    print("You decide not to venture into the unknown. Game over.")


def main():
    print("Welcome to the Castle Adventure!")
    start()


if __name__ == "__main__":
    main()
