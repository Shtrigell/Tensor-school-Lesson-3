x = 0
y = 0
steps=0
while steps != "Уйти":
    steps= input(""" Куда вы хотите пойти:
    U - один шаг вверх
    D - один шаг вниз
    R - один шаг вправо
    L - один шаг влево
    Если захотите уйти введите - Уйти
    """)
    if steps == "U":
        y+=1
    elif steps == "D":
        y-=1
    elif steps == "R":
        x+=1
    elif steps =="L":
        x-=1
    else:
        print("Неизвестная команда")
print("Ваша координата X: ",x,"Ваша координата Y: ",y)
