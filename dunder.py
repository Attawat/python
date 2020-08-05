import area
def rectangle(w, h):
    return w * h
# special variables __name__
if __name__ == "__main__": #dunder = double underscore that is entry point
    print(__name__)
    print(rectangle(3,5))
    print(area.triangle(444, 3))
#if __name__ == "__main__":ถ้าเกิดมี function นี้เครื่องจะทำงานแค่ในคำสั่งนี้ แต่ถ้าสมมุติเอาคำสั่งนี้ออกเวลา import file เข้ามาเครื่องจะทำงานทั้งหมดเลย
#สามารถสร้างเพื่อเช็คแค่ในแต่ละฟังชั้น พอเอา่ออกไปช้างนอกเอาแค่สมการบางฟังชันออกไป