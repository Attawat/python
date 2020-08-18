# point = 1, 7 #tuple
# print(point[0])
# print(point[1])
# 
# pointB = (1, 7) #same line 1
# print(pointB[0])
# 
# th = "Thailand", 5, 10, 15
# print(th[1] + th[2] + th[3])
# 
# monster = ("pikuchu", "bulbasaur", "eevee")

def distance(pointA, pointB):
    return ((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)**0.5

pointA = 1, 7
pointB = 1, 10

d = distance(pointA, pointB)
print(d)
 #when not use tuple use 4 variable

 #immutable ไม่สามารถเปลี่ยนแปลง หรือแก้ไข เมื่อมีการสร้างครั้งแรก ต่างจาก List ที่เป็นแบบ mutable สามารถแก้ไขได้
  