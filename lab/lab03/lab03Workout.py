# (1) Printing letter count
def print_letters(val):
    if val == 1 or val == 2 or val == 6:
        print(3)
    elif val == 4 or val == 5 or val == 9:
        print(4)
    else:
        print(5)

# (2) return letters
def return_letters(val):
    if val == 1 or val == 2 or val == 6:
        return 3
    elif val == 4 or val == 5 or val == 9:
        return 4
    else:
        return 5
    
# (4) Most letters
def most_letters(num1, num2, num3):
    x =return_letters(num1)
    y = return_letters(num2)
    z = return_letters(num3)
    most = 0
    if x > y and x > z:
        most = num1 
        return num1, 'has the most letters!'
    elif x < y and y > z:
        most = num2
        return num2, 'has the most letters!'
    elif x < z and y < z:
        most = num3 
        return num3, 'has the most letters!'
    elif x == y:
        return 'It\'s a tie!', num1, 'and', num2
    elif x == z: 
        return 'It\'s a tie!', num1, 'and', num3
    elif y == z: 
        return 'It\'s a tie!', num2, 'and', num3
    else: 
        return 'Threeway Tie!'
    



num1 = int(input('first number: ' ))
num2 = int(input('second numer: ' ))
num3 = int(input('third number: '))

print(most_letters(num1, num2, num3))