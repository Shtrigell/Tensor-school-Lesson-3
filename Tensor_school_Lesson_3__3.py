import math
print("Введите коэффициенты уравнения")
a=float(input("Коэффициент a "))
b=float(input("Коэффициент b "))
c=float(input("Коэффициент c "))
print(f"Ваше уравнение: ",a,"x^2+",b,"x+",c,sep ="")
discr = (b**2)-(4*a*c)
print("Дискриминант равен: ",discr)
if discr>0:
      x_1 = float((-b+math.sqrt(discr))/2*a)
      x_2 = float((-b-math.sqrt(discr))/2*a)
      print("Ваши корни : X1 = ",x_1,"X2 = ",x_2)
elif discr==0:
    x = -b/(2*a)
    print("X = ")
else:
  print("Корней нет")
