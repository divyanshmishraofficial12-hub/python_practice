#python escape room

import random  #for generating random numbers, choosing random items, and shuffling data.

max_lives=3 #total lives of player

def intro():
    print("welcome to the Python escape game..!")
    print("solve the challenge using logic to escape..!")


def math_first_puzzle():
    answer=int(input("Door 1: what is 7 * 6 +8..?"))
    return True if answer == 50 else False

def pattern_puzzle(attempts=2):
    secret="mystery"
    tries=0

    while tries<attempts:
        guess=input("what is puzzle answer..?").lower()

        if guess =="":
            return "blank"
            continue
        if guess == secret:
            return "u guessed correct..!"
        tries+=1
        print("wrong answer..!")

    return False


#door 3
def door_3(start=1, end =5):
    lucky=random.randint(start, end)

    for i in range(2):
        guess=int(input("guess the number in between(1-5)..?"))
        if guess == lucky:
            return True
    return False

def badge(*badges):
    return random.choice(badges)

def escape_room():
    lives=max_lives
    collected_badges=set()

    while True:
        print("\nChoose a door:")
        print("1. Math Door")
        print("2. Pattern Door")
        print("3. Lucky Door")
        print("4. Exit Game")

        choice = input("Your choice: ")

        if choice == "1":
            if  math_first_puzzle():
                collected_badges.add(badge("Logic Master", "Math Whiz"))
                print("Door unlocked!")
            else:
                lives -= 1

        elif choice == "2":
            if  pattern_puzzle():
                collected_badges.add(badge("Pattern Pro", "Code Breaker"))
                print("Door unlocked!")
            else:
                lives-=1
        elif choice == "3":
            if door_3():
                collected_badges.add(badge("Lucky Star", "Risk Taker"))
                print("Door unlocked!")
            else:
                lives -= 1

        elif choice == "4":
            break

        else:
            print("Invalid door!")

        print(f"Lives left: {lives}")
        print(f"Badges collected: {collected_badges}")

        if lives == 0:
            print("Game Over!")
            break

    print("🏆 Escape Room Ended. Thanks for playing!")


def main():
    intro()
    escape_room()


if __name__ == "__main__":
    main()        


    
