def ticket(age, is_local):
    if (age <= 5 or age >= 60) and is_local:#is_local == True
        # return 0 age <= 5 or age >= 60 else 100 #that is ternary
        return 0
    else:
        return 100

def demo(a):
    if a >= 10 and a <= 20: # can write 10 <= a <= 20:
        print("ok")
    else:
        print("not ok")

print(ticket(80, True))
demo(15)