import turtle

        
############################# Q4 ###########################

if __name__ == "__main__":  
    while True: 
        pic = turtle.Screen()
        pic.listen()
        pic.onkeypress(lambda: print('Left'),'Left')
        turtle.done()
        
        
############################# Q5 ###########################

def game_time(value):
    dict = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper':'Rock'}
    x = input('Enter Rock, Paper, or Scissors: '  )
    if x!= value and x in dict:
        if dict[x] == value:
            return True 
        else:
            return False
    else: 
        return game_time(value)
        
        