
import math

# Anna Breck
# Csci 1133
# Homework2


    
# (Problem A) A Few Simple Functions
# Complete the three functions: circumference_circle, gallons_to_liters, and days_to_minutes.

def circumference_circle(diameter):
    # Purpose: to calculate circumference
    # Parameter: diameter
    # Return Value: circumference
    circumference = diameter * math.pi
    return circumference

def gallons_to_liters(gallons):
    # Purpose: convert gallons to liters 
    # Parameter: gallons
    # Return Value: liters
    liters = (1/3.785)*gallons 
    return gallons 

def days_to_minutes(days):
    # Purpose: to state how many minutes in a number of days
    # Parameter: days
    # Return Value: minutes
    minutes = 1440*days
    return minutes

# Problem B  
def trip_cost(students, teachers, own_skates):
    # Purpose: to calculate the total of a trip
    # Parameters: number of teachers and students, number of students who brought their own skates
    #return value: total trip cost
    total_people = students + teachers
    busses = total_people / 50
    if busses % 1 != 0:
        busses = busses//1 + 1
    bus_cost = int(busses * 200)

    lunch = (5*students)+(7*teachers)
    skates = (students-own_skates)*4
    return lunch, bus_cost , skates, lunch + bus_cost + skates 

students = int(input('Students:'))
teachers = int(input('Teachers:'))
own_skates = int(input('Students with own skates:'))
total = trip_cost(students, teachers, own_skates)

print ('Bus Cost:', total[1], '\nLunch Cost:', total[0], '\nRental Cost:', total[2], '\nTotal Cost:', total[3])