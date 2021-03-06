# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Anthony Matl, Luca Maddaleni, Landon Charles, Nathaniel Michaud
# Group:        8
# Section:      273
# Assignment:   Lab 6 Program 3
# Date:         9/30/2020

from matplotlib import pyplot as pyp


# Creating function calc_mpg
def calc_mpg(mph):
    mph = float(mph)
    mpg = -5.9852 + 1.6052 * mph - 0.0141 * mph ** 2
    mpg = round(mpg, 2)
    return mpg


# Creating function trip
def trip(fuel_cost, distance):
    fuel_cost, distance = float(fuel_cost), float(distance)
    vMPH_list = []
    mpg_list = []
    cost_list = []
    time_list = []
    for i in range(5, 85, 5):
        vMPH_list.append(i)
    for i in range(5, 85, 5):
        mpg_list.append(calc_mpg(i))
    for i in mpg_list:
        cost_list.append(round((distance / i) * fuel_cost, 2))
    for i in vMPH_list:
        time_list.append(round(distance / i, 2))
    return vMPH_list, mpg_list, cost_list, time_list, fuel_cost, distance


mph, mpg, cost, time, fuel_cost, distance = trip(input("Enter the current cost of fuel per gallon: "),
                                                 input("Enter the distance you wish to travel: "))
user_input = 0
while user_input != 5:
    print("1 - Create a table")
    print("2 - Create a plot of cost vs speed")
    print("3 - Create a plot of cost vs time")
    print("4 - Calculate the cost and time at a specific speed")
    print("5 - Quit")
    user_input = int(input("Enter your selection: "))
    if user_input == 1:
        print("|", "MPH", " " * (6 - len("mph")),
              "|", "MPG", " " * (9 - len("mpg")),
              "|", "Cost", " " * (6 - len("Cost")),
              "|", "Hours", " " * (9 - len("Hours")), "|")
        for i in range(16):
            print("|", mph[i], "mph", " " * (2 - len(str(mph[i]))),
                  "|", mpg[i], "mpg", " " * (5 - len(str(mpg[i]))),
                  "|", "$" + str(cost[i]), " " * (5 - len(str(cost[i]))),
                  "|", time[i], "hours", " " * (2 - len(str(time[i]))), "|")
    if user_input == 2:
        pyp.plot(mph[4:], cost[4:])
        pyp.xlabel("Miles per Hour")
        pyp.ylabel("Cost in Dollars")
        pyp.show()
    if user_input == 3:
        pyp.plot(time[4:], cost[4:])
        pyp.xlabel("Time in Hours")
        pyp.ylabel("Cost in Dollars")
        pyp.show()
    if user_input == 4:
        user_mph = int(input("Enter the specific speed: "))
        user_mpg = calc_mpg(user_mph)
        user_cost = round((distance / user_mph) * fuel_cost, 2)
        user_time = round(distance / user_mph, 2)
        print("The cost and time needed at {} mph are ${} and {} Hours.".format(user_mph, user_cost, user_time))