from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox
import datetime
#############################################################################

file_name ='Final_calcutions.txt'
access_mode ='a+'
#new_text_file =open(file_name, access_mode)
#############################################################################

print("Wellcom To Our Kantayn Calculations ^_^")
print("#" *50)

print(" 1) For Calculate Itims Value .".center(50,"#"))
print(" 2) For Enter Itims Value Direct .".center(50,"#"))
print(" 3) For End The Operation .".center(50,"#"))
print("#" *50)
print("\n")



###############################################################################

def final_calc_fnu_gui() :
    

    root_kantyen_app = Tk() 
    root_kantyen_app.title("Kanteyn Calculations")
    root_kantyen_app.geometry("500x300")


    canvas1=Canvas(root_kantyen_app,width=500, height=350, bg="lightsteelblue")
    canvas1.pack()
    #lable1
    BadahKolaya_label = Label( root_kantyen_app, text =('BadahKolaya'),fg="red",font =("Arail",12)).place(x=10,y=0)
    #BadahKolaya_label.pack()
    #entry1
    BadahKolaya =StringVar()
    BadahKolaya.set("00000")
    BadahKolaya_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = BadahKolaya).place(x=150,y=0)
    #BadahKolaya_Entry.pack()


    #lable2
    Rasalmal_label = Label( root_kantyen_app, text ="Rasalmal",fg="red",font =("Arail",12)).place(x=10,y=30)
    #Rasalmal_label.pack()
    #entry2
    Rasalmal =StringVar()
    Rasalmal.set("00000")
    Rasalmal_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Rasalmal).place(x=150,y=30)
    #Rasalmal_Entry.pack()


    #lable3
    Mokamdad_label = Label( root_kantyen_app, text ="Mokamdad",fg="red",font =("Arail",12)).place(x=10,y=60)
    #Mokamdad_label.pack()
    #entry3
    Mokamdad =StringVar()
    Mokamdad.set("00000")
    Mokamdad_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Mokamdad).place(x=150,y=60)
    #Mokamdad_Entry.pack()

    #lable3
    Moasasa_label = Label( root_kantyen_app, text ="Moasasa",fg="red",font =("Arail",12)).place(x=10,y=90)
    #Moasasa_label.pack()
    #entry3
    Moasasa =StringVar()
    Moasasa.set("00000")
    Moasasa_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Moasasa).place(x=150,y=90)
    #Moasasa_Entry.pack()

    #lable4
    Manfaz_label = Label( root_kantyen_app, text ="Manfaz",fg="red",font =("Arail",12)).place(x=10,y=120)
    #Manfaz_label.pack()
    #entry4
    Manfaz =StringVar()
    Manfaz.set("00000")
    Manfaz_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Manfaz).place(x=150,y=120)
    #Manfaz_Entry.pack()


    #lable5
    Fatar_label = Label( root_kantyen_app, text ="Fatar",fg="red",font =("Arail",12)).place(x=10,y=150)
    #Fatar_label.pack()
    #entry5
    Fatar =StringVar()
    Fatar.set("00000")
    Fatar_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Fatar).place(x=150,y=150)
    #Fatar_Entry.pack()


    #lable6
    Asha_label = Label( root_kantyen_app, text ="Asha",fg="red",font =("Arail",12)).place(x=10,y=180)
    #Asha_label.pack()
    #entry6
    Asha =StringVar()
    Asha.set("00000")
    Asha_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Asha).place(x=150,y=180)
    #Asha_Entry.pack()



    #lable7
    others_label = Label( root_kantyen_app, text ="others",fg="red",font =("Arail",12)).place(x=10,y=210)
    #others_label.pack()
    #entry7
    others =StringVar()
    others.set("00000")
    others_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = others).place(x=150,y=210)
    #others_Entry.pack()


    ############################################################################################
    #border_label = Label( root_kantyen_app, text ="                      ",font =("Arail",12), bg="brown")
    #border_label.pack()
    ############################################################################################
    #lable7
    BadaMorahal_label = Label( root_kantyen_app, text ="BadaMorahal",fg="red",font =("Arail",12)).place(x=320,y=0)
    #BadaMorahal_label.pack()

    #entry7
    BadaMorahal =StringVar()
    BadaMorahal.set("00000")
    BadaMorahal_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = BadaMorahal).place(x=250,y=0)
    #BadaMorahal_Entry.pack()

    #lable8
    Takrasha_label = Label( root_kantyen_app, text ="Takrasha",fg="red",font =("Arail",12)).place(x=320,y=30)
    #Takrasha_label.pack()
    #entry8
    Takrasha =StringVar()
    Takrasha.set("00000")
    Takrasha_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Takrasha).place(x=250,y=30)
    #Takrasha_Entry.pack()


    #lable9
    Nathruat_label = Label( root_kantyen_app, text ="Nathruat",fg="red",font =("Arail",12)).place(x=320,y=60)
    #Nathruat_label.pack()
    #entry9
    Nathruat =StringVar()
    Nathruat.set("00000")
    Nathruat_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Nathruat).place(x=250,y=60)
    #Nathruat_Entry.pack()


    #lable10
    Nakdy_label = Label( root_kantyen_app, text ="Nakdy",fg="red",font =("Arail",12)).place(x=320,y=90)
    #Nakdy_label.pack()
    #entry10
    Nakdy =StringVar()
    Nakdy.set("00000")
    Nakdy_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Nakdy).place(x=250,y=90)
    #Nakdy_Entry.pack()


    #lable11
    Bonat_label = Label( root_kantyen_app, text ="Bonat",fg="red",font =("Arail",12)).place(x=320,y=120)
    #Bonat_label.pack()
    #entry11
    Bonat =StringVar()
    Bonat.set("00000")
    Bonat_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = Bonat).place(x=250,y=120)
    #Bonat_Entry.pack()


    #lable12
    others_side2_label = Label( root_kantyen_app, text ="others",fg="red",font =("Arail",12)).place(x=320,y=150)
    #others_side2_label.pack()
    #entry12
    others_side2 =StringVar()
    others_side2.set("00000")
    others_side2_Entry =Entry(root_kantyen_app, width=5, font =("Arail",12),fg="blue",textvariable = others_side2).place(x=250,y=150)
    #others_side2_Entry.pack()
    
    policy_1_label = Label( root_kantyen_app, text =" القسم الهندسي والجيولوجي",fg="red",font =("Arail",12)).place(x=354,y=250)
    policy_2_label = Label( root_kantyen_app, text =" نقيب / محمد نحله",fg="red",font =("Arail",12)).place(x=376,y=270)
    policy_2_label = Label( root_kantyen_app, text ="Dev.By/ M.aboelsaoud",fg="red",font =("Arail",8)).place(x=2,y=275)
    
    #***************************************************
    def calc_function():
        SumOfFirstSide = (float(Rasalmal.get()) + float(BadahKolaya.get()) + float(Fatar.get()) + float(Asha.get()) + float(Mokamdad.get()) +
        float(Manfaz.get()) + float(Moasasa.get()) ) + float(others.get()) 
        SumOfSecondSide = (float(BadaMorahal.get()) + float(Nakdy.get()) + float(Takrasha.get()) + float(Nathruat.get()) + float(Bonat.get())) + float(others_side2.get()) 
        new_text_file =open(file_name, access_mode)
        
        if((SumOfFirstSide - SumOfSecondSide) <= 0):
            messagebox.showinfo("The Final Result ","IT IS GOOD THERE IS NO LOSE ^_^ The Over = {}".format(SumOfSecondSide - SumOfFirstSide))
            print("IT IS GOOD THERE IS NO LOSE ^_^ The Over = {}".format(SumOfSecondSide - SumOfFirstSide))
            new_text_file.write("\nIT IS GOOD THERE IS NO LOSE ^_^ The Over = {}".format(SumOfSecondSide - SumOfFirstSide))
            print("\n")
        else:
            messagebox.showinfo("The Final Result ","IT IS NOT FINE ^-^ The Lose = {}".format(SumOfFirstSide - SumOfSecondSide))
            print("IT IS NOT FINE ^-^ The Lose = {}".format(SumOfFirstSide - SumOfSecondSide))
            new_text_file.write("\nIT IS NOT FINE ^-^ The Lose = {}".format(SumOfFirstSide - SumOfSecondSide))
            print("\n")
       
    #***************************************************

   
    #creat the button
    btn =Button(root_kantyen_app,text="Calculate",font=("Arial",14),bg="green",borderwidth=0, command = calc_function).place(x=250,y=200)
    #btn.pack()


    root_kantyen_app.mainloop()

#**********************************************************#
print("#" *50)
def CalcuItem( Rasalmal =0,BadahKolaya=0, Fatar =0, Asha = 0, Mokamdad =0, Manfaz =0, Moasasa =0, Nakdy =0, Takrasha =0, Nathruat =0, Bonat =0, BadaMorahal =0):
     print("Sellect The Item You Want To calculate It : ")
     print("""1)Rasalmal  2)BadahKolaya  3)Fatar  4)Asha       5)Mokamdad
6)Manfaz    7)Moasasa      8)Nakdy  9)Takrasha  10)Nathruat  
11)Bonat   12)BadaMorahal   FOR EXIT Press '*'""")
     print(50 *"#")
     num =-1
     while(num !='*'):
       num = input("The Item You Want : ")
   
       if num == "1":
          i=-1
          while(i!= 0):
              i = float(input("Your Selection Is Rasalmal: "))
              Rasalmal = Rasalmal + i
       elif num == "2":
          i=-1
          while(i != 0):
              i = float(input("Your Selection Is BadahKolaya: "))
              BadahKolaya = BadahKolaya + i
       elif num == "3":
            i=-1
            while(i != 0):
              i = float(input("Your Selection Is Fatar: "))
              Fatar = Fatar + i
              Fatar_total=Fatar
       elif num == "4":
           i=-1
           while(i != 0):
              i = float(input("Your Selection Is Asha: "))
              Asha = Asha + i
       elif num == "5":
           i=-1
           while(i != 0):
               i = float(input("Your Selection Is Mokamdad: "))
               Mokamdad = Mokamdad + i
       elif num == "6":
           i=-1
           while(i != 0):
               i = float(input("Your Selection Is Manfaz: "))
               Manfaz = Manfaz + i
       elif num == "7":
           i=-1
           while(i != 0):
               i = float(input("Your Selection Is Moasasa: "))
               Moasasa = Moasasa + i
       elif num == "8":
           i=-1
           while(i != 0):
               i = float(input("Your Selection Is Nakdy: "))
               Nakdy = Nakdy + i
       elif num == "9":
            i=-1
            while(i != 0):
                i = float(input("Your Selection Is Takrasha: "))
                Takrasha = Takrasha + i
       elif num == "10":
           i=-1
           while(i != 0):
               i = float(input("Your Selection Is Nathruat: "))
               Nathruat = Nathruat + i
               #print(Nathruat)
       elif num == "11":
           i=-1
           while(i != 0):
               i = float(input("Your Selection Is Bonat: "))
               Bonat = Bonat + i
               #print(Bonat)
       elif num == "12":
           i=-1
           while(i != 0):
               i = float(input("Your Selection Is BadaMorahal: "))
               BadaMorahal = BadaMorahal + i
     print("#" *50)
     print((" BadahKolaya =  "+str(BadahKolaya)+" ").center(50,"#"))
     print((" Rasalmal    =  "+str(Rasalmal)+" ").center(50,"#"))
     print((" Fatar       =  "+str(Fatar)+" ").center(50,"#"))
     print((" Asha        =  "+str(Asha)+" ").center(50,"#"))
     print((" Mokamdad    =  "+str(Mokamdad)+" ").center(50,"#"))
     print((" Manfaz      =  "+str(Manfaz)+" ").center(50,"#"))
     print((" Moasasa     =  "+str(Moasasa)+" ").center(50,"#"))
     print((" BadaMorahal =  "+str(BadaMorahal)+" ").center(50,"#"))
     print((" Takrasha    =  "+str(Takrasha)+" ").center(50,"#"))
     print((" Nakdy       =  "+str(Nakdy)+" ").center(50,"#"))
     print((" Nathruat    =  "+str(Nathruat)+" ").center(50,"#"))
     print((" Bonat       =  "+str(Bonat)+" ").center(50,"#"))
     print(("#" *50))
     
     current_datatime = datetime.datetime.now()
     new_text_file =open(file_name, access_mode)
     new_text_file.write("\n")
     new_text_file.write("#" *43)
     new_text_file.write("\nOperation Time : "+str(current_datatime))
     new_text_file.write("\n")
     new_text_file.write("#" *43)
     new_text_file.write("\n BadahKolaya =  "+str(BadahKolaya))
     new_text_file.write("\n Rasalmal    =  "+str(Rasalmal))
     new_text_file.write("\n Fatar       =  "+str(Fatar))
     new_text_file.write("\n Asha        =  "+str(Asha))
     new_text_file.write("\n Mokamdad    =  "+str(Mokamdad))
     new_text_file.write("\n Manfaz      =  "+str(Manfaz))
     new_text_file.write("\n Moasasa     =  "+str(Moasasa))
     new_text_file.write("\n BadaMorahal =  "+str(BadaMorahal))
     new_text_file.write("\n Takrasha    =  "+str(Takrasha))
     new_text_file.write("\n Nakdy       =  "+str(Nakdy))
     new_text_file.write("\n Nathruat    =  "+str(Nathruat))
     new_text_file.write("\n Bonat       =  "+str(Bonat))
     new_text_file.write("\n")
     new_text_file.write("#" *43)
     new_text_file.write("\n")
     new_text_file.close()
#**********************************************************#
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
       
#**********************************************************#
sellction ="0"
while sellction != "3":
    sellction = input("Press Number According To Your Need: ").strip()
    if sellction == "1":
        CalcuItem()
    elif sellction == "2":
        final_calc_fnu_gui()
    else:
        print("The Opertion Is Ended ^_^")
    


