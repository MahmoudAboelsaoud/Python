import turtle
#turtle.forward(100)
#turtle.right(90)
#turtle.color('red')
#turtle.forward(100)
#turtle.left(90)
#turtle.color('green')
#turtle.backward(100)
#turtle.right(90)
#turtle.color('red')
#turtle.backward(100)

#turtle.forward(100)
#turtle.right(90)
#turtle.color('red')
#turtle.forward(100)
#turtle.right(90)
#turtle.color('green')
#turtle.forward(100)
#turtle.right(90)
#turtle.color('red')
#turtle.forward(100)

#############################shaps######################### 
#nbrsides=30
#for steps in range(nbrsides):
#    turtle.forward(100)
#    turtle.right(360/nbrsides)
#    for steps in range(nbrsides):
#        turtle.forward(50)
#        turtle.right(360/nbrsides)
############################################################
#turtle.color('red')
#turtle.forward(200)


#for steps in range(0,10,2):
#    print(steps)

#for steps in [1,2,4,5,8]:
#    print(steps)


#for steps in ['red','green','black','red']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)
    #print(steps)
#############Challenge Octagon draw##############################
shape=8
for steps in range(shape):
    turtle.forward(100)
    turtle.right(360/shape)
    for steps in range(shape):
        turtle.forward(40)
        turtle.right(360/shape)

print("the number of sides in the shape:- ",shape*shape)






