#language =input("what is your language you speak : ").upper()
#kind =input("what is your kind: " ).upper()
#age=int(input("what is you age : ")) 
#if language =="ENGLISH" and (kind=="MAN" or age > 18):
#    print("HELLO MAN")
#elif language=="GERMAN" and kind=="MAN" \
#    and age > 18:
#    print("GUTAN TUG MAN")
#else:
#    print('I don\'t found your language')

#if age > 18:
#    print("your age is more then 18 year")
#    if kind =="MAN":
#      print("your are man")
#    print("you are welcome")

#********************************Challenge**********************

country =input("PLZ Enter Your Country:- ").upper()
total_order=float(input("PLZ Enter Your Total Order:- "))

if country=="CANADA":
    Province=input("PLZ Enter YOUR Province:- ").upper()
    if Province=="ALBERTA":
        print("Your Charge Is ",total_order*(5/100))
    elif Province=="ONTARIO" or Province=="NEW BRUNSWICK" or Province=="NOVA SCOTIA":
        print("Your Charge Is ",total_order*(13/100))
    else:
        print("Your Charge Is ",total_order*(6/100) + total_order*(5/100))
else:
    print("There Is No Taxes For ",country)
    print("Your Charge Is ",total_order)
