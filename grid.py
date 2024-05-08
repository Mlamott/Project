import math

dist = ("the dist between the point and the origin is,")
comma = (",")
p1 = input ("p1 value: ")
p2 = input ("p2 value: ")

distance = math.sqrt((int(p1)**2) + (int(p2)**2))

print (p1, comma, p2)

if int(p1) > 0 and int(p2) > 0:
    print("this point is in quadrant 1")
elif int(p1) < 0 and int(p2) > 0:
    print("this point is in quadrant 2")
elif int(p1) < 0 and int(p2) < 0:
    print("this point is in quadrant 3")
elif int(p1) > 0 and int(p2) < 0:
    print("this point is in quadrant 4")
elif int(p1) == 0 and int(p2) == 0:
    print("this point is on the orgin")
elif int(p1) == 0:
    print("this point is on the x-axis")
elif int(p1) == 0:
    print("this point is on the y-axis")
    
    