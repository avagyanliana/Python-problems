# import math
# a = int(input("input edge "))
# b = int(input("input next edge "))
# c = math.sqrt(a ** 2 + b ** 2)
# print(c)

# import math
# import cmath
# a = int(input("input a "))
# b = int(input("input b "))
# c = int(input("input c "))
# d = b ** 2 - (4 * a * c)
# if d == 0 :
#     x = - b / 2 * a
#     print(x)
# else :
#     x1 = (- b - cmath.sqrt(d) ) / 2 * a
#     x2 = (- b + cmath.sqrt(d) ) / 2 * a
#     print(x1)
#     print(x2)

# print("Fruits")
# print("Vegetables")
# a = input("input your choice ")
#
# if a != "Quit":
#     if a == "fruits":
#         print("apple")
#         print("peach")
#         b = input("input fruit ")
#         if b == "apple":
#             print("apple")
#         elif b == "peach":
#             print("peach")
#         else:
#             print("Bye !")
#
#     elif a == "vegetables":
#         print("cucumber")
#         print("cauliflower")
#         c = input("input vegetable ")
#         if c == "cucumber":
#             print("cucumber")
#         elif c == "cauliflower":
#             print("cauliflower")
#         else:
#             print("Bye !")
# else:
#     print("Bye !")


# /////////////////// 10 ////////////////////
# print("Rectangle --> 1")
# print("Triangle --> 2")
# print("Circle --> 3")
# print("Quit --> 4")
# shape = int(input("Input shape  "))
#
# if shape == 1:
#     side = int(input("Input side of the rectangle "))
#     side1 = int(input("Input next side of the rectangle "))
#     area = side * side1
#     print("Area is " + str(area))
# elif shape == 2:
#     base = int(input("Input base of triangle "))
#     height = int(input("Input height of triangle "))
#     area = base * height / 2
#     print("Area is " + str(area))
# elif shape == 3:
#     radius = int(input("Input radius of a circle "))
#     area = 3.14 * radius ** 2
#     print("Area is " + str(area))
# else:
#     print("Bye !")


# /////////////////// 11 ////////////////////
# a = 15.9
# num = float(input("Input number here "))
# if num < a:
#     print("-1")
# elif num > a:
#     print("1")
# else:
#     print("0")

# /////////////////// 12 ////////////////////
# low_bound = float(input("Input low bound here "))
# upper_bound = float(input("Input upper bound here "))
# num = float(input("Input number here so I tell u it is in your interval or not "))
# if num < upper_bound and num > low_bound:
#     print("True")
# else:
#     print("False")

# /////////////////// 13 ////////////////////

# lamp = "ON"
# print("lamp is " + lamp)
#
# while True:
#     num = int(input("Input number here "))
#     if num >= 0 and num % 2 == 0:
#         if lamp == "ON":
#             lamp = "OFF"
#         elif lamp == "OFF":
#             lamp = "ON"
#         print("lamp is " + lamp)
#     else :
#         print("lamp is " + lamp)
#     if num <= -1:
#         break

# /////////////////// 14 ////////////////////

# print("\033[1;36;1m Patio --- ON --- 1 ")
# print("\033[1;32;1m Living room --- OFF --- 2")
# print("\033[1;31;1m Garage --- ON --- 3")
# print("\033[1;34;1m Garden --- OFF --- 4")
# print("")
#
# patio = "ON"
# living_room = "OFF"
# garage = "ON"
# garden = "OFF"
#
# while True:
#     switch = int(input("\033[1;37;1m Choose one of the options  "))
#     if switch == 1:
#         if patio == "ON":
#             patio = "OFF"
#         elif patio == "OFF":
#             patio = "ON"
#         print("\033[1;36;1m patio ---> " + patio)
#         print("\033[1;32;1m living_room ---> " + living_room)
#         print("\033[1;31;1m garage ---> " + garage)
#         print("\033[1;34;1m garden ---> " + garden)
#     elif switch == 2:
#         if living_room == "ON":
#             living_room = "OFF"
#         elif living_room == "OFF":
#             living_room = "ON"
#         print("\033[1;36;1m patio ---> " + patio)
#         print("\033[1;32;1m living_room ---> " + living_room)
#         print("\033[1;31;1m garage ---> " + garage)
#         print("\033[1;34;1m garden ---> " + garden)
#     elif switch == 3:
#         if garage == "ON":
#             garage = "OFF"
#         elif garage == "OFF":
#             garage = "ON"
#         print("\033[1;36;1m patio ---> " + patio)
#         print("\033[1;32;1m living_room ---> " + living_room)
#         print("\033[1;31;1m garage ---> " + garage)
#         print("\033[1;34;1m garden ---> " + garden)
#     elif switch == 4:
#         if garden == "ON":
#             garden = "OFF"
#         elif garden == "OFF":
#             garden = "ON"
#         print("\033[1;36;1m patio ---> " + patio)
#         print("\033[1;32;1m living_room ---> " + living_room)
#         print("\033[1;31;1m garage ---> " + garage)
#         print("\033[1;34;1m garden ---> " + garden)
#     else:
#         print("Please choose from offered options only")

# /////////////////// 15 ////////////////////

# print("AUA_Wifi --- 1")
# print("AUA_Guest --- 2")
# print("Liana's phone --- 3")
#
# first = "AUA_Wifi"
# second = "AUA_Guest"
# third = "Liana's phone"
#
# while True:
#     switch = int(input("Input your choice  "))
#     if switch == 1:
#         print(first + "  CONNECTED")
#         print(second)
#         print(third)
#     elif switch == 2:
#         print(first)
#         print(second + "  CONNECTED")
#         print(third)
#     elif switch == 3:
#         print(first)
#         print(second)
#         print(third + "  CONNECTED")


# /////////////////// 16 ////////////////////
# n = int(input("Input n "))
# for i in range(n):
#     print("ALL WORK AND NO PLAY, MAKES HOVAK A VERY DULL BOY")
#     i += 1

# /////////////////// 17  18   19   20  ////////////////////

# for i in range(1, 10):
#     print(i)
#     i += 1
# for i in range(1, 10, 2):
#     print(i)
#     i += 1

# m = int(input("Input starting point "))
# n = int(input("Input ending point "))
# for i in range(m, n + 1):
#     if i % 2 == 0:
#         print(i)
#     i += 1


# /////////////////// 21 ////////////////////


# m = int(input("Input starting point "))
# n = int(input("Input ending point "))
#
# ifm = int(input("Is m inclusive? type : yes -- 1 or no -- 0 "))
# ifn = int(input("Is n inclusive? type : yes -- 1 or no -- 0 "))
#
# if ifm == 0:
#     m = m + 1
#
# if ifn == 1:
#     n = n + 1
#
# for i in range(m, n):
#     if i % 2 == 0:
#         print(i)
#         i += 1

# /////////////////// 22 ////////////////////

# number = int(input("Input number "))
# for i in range(number):
#     if i % 2 == 0:
#         print()
#         print("\033[31;1;47m ALL WORK AND NO PLAY MAKES HOVAK A VERY DULL BOY \033[m")
#     else:
#         print()
#         print("\033[30;1;41m ALL WORK AND NO PLAY MAKES HOVAK A VERY DULL BOY \033[m")

# /////////////////// 23 ////////////////////
# from math import pow
# x1 = input("Input the first root ")
# x2 = input("Input the second root ")
#
# sign = "+"
# b = -(float(x1) + float(x2))
# c = float(x1) * float(x2)
#
# print()
# print(str(pow(x, 2)) + " " + sign +  " " + str(b) + "x" + " " + sign + " " + str(c) + " = 0")

# /////////////////// 24 ////////////////////

# n = int(input("Input number here  "))
# for i in range(n):
#     print("*" * n)

# /////////////////// 26 ////////////////////

length = int(input("Input length  "))
width = int(input("Input width  "))
border = input("Input border character  ")
fill = input("Input fill character  ")
a = length - 2
b = width - 2

print(border, border * (length - 2), border)
for i in range(width - 2):
    print(border, fill * a, border)
print(border, border * (length - 2), border)


# /////////////////// 27 ////////////////////

# n = int(input("Input n  "))
# a = 1
# ch = "#"
#
# for i in range(n):
#     print(ch * n)
#     n -= 1
#
# for j in range(1, n + 1):
#     print(ch * a)
#     a += 1



