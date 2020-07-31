print(2016 % 4)
print(2559 % 4)

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def is_even(n):
    return True if n % 2 == 0 else False
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

def is_odd(n):
    return not(is_even(n)) #opposite
    # if n % 2 == 1:
    #     return True
    # else:
    #     return False

def promotion(come, pay, per_head, pax):
    #come 4 pay 2
    #come 5 pay =?
    #perhead = 100
    return ((pax // come) * pay * per_head) + ((pax % come) * per_head)
# print(leap_year(2016))
print(is_even(5))
print(is_odd(5))
print(promotion(5, 2, 100, 5))