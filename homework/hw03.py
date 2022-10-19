import time



'''
(Problem A)
'''

def bagel_costs(num_bagels, delivery):
    if num_bagels <=6: 
        total_cost = 90*num_bagels
        if delivery:
            total_cost+= 500
    elif num_bagels <= 12:
        total_cost = 80*num_bagels
        if delivery:
            total_cost+= 500
    else: 
        total_cost = 70*num_bagels
        if delivery:
            total_cost+= 500
    return total_cost
            
            
            
'''
(Problem B)
'''

def three_options(text, optionA, optionB, optionC):
    print(text)
    time.sleep(2)
    print(optionA)
    time.sleep(2)
    print(optionB)
    time.sleep(2)
    print(optionC)
    choice = input('what do you choose? (please enter either A,B or C)')
    if choice == 'A':
        return 'A'
    elif choice == 'B':
        return 'B'
    elif choice == 'C' or choice == 'c':
        return 'C'
    else:
        print('Invalid option, defaulting to C')
        return 'C'



'''
(Problem C)
'''

def adventure():
    print('Welcome to your doom...')
    time.sleep(1)
    print('Make good choices to escape...')
    time.sleep(1)
    print('... or dont')
    time.sleep(2)
    q1 = three_options(' You\'re driving down a dark road and suddenly your tire blows do you', 'A) go to the mansion you saw a few miles up the road', 'B) try your phone', 'C) wait for help')
    if q1 == 'A': 
        print('You chose to go to the mansion?!?!?!?!')
        print('Are You crazy?!?!?')
        time.sleep(1)
        print('... o well, your fate not mine...')
        time.sleep(2)
        q2 = three_options('Now that youre here, go inside', 'A Try the front door', 'B try the window', 'C ring the doorbell')
        if q2 == 'A' or q2 == 'B':
            time.sleep(1)
            print('Wow breaking in and entering...')
            time.sleep(1)
            print('Great way to die...')
            return False
        else: 
            time.sleep(1)
            print('The door slowly creeks open...')
            time.sleep(1)
            q3 = three_options('A voice craoks out.... \"Come inside\"', 'A remember your phone and use that' , 'B RUN', 'C offer to sell some girl scout cookies')
            if q3 == 'A':
                q4 = three_options('Your phone is dead.... idiot', 'A wait in the front seat', 'B check the trunk for a charger', 'C run and hope you find the cops before it finds you')
                if q4 == 'A':
                    print('God, youll survive')
                    return True
                else:
                    print('Nice try, youre dead')
                    return False
            elif q3 == 'B': 
                print('Thank you for finally being smart')
                return True
            else: 
                print('Congrats... you got yourself killed')
                return False
    elif q1 == 'B':
        q4 = three_options('Your phone is dead.... idiot', 'A wait in the front seat', 'B check the trunk for a charger', 'C run and hope you find the cops before it finds you')
        if q4 == 'A':
            print('God, youll survive')
            return True
        else:
            print('Nice try, youre dead')
            return False
    else: 
        print('Good job not not being an idiot, you survive')
        return True
    
    