import random
from string import capwords
###### Warm up ######

def word_freq(fname):
    fp = open(fname)
    counts = {}
    for line in fp:
        words = line.split()
        for word in words:
            if word in counts: 
                counts[word] += 1
            else:
                counts[word] = 1
    fp.close()
    return counts
 


####### Stretch ######
 
def morse(message):
    morse_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}
    string = [*message]
    morse_string = []
    for letter in string:
        morse_string.append(morse_dictionary[letter])
    message = ''.join(morse_string)
    return message



###### Work Out ######


costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}
total = costs['Chicago']['Las Vegas'] + costs['Las Vegas']['Dallas']
print(total)

def cheapest(origin, destination):
    costs = {'Philadelphia':{'Chicago':227, 'Dallas':289},
         'Chicago':{'Philadelphia':227, 'Dallas':105, 'Las Vegas':56},
         'Dallas':{'Philadelphia':289, 'Houston':173, 'Chicago':105,
                   'Las Vegas':44, 'San Diego':303},
         'Houston':{'Dallas':173},
         'Las Vegas':{'Chicago':56, 'Dallas':44, 'San Diego':74,
                      'Los Angeles':44, 'San Francisco':56},
         'Los Angeles':{'Las Vegas':44, 'San Diego':157,
                        'San Francisco':111},
         'San Diego':{'Las Vegas':44, 'Los Angeles':157, 'Dallas':303},
         'San Francisco':{'Las Vegas':56, 'Los Angeles':111}}
    for i in costs[origin]: 
        if destination in costs[i]:
            connecting_total = costs[i][destination] + costs[origin][i]
    if costs[origin][destination]:
        direct_total = costs[origin][destination]
    if connecting_total < direct_total:
        return connecting_total
    elif direct_total < connecting_total:
        return direct_total 
    else:
        return 'equal'
        
            
            
            