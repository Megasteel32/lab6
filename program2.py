# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Anthony Matl, Luca Maddaleni, Landon Charles, Nathaniel Michaud
# Group:        8
# Section:      273
# Assignment:   Lab 6 Program 2
# Date:         9/30/2020

# While user is inputting integers and not 'q'
user_input = 0
list = []
while user_input != "q":
    user_input = input("Enter something! ")
    if user_input != "q": # Checks if user input is q
        user_input = int(user_input)
        if user_input % 2 == 0: # Checks if number is even
            list.append(user_input)
list.sort() # Sorts the list
print(list) # Prints it