#init
import random

print("Welcome to madlibs!")
#func
def story():
    name = input("Please enter a name, or type random: ")
    if name == "random":
        num = random.randint(1, 4)
        if num == 1:
            r_name = "BILL"
        elif num == 2:
            r_name = "CARL"
        elif num == 3:
            r_name = "FRED"
        elif num == 4:
            r_name = "GEORGE"
    else:
        r_name = name.upper()

    food = input("Please enter a food, or type random: ")
    if food == "random":
        num = random.randint(1, 4)
        if num == 1:
            r_food = "CUCUMBER"
        elif num == 2:
            r_food = "CHICKEN"
        elif num == 3:
            r_food = "SANDWICH"
        elif num == 4:
            r_food = "BANANA"
    else:
        r_food = food.upper()

    animal = input("Please enter an animal, or type random: ")
    if animal == "random":
        num = random.randint(1, 4)
        if num == 1:
            r_animal = "DUCK"
        elif num == 2:
            r_animal = "CAT"
        elif num == 3:
            r_animal = "PIGEON"
        elif num == 4:
            r_animal = "DONKEY"
    else:
        r_animal = animal.upper()

    action = input("Please enter an action anding in ing, or type random: ")
    if action == "random":
        num = random.randint(1, 4)
        if num == 1:
            r_action = "RUNNING"
        elif num == 2:
            r_action = "JUMPING"
        elif num == 3:
            r_action = "DANCING"
        elif num == 4:
            r_action = "SINGING"
    else:
        r_action = action.upper()
    pet = input("Please enter an animal to be a pet, or type random: ")
    if pet == "random":
        num = random.randint(1, 4)
        if num == 1:
            r_pet = "CAT"
        elif num == 2:
            r_pet = "DOG"
        elif num == 3:
            r_pet = "FISH"
        elif num == 4:
            r_pet = "BIRD"
    else:
        r_pet = pet.upper()


    print(f"\033[1m{r_name}\033[0m was walking to the store and he saw a bit of \033[1m{r_food}\033[0m flying through the sky. It hit the ground on the street and he went to investigate because it landed on a \033[1m{r_animal}\033[0m. When he got there, he picked it up and started to \033[1m{r_action}\033[0m with it. He dicided to take it home amd feed it to his pet \033[1m{r_pet}\033[0m. His pet really liked it so he decided to try some but then we didnt have anymore so he went and to bed.")
    
#main
story()
