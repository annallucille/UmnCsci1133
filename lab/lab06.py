

'''
Warm Up 

Problem (A)
Average grade
'''

def filter_average(can):
    if can[6] >= 85:
        return True
    else: 
        return False
    
'''
Problem (B)
Mininmum Grade
'''
def filter_no_fail(can):
    for std in can:
        if std < 65:
            return False
    return True

'''
Sretch 

Problem (A)
More detailed approaches
'''
def filter_4_high(can):
    can.sort()
    for n in range(0,4):
        if can[n] < 85:
            return False
    return True

'''
Problem (B)
average again?
'''

def filter_averageCS(cand):
    avg = (sum(cand[0,6])/6)
    if avg >= 85:
        return True
    else: 
        return False
    
'''
Workout 

Problem (A)
'''
def filter_all_nf(applicants_list):
    fails = []
    for cand in applicants_list:
        n= filter_no_fail(cand)
        if n == False:
            fails.append(applicants_list.index(cand))