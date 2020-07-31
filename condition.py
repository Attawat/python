def rectangle(w, h): #dynamic typing
    # code block 
    area = w * h
    return area
def triangle(w, h):
    area = 0.5 * w * h
    # return area
    return 0.5 * w * h

print("1.rectangle")
print("2.triangle")
n = input("please select option: ")
w = int(input("width = ")) 
h = int(input("height = ")) 
if n == "1": #compare string
    print("rectangle area = ")
    print(rectangle(w, h))
else:
    print("triangle area = ")
    print(triangle(w, h))