def rectangle(w, h): #dynamic typing
    # code block 
    area = w * h
    return area
def triangle(w, h):
    area = 0.5 * w * h
    # return area
    return 0.5 * w * h

w = int(input("width = ")) 
h = int(input("height = ")) 
print(rectangle(w, h))
print(triangle(w, h))