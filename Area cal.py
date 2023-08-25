print("AREA CALCULATOR(InCM)")
print("Choose your shape","1.circle","2.triangle","3.square","4.rectangle","5.parallogram")
x=int(input("enter your shape"))
if x==1:
    print("CIRCLE")
    a=int(input("enter the radius"))
    print("Area of circle",22/7*a*a,"cm")
elif x==2:
    print("TRIANGLE")
    b=int(input("enter the base"))
    c=int(input("enter the height"))
    print("Area of triangle",1/2*b*c,"cm")
elif x==3:
    print("SQUARE") 
    a=int(input("enter the side"))
    print("Area of square",a*a,"cm")
elif x==4:
    print("RECTANGLE")
    l=int(input("enter the length"))
    b=int(input("enter the width"))
    print("Area of reactangle",l*b,"cm")
elif x==5:
    print("PARLLOGRAM")
    b=int(input("enter the base"))
    h=int(input("enter the vertical height"))
    print("Area of parallogrm",b*h,"cm")

print("PROGRAM OVER")    
