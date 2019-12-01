import turtle

#answer='0'
#while answer !='20':
#    answer=input("PLZ input your ansmer ")
#print("YOU ARE RIGHT")

#counter=0
#while counter < 4:
#    turtle.forward(100)
#    turtle.right(90)
#    counter=counter+1

pen_color = input("PlZ Enter the Pen Color You Want 'red','green','blue':-")
line_lenght= int(input("PlZ Enter The Line Lenght :- "))
angle =int(input("PLZ Enter The Shap Angle:- "))

while line_lenght != 0:
    turtle.color(pen_color)
    turtle.forward(line_lenght)
    turtle.right(angle)
    line_lenght -=1
