from tkinter import *
from tkinter import messagebox

#create the main app window
age_app = Tk()

#change app title
age_app.title("Aboelsaoud Calculator")

#set dimensions
age_app.geometry("400x200")

#write age lable
the_text = Label(age_app, text="Write Your Age", height =2, font=("Arial",14))
the_text.pack() #place the lable in the main window

#age variable  
age = StringVar()
#set def value
age.set("00")
#input for the age
age_input = Entry(age_app, width=2,font=("Arial",14),textvariable = age)
age_input.pack()

#function of the button 
def calc_age():
    the_age_value=age.get()
    months = int(the_age_value)*12
    weeks = months*4
    days = weeks*7
    line_one=f"your age in months {months}"
    line_two=f"your age in weeks {weeks}"
    line_three=f"your age in days {days}"

    all_lines = [line_one, line_two, line_three]
    messagebox.showinfo("Your Age In All Time Units", "\n".join(all_lines))
    

#creat the button
btn = Button(age_app,text="Calculate Age",font=("Arial",14),bg="#e91e63",borderwidth=0,command=calc_age)
btn.pack()



#run the the app for infinte
age_app.mainloop()
