
#this program will answer questions about national parks and if the user does not know what national park to ask about, it will ask them some questions to help find them a good park

#init
import pandas as pd
data = pd.read_csv("parks.csv")
id = data["id"]
name = data["Name"]
image = data["Image"]
location = data["Location"]
established = data["Date established"]
area = data["Area in acres"]
visitors = data["Recreation visitors in 2019"]
description = data["Description"]

filter = []     #Blank array used for filtering data

#func

def region(state):      #sorts through the locations and filters the name of the parks in that state into an array
    for i in range(len(name)):
        if state in location[i]:
            filter.append(name[i])
    if filter == []:
        print(f"Sorry there are no National parks in {state}")
    else:
        print(f"Here is a list of parks that are located in {state}: \n {filter}")

def size(land_mass):
    if land_mass == "small":
        for i in range(len(area)):
            if area[i] <= 75000:
                filter.append(name[i])
        print(f"Here is a list of Parks that are small: \n {filter}")
        filter.clear()
    elif land_mass == "medium":
        for i in range(len(area)):
            if area[i] <= 750000 and area[i] >= 75001:
                filter.append(name[i])
        print(f"Here is a list of Parks that are medium: \n {filter}")
        filter.clear()
    elif land_mass == "large":
        for i in range(len(area)):
            if area[i] >= 750001:
                filter.append(name[i])
        print(f"Here is a list of Parks that are large: \n {filter}")
        filter.clear()
def locate(park):      #sorts through the names of the parks and the locations and helps the user locate the park tey are looking for
    for i in range(len(name)):
        if park in name[i]:
            filter.append(location[i])
    print(f"{park} is located in {filter}")
    filter.clear()
def age(park):      #sorts through the names and year the park was established in order to teel the user when the park the enter was established
    for i in range(len(name)):
        if park in name[i]:
            filter.append(established[i])
    print(f"This park was founded on {filter}")
    filter.clear()
def popularity(park):      #sorts through the parks and visitors in order to give the user info about the amount of visitors
    for i in range(len(name)):
        if park in name[i]:
            filter.append(visitors[i])
    print(f"There are {filter} people that are here every year")
    filter.clear()
def desc(park):      #gives the user a description of the park they are asking about
    for i in range(len(name)):
        if park in name[i]:
            filter.append(i)
    print(f"Here is a description of {park}:")
    print(f"{description[i]} \nif you follow the link below it will show you an image of {park} \n{image[i]}")
    filter.clear()

def main():
    print("Hello! Welcome to the national park helper! This program will ask you some questions and then help you find information about specific national parks.")
    while True:
        start = input("Do you already know what the name of the National Park is? (yes/no): ")
        if start == "yes":
            print("Perfect, that is very helpful")
            print("We can answer several questions yoiu might not know about the park you are thinking of")
            park = input("What is the name of your Park?: ").title()
            while True:
                second = input("Would you like to; 1) know when it was founded, 2) know what state it is in, 3) know how popular it is, or 4) have a description and image of it: ")
                if second == "1":
                    age(park)
                    q = input("Would you like to ask another question? (yes/no): ")
                    if q == "no":
                        print("Thank you for participating")
                        exit()
                elif second == "2":
                    locate(park)
                    q = input("Would you like to ask another question? (yes/no): ")
                    if q == "no":
                        print("Thank you for participating")
                        exit()
                elif second == "3":
                    popularity(park)
                    q = input("Would you like to ask another question? (yes/no): ")
                    if q == "no":
                        print("Thank you for participating")
                        exit()
                elif second == "4":
                    desc(park)
                    q = input("Would you like to ask another question? (yes/no): ")
                    if q == "no":
                        print("Thank you for participating")
                        exit()
                else:
                    print("Invalid input")
                    q = input("Would you like to ask another question? (yes/no): ")
                    if q == "no":
                        print("Thank you for participating")
                        exit()

        elif start == "no":
            print("That's ok, I can help with that")
            while True:
                state = input("What state are you looking for a National Park in?: ").title()
                region(state)
                if filter == []:
                    print("Please try another state")
                else:
                    filter.clear()
                    second = input("Do any of these catch your eye? (yes/no): ")
                    if second == "no":
                        print("Ok maybe you might know how big a park you are looking for, this could give you options outside of the state you were initially looking for")
                        land_mass = input("Are you looking for a park that's small, medium, or large?: ")
                        size(land_mass)
                        next = input("Do and of these catch your eye? (yes/no): ")
                        if next == "no":
                            print("Sorry we are unable to help you, have a nice day")
                        elif next == "yes":
                            park = input("What is the name of your Park?: ").title()
                            print("Perfect, now we help you learn more about your park")
                            while True:
                                third = input("Would you like to; 1) know when it was founded, 2) know what state it is in, 3) know how popular it is, or 4) have a description and image of it: ")
                                if third == "1":
                                    age(park)
                                    q = input("Would you like to ask another question? (yes/no): ")
                                    if q == "no":
                                        print("Thank you for participating")
                                        exit()
                                elif third == "2":
                                    locate(park)
                                    q = input("Would you like to ask another question? (yes/no): ")
                                    if q == "no":
                                        print("Thank you for participating")
                                        exit()
                                elif third == "3":
                                    popularity(park)
                                    q = input("Would you like to ask another question? (yes/no): ")
                                    if q == "no":
                                        print("Thank you for participating")
                                        exit()
                                elif third == "4":
                                    desc(park)
                                    q = input("Would you like to ask another question? (yes/no): ")
                                    if q == "no":
                                        print("Thank you for participating")
                                        exit()
                                else:
                                    print("Invalid input")
                                    q = input("Would you like to ask another question? (yes/no): ")
                                    if q == "no":
                                        print("Thank you for participating")
                                        exit()

                    elif second == "yes":
                        park = input("What is the name of your Park?: ").title()
                        while True:
                            print("Great, we can answer several questions about it to give you more info")
                            third = input("Would you like to; 1) know when it was founded, 2) know what state it is in, 3) know how popular it is, or 4) have a description and image of it: ")
                            if third == "1":
                                age(park)
                                q = input("Would you like to ask another question? (yes/no): ")
                                if q == "no":
                                    print("Thank you for participating")
                                    exit()
                            elif third == "2":
                                locate(park)
                                q = input("Would you like to ask another question? (yes/no): ")
                                if q == "no":
                                    print("Thank you for participating")
                                    exit()
                            elif third == "3":
                                popularity(park)
                                q = input("Would you like to ask another question? (yes/no): ")
                                if q == "no":
                                    print("Thank you for participating")
                                    exit()
                            elif third == "4":
                                desc(park)
                                q = input("Would you like to ask another question? (yes/no): ")
                                if q == "no":
                                    print("Thank you for participating")
                                    exit()
                            else:
                                print("Invalid input")
                                q = input("Would you like to ask another question? (yes/no): ")
                                if q == "no":
                                    print("Thank you for participating")
                                    exit()
                    else:
                        print("Invalid input, please try again")
                    break

#main
main()


