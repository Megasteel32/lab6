# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Anthony Matl, Luca Maddaleni, Landon Charles, Nathaniel Michaud
# Group:        8
# Section:      273
# Assignment:   Lab 6 Program 1
# Date:         9/30/2020

# Defining dictionary and asking for input from users
pokedex = {}
pokemon = input("WHO'S THAT POKEMON? ")
current_cp = int(input("What's its CP? "))
current_level = int(input("What's its level? "))
candies = int(input("How many candies? "))

# Adding user input to dictionary
pokedex["Pokemon"] = pokemon
pokedex["Current CP"] = current_cp
pokedex["Current Level"] = current_level
pokedex["Candies"] = candies

# Main loop
user_input = 0
while user_input != 3:
    # Printing out menu with stored values
    print("Pokemon: {}".format(pokedex["Pokemon"]))
    print("Current CP: {}".format(pokedex["Current CP"]))
    print("Current Level: {}".format(pokedex["Current Level"]))
    print("Candies: {}".format(pokedex["Candies"]))
    print("1 - Add Candy")
    print("2 - Use Candy to Level-Up")
    print("3 - Exit to Main Menu")
    user_input = int(input("Enter 1, 2, or 3: "))
    if user_input == 1:
        # Adding user inputted candies to dictionary
        candies = int(input("How many candies would you like to add? "))
        pokedex["Candies"] += candies
    if user_input == 2:
        # Checking for current level
        if pokedex["Current Level"] < 31 and pokedex["Candies"] > 0:
            # Adding correct CP if the level is between 1 and 30
            pokedex["Candies"] -= 1
            pokedex["Current Level"] += 1
            pokedex["Current CP"] = (pokedex["Current CP"] * 0.0094) / (0.095 * pokedex["Current CP"]**(1/2))**2
        elif pokedex["Current Level"] < 40 and pokedex["Candies"] > 1:
            # Adding correct CP if the level is between 31 and 40
            pokedex["Candies"] -= 2
            pokedex["Current Level"] += 1
            pokedex["Current CP"] = (pokedex["Current CP"] * 0.0045) / (0.095 * pokedex["Current CP"] ** (1 / 2)) ** 2
        elif pokedex["Current Level"] == 40:
            # If the pokemon is at level 40, no CP is added
            print("Maximum level is 40!")
        else:
            # If the user doesn't have enough candies for the level upgrade needed, tell them so
            print("You need more candies!")