
# (1) Rounding function
def roundit(number):
    if number % 1 >= .5:
        number = int(number) + 1
    elif number % 1 < .5 and number % 1 > 0:
        number = int(number)
    else: 
        return 'Already Rounded :)' 
    return 'Rounded number is', int(number)

# (2) Test case
# For my specific function at least 4 would be needed


chooseYourDestiny = float(input('What number shall i round for you today?'))
print(roundit(chooseYourDestiny))

