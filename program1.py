pokedex = {}
pokemon = input("WHO'S THAT POKEMON? ")
current_cp = int(input("What's its CP? "))
current_level = int(input("What's its level? "))
candies = int(input("How many candies? "))
pokedex["Pokemon"] = pokemon
pokedex["Current CP"] = current_cp
pokedex["Current Level"] = current_level
pokedex["Candies"] = candies

user_input = 0
while user_input != 3:
    print("Pokemon: {}".format(pokedex["Pokemon"]))
    print("Current CP: {}".format(pokedex["Current CP"]))
    print("Current Level: {}".format(pokedex["Current Level"]))
    print("Candies: {}".format(pokedex["Candies"]))
    print("1 - Add Candy")
    print("2 - Use Candy to Level-Up")
    print("3 - Exit to Main Menu")
    user_input = int(input("Enter 1, 2, or 3: "))
    if user_input == 1:
        candies = int(input("How many candies would you like to add? "))
        pokedex["Candies"] += candies
    if user_input == 2:
        if pokedex["Current Level"] < 31 and pokedex["Candies"] > 0:
            pokedex["Candies"] -= 1
            pokedex["Current Level"] += 1
            pokedex["Current CP"] = (pokedex["Current CP"] * 0.0094) / (0.095 * pokedex["Current CP"]**(1/2))**2
        elif pokedex["Current Level"] < 40 and pokedex["Candies"] > 1:
            pokedex["Candies"] -= 2
            pokedex["Current Level"] += 1
            pokedex["Current CP"] = (pokedex["Current CP"] * 0.0045) / (0.095 * pokedex["Current CP"] ** (1 / 2)) ** 2
        elif pokedex["Current Level"] == 40:
            print("Maximum level is 40!")
        else:
            print("You need more candies!")