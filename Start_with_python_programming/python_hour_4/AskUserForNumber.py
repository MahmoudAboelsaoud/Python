#salary = input("Plase input your salary ")
#bonus = input("Plase input your bonus ")

#paycheckAmount = float(salary) + float(bonus)

#print(paycheckAmount)
###################################################################
# the Loan Calculator

#Declare and initialize the variables
Loan_Amount = 0
Interest_Rate = 0
Num_Payment = 0

#ask user for input data
Loan_Amount = input("PLZ input your Loan Amount :- ")
Interest_Rate =input("PLZ input your Interest Rate :- ")
Num_Payment =input("PLZ input the Number of Payments :- ")

L =float(Loan_Amount)
i =float(Interest_Rate)
Num_Payment = 12 *Num_Payment
n =float(Num_Payment) 

monthly_payment = M =L*(i*(i+1)*n)/((i+1)*n-1)
print("The monthly_payment for you is:- %f " %M)
print("The monthly_payment for you is:- " + str(M))

