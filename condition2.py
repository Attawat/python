# ==, <>, !=, <, >, <=, >=, not, and, or
score = 75
# if score > 70:
#     print("good")
# else:
#     print("try harder")

def greeting(lang):
    if lang == "th": #compare string
        print("sawadee")
    elif lang == "jp":
        print("konichiwa")
    else:
        print("hello")
greeting("jp")        

def meet_req(eng, interview):
    if eng > 70 and interview > 80:
        return True
    else:
        return False
print(meet_req(80, 700))