print("Please Guass Number Between 0 and 100 ^_^")

print("Is your Number Is 50 ")
print(""" If your Number gteater Then Press h
          If your Number less Then Press l
          Enter c if the Number Is Correct""")
user_input= input()

low =0
med =50
high =100


while user_input!='c':
    if user_input=='l':
        while user_input=='l':
             #low=low
             high=med
             med=(low+high)/2
             print("Is your Number Is %s " %int(med))
             print(""" If your Number gteater Then Press h
                       If your Number less Then Press l
                       Enter c if the Number Is Correct""")
             user_input= input()
    elif user_input=='h':
        while user_input=='h':
            #high=high
            low=med
            med=(low+high)/2
            print("Is your Number Is %s " %int(med))
            print(""" If your Number gteater Then Press h
                      If your Number less Then Press l
                      Enter c if the Number Is Correct""")
            user_input= input()

print("Game Over the Number is %s" %int(med))


