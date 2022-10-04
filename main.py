from ML_Games.November_Day.November_Day import *
from ML_Games.Day_At_Zoo.Day_At_Zoo import *


def Banner():
    print("--------------------------------------------------")
    print("|               Adoni's Mad Libs                 |")
    print("--------------------------------------------------")


def Menu():
    print("\nWhich Mad Libs game would you like to play today?")
    print("(1) November Day")
    print("(2) Day at the Zoo")
    choice = int(input())

    if choice == 1:
        novemberDay = November_Day()
        print("\n")  # line break
        novemberDay.game()
        print("\n")  # line break
    if choice == 2:
        dayAtZoo = Day_At_Zoo()
        print("\n")  # line break
        dayAtZoo.game()
        print("\n")  # line break
    else:
        print("Invalid Input. Please try again")
        Menu()


def main():
    Banner()
    Menu()


if __name__ == "__main__":
    main()
