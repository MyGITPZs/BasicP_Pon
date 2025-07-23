mie = float(input("ระยะทาง : "))
if mie >= 5 and mie <= 50 :
    print("10 B")
elif mie >= 51 and mie <= 100 :
    print("15 B")
elif mie >= 101 and mie <= 300 :
    print("25 B")
elif mie >= 301 and mie <= 500 :
    print("35 B")
elif mie > 500 :
    print("45 B")
else:
    print("ไม่ส่ง")