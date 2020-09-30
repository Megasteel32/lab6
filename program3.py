# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Anthony Matl, Luca Maddaleni, Landon Charles, Nathaniel Michaud
# Group:        8
# Section:      273
# Assignment:   Lab 6 Program 3
# Date:         9/30/2020

# Creating function calc_mpg
def calc_mpg(mph):
    mph = float(mph)
    mpg = -5.9852 + 1.6052 * mph - 0.0141 * mph ** 2
    mpg = round(mpg, 2)
    return mpg


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
        time_list.append(i / distance)
    return vMPH_list, mpg_list, cost_list, time_list

mph, mpg, cost, time = trip(input(), input())
print(mph)
print(mpg)
print(cost)
print(time)