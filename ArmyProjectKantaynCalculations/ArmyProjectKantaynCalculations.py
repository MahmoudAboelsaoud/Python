print("Wellcom To Our Kantayn Calculations ^_^")
print("*" *40)

print(""" 1) For Calculate Itims Value .
 2) For Enter Itims Value Direct .
 3) For End The Operation .""")
print("*" *40)
sellction = input("Press Number According To Your Need: ").strip()

Rasalmal =0
Fatar =0
Asha = 0
Mokamdad =0
BadahKolaya =0
Manfaz =0
Moasasa =0
SumOfFirstSide = 0

Nakdy =0
Takrasha =0
Nathruat =0
Bonat =0
BadaMorahal =0
SumOfSecondSide = 0
#**********************************************************#
def CalcuItem( Rasalmal =0, Fatar =0, Asha = 0, Mokamdad =0, Manfaz =0, Moasasa =0, Nakdy =0, Takrasha =0, Nathruat =0, Bonat =0, BadaMorahal =0 ):
     print("Sellect The Item You Want To calculate It : ")
     print("""1)Rasalmal  2)BadahKolaya  3)Fatar  4)Asha  5)Mokamdad
     6)Manfaz  7)Moasasa  8)Nakdy  9)Takrasha  10)Nathruat  11)Bonat  12)BadaMorahal""")
     num =-1
     while(num !='*'):
       num = input("The Item You Want : ")
       if num == "1":
          i=-1
          while(i!= 0):
                i = int(input("Your Selection Is Rasalmal: "))
                Rasalmal = Rasalmal + i
                print(Rasalmal)
       elif num == "2":
          i=-1
          while(i != 0):
             i = int(input("Your Selection Is BadahKolaya: "))
             BadahKolaya = BadahKolaya + i
       elif num == "3":
            i=-1
            while(i != 0):
              i = int(input("Your Selection Is Fatar: "))
              Fatar = Fatar + i
              print(Fatar)
       elif num == "4":
           i=-1
           while(i != 0):
              i = int(input("Your Selection Is Asha: "))
              Asha = Asha + i
       elif num == "5":
           i=-1
           while(i != 0):
               i = int(input("Your Selection Is Mokamdad: "))
               Mokamdad = Mokamdad + i
       elif num == "6":
           i=-1
           while(i != 0):
               i = int(input("Your Selection Is Manfaz: "))
               Manfaz = Manfaz + i
       elif num == "7":
           i=-1
           while(i != 0):
               i = int(input("Your Selection Is Moasasa: "))
               Moasasa = Moasasa + i
       elif num == "8":
           i=-1
           while(i != 0):
               i = int(input("Your Selection Is Nakdy: "))
               Nakdy = Nakdy + i
       elif num == "9":
            i=-1
            while(i != 0):
                i = int(input("Your Selection Is Takrasha: "))
                Takrasha = Takrasha + i
       elif num == "10":
           i=-1
           while(i != 0):
               i = int(input("Your Selection Is Nathruat: "))
               Nathruat = Nathruat + i
               print(Nathruat)
       elif num == "11":
           i=-1
           while(i != 0):
               i = int(input("Your Selection Is Bonat: "))
               Bonat = Bonat + i
               print(Bonat)
       elif num == "12":
           i=-1
           while(i != 0):
               i = int(input("Your Selection Is BadaMorahal: "))
               BadaMorahal = BadaMorahal + i
               print(BadaMorahal) 
 

def EnterItems():
     print("PLZ Enter The First Side Items: ")
     Rasalmal = int(input("The Sum of Rasalmal: "))
     Fatar = int(input("The Sum of Fatar: "))
     Asha = int(input("The Sum of Asha: "))
     Mokamdad = int(input("The Sum of Mokamdad: "))
     BadahKolaya = int(input("The Sum of BadahKolaya: "))
     Manfaz = int(input("The Sum of Manfaz: "))
     Moasasa = int(input("The Sum of Moasasa: "))
     SumOfFirstSide = Rasalmal+ Fatar +Asha +Mokamdad +BadahKolaya +Manfaz +Moasasa
     
     print("PLZ Enter The Secend Side Items: ")
     Nakdy = int(input("The Sum of Nakdy: "))
     Takrasha = int(input("The Sum of Takrasha: "))
     Bonat = int(input("The Sum of Bonat: "))
     Nathruat = int(input("The Sum of Nathruat: "))
     BadaMorahal = int(input("The Sum of BadaMorahal: "))
     SumOfSecondSide = Nakdy+ Takrasha+ Bonat+ Nathruat+ BadaMorahal
     
     if((SumOfFirstSide - SumOfSecondSide) <= 0):
         print("IT IS GOOD THERE IS NO LOSE ^_^ The Over = {}".format(SumOfSecondSide - SumOfFirstSide))
       # print("IT IS GOOD THERE IS NO LOSE ^_^ The Over =")
        #return  str(SumOfSecondSide - SumOfFirstSide)
     else:
         print("IT IS NOT FINE ^-^ The Lose = {}".format(SumOfFirstSide - SumOfSecondSide))
       
   

if sellction == "1":
    CalcuItem()
elif sellction == "2":
    EnterItems()
else:
    print("The Opertion Is Ended ^_^")
    



