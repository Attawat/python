def prompay(money):
    if money > 100000:
        return 10
    elif money > 30000:
        return 5
    elif money > 5000:
        return 2
    else:
        return 0
        
print("fee = ", prompay(50))