import datetime

CurrentDate = datetime.date.today()
#print(CurrentDate)
#print(CurrentDate.month)
#print(CurrentDate.year)
#print(CurrentDate.strftime('%d %b, %Y'))
#print(CurrentDate.strftime('%d %b, %y'))
#print(CurrentDate.strftime('PlZ attend our event %A, %b %d in the year %Y'))

#UserInput = input('PLZ input your birthday "dd/mm/yyyy":- ')
#birthday = datetime.datetime.strptime(UserInput, '%d/%m/%Y').date()
#print(birthday)
#days = birthday - CurrentDate

#print(days)

#print(CurrentDate.strftime("PLZ attent our birthday event at %A,%B %d in this year %Y "))

UserInput =input("PLZ input your project deadline'd/m/y':-")
DaedLine =datetime.datetime.strptime(UserInput,'%d/%m/%Y').date()
print(DaedLine)

days= DaedLine - CurrentDate
weeks =days/7
days_reminder = days % 7
print("There is only %d days till your deadline" ,days)
print("There is only %d weeks till your deadline" ,weeks)
print("There is only %d days till your deadline" ,days_reminder)





