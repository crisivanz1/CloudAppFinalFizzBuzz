fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = fizz + buzz
increment3 = 3
increment5 = 5
APP_FILE = "FizzBuzz.py"

def Default():
    for i in range(1,101):
        if i % increment3 == 0 and i % increment5 == 0:
            print(fizzbuzz)
        elif i % increment3 == 0:
            print(fizz)
        elif i % increment5 == 0:
            print(buzz)
        else:
            print(i)

def OnePlayer():
    failed = False
    print("Hello player! Hope you know how to play FizzBuzz!")
    for i in range(1,101):
        playerEntry = str(input("Your turn: "))
        if i % increment3 == 0 and i % increment5 == 0:
            if playerEntry.upper() != (fizzbuzz.upper()):
                failed = True
            else:
                print(fizzbuzz)
        elif i % increment3 == 0:
            if playerEntry.upper() != (fizz.upper()):
                failed = True
            else:
                print(fizz)
        elif i % increment5 == 0:
            if playerEntry.upper() != (buzz.upper()):
                failed = True
            else:
                print(buzz)
        else:
            if playerEntry != str(i):
                print("Whoops, wrong answer. You lose!")
                break
            else:
                print(i)
        if failed == True:
            print("Whoops, wrong answer. You lose!")
            break
        if i == 100:
            print("\nYou win!")
        
    print("\nThanks for playing FizzBuzz!")
                
def VsCPU():
    playerTurn = True
    print("Hello player! Hope you know how to play FizzBuzz! Your opponent today is a machine!")
    for i in range(1,101):
        failed = False
        if playerTurn == True:
            playerEntry = str(input("Your turn: "))
            if i % increment3 == 0 and i % increment5 == 0:
                if playerEntry.upper() != (fizzbuzz.upper()):
                    failed = True
                else:
                    print(fizzbuzz)
                    playerTurn = False
            elif i % increment3 == 0:
                if playerEntry.upper() != (fizz.upper()):
                    failed = True
                else:
                    print(fizz)
                    playerTurn = False
            elif i % increment5 == 0:
                if playerEntry.upper() != (buzz.upper()):
                    failed = True
                else:
                    print(buzz)
                    playerTurn = False
            else:
                if playerEntry != str(i):
                    failed = True
                else:
                    print(i)
                    playerTurn = False
            if failed == True:
                print("Whoops, wrong answer. You lose!")
                break

            if i == 100:
                print("\nYou win!")
                
        else:
            if i % increment3 == 0 and i % increment5 == 0:
                print(fizzbuzz)
                playerTurn = True
            elif i % increment3 == 0:
                print(fizz)
                playerTurn = True
            elif i % increment5 == 0:
                print(buzz)
                playerTurn = True
            else:
                print(i)
                playerTurn = True


    print("\nThanks for playing FizzBuzz!")

def TwoPlayer():
    currentPlayer = True
    failed = False
    print("Hello players! Hope you know how to play FizzBuzz! Today you're facing each other!")
    for i in range(1,101):
        if currentPlayer == True:
            playerEntry = str(input("Player 1's turn: "))
        else:
            playerEntry = str(input("Player 2's turn: "))
        if i % increment3 == 0 and i % increment5 == 0:
            if playerEntry.upper() != (fizzbuzz.upper()):
                failed = True
            else:
                print(fizzbuzz)
                currentPlayer = not currentPlayer
        elif i % increment3 == 0:
            if playerEntry.upper() != (fizz.upper()):
                failed = True
            else:
                print(fizz)
                currentPlayer = not currentPlayer
        elif i % increment5 == 0:
            if playerEntry.upper() != (buzz.upper()):
                failed = True
            else:
                print(buzz)
                currentPlayer = not currentPlayer
        else:
            if playerEntry != str(i):
                failed = True
            else:
                print(i)
                currentPlayer = not currentPlayer
        if failed == True:
            if currentPlayer == True:
                print("Whoops, wrong answer Player 1!")
                print("Player 2, you win!")
                break
            else:
                print("Whoops, wrong answer Player 2!")
                print("Player 1, you win!")
                break

    print("\nThanks for playing FizzBuzz!")
                

menuOptions = ["1", "2", "3", "4"]
print("Welcome to the FizzBuzz program, Python Edition!")

while True:
    userInput = str(input("Choose a menu option: "))
    if userInput not in menuOptions:
        print("bruh, choose again")
    else:
        if userInput == menuOptions[0]:
            Default()
        elif userInput == menuOptions[1]:
            OnePlayer()
        elif userInput == menuOptions[2]:
            VsCPU()
        elif userInput == menuOptions[3]:
            TwoPlayer()
        break

