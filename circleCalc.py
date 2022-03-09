'''
    Circle area : πr2
    Circle circumference  : 2πr2

    Calculate the area and perimeter of a circle given the radius
'''

r = float(input("Enter the radius of the circle : "))
cArea= 3.14*(r**2)
cCircumference = 2*3.14*r
print("Circle area :{area}\nCircle circumference :{circumfrence}".format(area=cArea,circumfrence=cCircumference))
input()
