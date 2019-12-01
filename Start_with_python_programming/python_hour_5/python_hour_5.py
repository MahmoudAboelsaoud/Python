#if statment with string
#opinain ="YES"
#answer=input("would you like to git out ? ")
#if answer.upper()== opinain: #convert the answer to upper first than comper .swapcase() 
#    print(" your answer is yes")
#else:
#    print(" your answer is not yes")


#if statment with numarical

#deposit =int(input("How much you want to deposit :- "))
#if deposit > 100:
#    print("your deposit is more than 100$")
#else:
#     print("your deposit is less than 100$")


#************************************calculator********************************* 
print("******************Welcome To Your Calculator*********************")

first_paramater=input("PLZ Enter the first Element: ")
second_paramater=input("PLZ Enter the second Element: ")
operation=input("PLZ Enter the Operation(/ *  + -): ")

if operation == "+":
    resulat = float(first_paramater)+float(second_paramater)
    print("The Resulat Is : ",resulat)
if operation == "-":
    resulat = float(first_paramater)-float(second_paramater)
    print("The Resulat Is : ",resulat)
if operation == "*":
    resulat = float(first_paramater)*float(second_paramater)
    print("The Resulat Is : ",resulat)
if operation == "/":
    if float(second_paramater) == 0:
        print("Invailed Devision By Zero")
    else:
        resulat = float(first_paramater)/float(second_paramater)
        print("The Resulat Is : ",resulat)







