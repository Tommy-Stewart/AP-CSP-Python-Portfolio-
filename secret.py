#tommy
#secret
#a game where the computer generates a number and the user has to guess until hey get it right

#init
import random
#func
def game():
        difficulty = input("Please choose a difficulty level, 1, 2, or 3: ") #Asks the user for the difficulty of the game they want to play
        if difficulty == "1":
                number = random.randint(1, 10) #generates the number, same for every time this line appears
                win = 0
                for guess in range(5): #Only allows 5 guesses
                    guess = int(input("Please enter your guess 1-10 here, you have 5 guesses: ")) #tells the user how many guesses they have and what the number range is
                    if guess <= number-5 or guess >= number+5: #these tell the played how far off they are
                        print("Cold, try again")
                    elif guess <= number-3 or guess >= number+3:
                        print("Warm, try again")
                    elif guess <= number-1 or guess >= number+1:
                        print("Hot, try again")
                    elif guess == number:
                        print("Correct! You've finished level 1!") #if the user guesses correctly, this is the message
                        win = 1
                        break
                if win == 0:
                    print("You lose, the number was: ") #This is printed only id=f the person doesnt complete level 1
                    print(number)
        elif difficulty == "2":
            number_2 = random.randint(1, 40)
            win = 0
            for guess in range(5):
                guess = int(input("Please enter your guess 1-40 here, you have 5 guesses: ")) #tells the user how many guesses they have and what the number range is
                if guess <= number_2-20 or guess >= number_2+20:
                    print("Cold, try again")
                elif guess <= number_2-10 or guess >= number_2+10:
                    print("Warm, try again")
                elif guess <= number_2-5 or guess >= number_2+5:
                    print("Hot, try again")
                elif guess == number_2:
                    print("Correct! You've beaten level 2!")
                    win = 1
                    break
            if win == 0:
                print("You lose, the number was: ") #This is printed only id=f the person doesnt complete level 2
                print(number_2)
        elif difficulty == "3":
            number_3 = random.randint(1, 100)
            win = 0
            for guess in range(5):
                guess = int(input("Please enter your guess 1-100 here, you have 5 guesses: ")) #tells the user how many guesses they have and what the number range is
                if guess <= number_3-50 or guess >= number_3+50:
                    print("Cold, try again")
                elif guess <= number_3-20 or guess >= number_3+20:
                    print("Warm, try again")
                elif guess <= number_3-5 or guess >= number_3+5:
                    print("Hot, try again")
                elif guess == number_3:
                    print("Correct! You've beaten level 3!")
                    win = 1
                    break
            if win == 0:
                print("You lose, the number was: ") #This is printed only id=f the person doesnt complete level 3
                print(number_3)
#main
game()
