# (1) wind chill function 

def wind_chill(t,v):
    windChill = 35.74 + ((0.6215*t)-35.75*(v**0.16))+(0.4275*t*(v**0.16))
    return windChill

t = float(input("Enter temperature in degrees Fahrenheit:" ))
v = float(input("Enter wind velocity in miles/hour:" ))

print("Wind Chill Temperature: ", wind_chill(t,v))


# (2) spare change
def total_change(money):

    dollars = int(money // 1)
    if money - dollars == 0:
        cents = 0
    else: 
        cents = ((money - dollars) *100)+ 1
    q1 = int((cents // 25))
    quarters = int(dollars*4+q1)
    dimes = int((cents - (q1*25)) // 10)
    nickles = int((cents -(q1*25)- (dimes*10)) // 5)
    pennies = int(cents -(q1*25)- (dimes*10)- (nickles*5)) 
    return 'Your change is ', quarters, 'quareters,', dimes,'dimes,', nickles, 'nickles, and', pennies, 'pennies.'

money = float(input("Cash Total: " ))
print(total_change(money))
