from tkinter import *
#from tkinter import ttk
from tkinter import messagebox

root_kantyen_app = Tk()
root_kantyen_app.title("Kanteyn Calculations")
root_kantyen_app.geometry("400x600")


#lable1
BadahKolaya_label = Label( root_kantyen_app, text =('BadahKolaya'),fg="red",font =("Arail",12))
BadahKolaya_label.pack()
#BadahKolaya_label.grid(column=0, row=0)
#entry1
BadahKolaya =StringVar()
BadahKolaya.set("0000")
BadahKolaya_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = BadahKolaya)
BadahKolaya_Entry.pack()


#lable2
Rasalmal_label = Label( root_kantyen_app, text ="Rasalmal",fg="red",font =("Arail",12))
Rasalmal_label.pack()
#entry2
Rasalmal =StringVar()
Rasalmal.set("0000")
Rasalmal_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Rasalmal)
Rasalmal_Entry.pack()


#lable3
Mokamdad_label = Label( root_kantyen_app, text ="Mokamdad",fg="red",font =("Arail",12))
Mokamdad_label.pack()
#entry3
Mokamdad =StringVar()
Mokamdad.set("0000")
Mokamdad_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Mokamdad)
Mokamdad_Entry.pack()

#lable3
Moasasa_label = Label( root_kantyen_app, text ="Moasasa",fg="red",font =("Arail",12))
Moasasa_label.pack()
#entry3
Moasasa =StringVar()
Moasasa.set("0000")
Moasasa_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Moasasa)
Moasasa_Entry.pack()

#lable4
Manfaz_label = Label( root_kantyen_app, text ="Manfaz",fg="red",font =("Arail",12))
Manfaz_label.pack()
#entry4
Manfaz =StringVar()
Manfaz.set("0000")
Manfaz_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Manfaz)
Manfaz_Entry.pack()


#lable5
Fatar_label = Label( root_kantyen_app, text ="Fatar",fg="red",font =("Arail",12))
Fatar_label.pack()
#entry5
Fatar =StringVar()
Fatar.set("0000")
Fatar_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Fatar)
Fatar_Entry.pack()


#lable6
Asha_label = Label( root_kantyen_app, text ="Asha",fg="red",font =("Arail",12))
Asha_label.pack()
#entry6
Asha =StringVar()
Asha.set("0000")
Asha_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Asha)
Asha_Entry.pack()

############################################################################################
border_label = Label( root_kantyen_app, text ="                      ",font =("Arail",12), bg="brown")
border_label.pack()
############################################################################################
#lable7
BadaMorahal_label = Label( root_kantyen_app, text ="BadaMorahal",fg="red",font =("Arail",12))
BadaMorahal_label.pack()
#entry7
BadaMorahal =StringVar()
BadaMorahal.set("0000")
BadaMorahal_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = BadaMorahal)
BadaMorahal_Entry.pack()

#lable8
Takrasha_label = Label( root_kantyen_app, text ="Takrasha",fg="red",font =("Arail",12))
Takrasha_label.pack()
#entry8
Takrasha =StringVar()
Takrasha.set("0000")
Takrasha_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Takrasha)
Takrasha_Entry.pack()


#lable9
Nathruat_label = Label( root_kantyen_app, text ="Nathruat",fg="red",font =("Arail",12))
Nathruat_label.pack()
#entry9
Nathruat =StringVar()
Nathruat.set("0000")
Nathruat_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Nathruat)
Nathruat_Entry.pack()


#lable10
Nakdy_label = Label( root_kantyen_app, text ="Nakdy",fg="red",font =("Arail",12))
Nakdy_label.pack()
#entry10
Nakdy =StringVar()
Nakdy.set("0000")
Nakdy_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Nakdy)
Nakdy_Entry.pack()


#lable11
Bonat_label = Label( root_kantyen_app, text ="Bonat",fg="red",font =("Arail",12))
Bonat_label.pack()
#entry11
Bonat =StringVar()
Bonat.set("0000")
Bonat_Entry =Entry(root_kantyen_app, width=4, font =("Arail",12),fg="blue",textvariable = Bonat)
Bonat_Entry.pack()

###############################################################################
def calc_function():
    SumOfFirstSide = (int(Rasalmal.get()) + int(BadahKolaya.get()) + int(Fatar.get()) + int(Asha.get()) + int(Mokamdad.get()) +
          int(Manfaz.get()) + int(Moasasa.get()) )
    SumOfSecondSide = (int(BadaMorahal.get()) + int(Nakdy.get()) + int(Takrasha.get()) + int(Nathruat.get()) + int(Bonat.get()))

    if((SumOfFirstSide - SumOfSecondSide) <= 0):
         messagebox.showinfo("The Final Result ","IT IS GOOD THERE IS NO LOSE ^_^ The Over = {}".format(SumOfSecondSide - SumOfFirstSide))
         print("IT IS GOOD THERE IS NO LOSE ^_^ The Over = {}".format(SumOfSecondSide - SumOfFirstSide))
    else:
         messagebox.showinfo("The Final Result ","IT IS NOT FINE ^-^ The Lose = {}".format(SumOfFirstSide - SumOfSecondSide))
         print("IT IS NOT FINE ^-^ The Lose = {}".format(SumOfFirstSide - SumOfSecondSide))
       
###############################################################################
#creat the button
btn =Button(root_kantyen_app,text="Calculate",font=("Arial",14),bg="green",borderwidth=0, command = calc_function)
btn.pack()


root_kantyen_app.mainloop()