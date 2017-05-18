from tkinter import*
from urllib import request
import json

mainWindow=Tk()
mainWindow.resizable(width=FALSE,height=FALSE)
mainWindow.geometry('240x200')
mainWindow.title('Currency converter')

label1=Label(mainWindow,text='USD: ')
label1.place(x=20,y=20)

label2=Label(mainWindow,text='To currency: ')
label2.place(x=20,y=55)

entryText=StringVar()
entry1=Entry(mainWindow,textvariable=entryText)
entry1.place(x=55,y=20)

entryText1=StringVar()
entry2=Entry(mainWindow,textvariable=entryText1)
entry2.place(x=55,y=100)

link = 'http://api.fixer.io/latest?base=USD'
try:
    data = request.urlopen(link)
except:
    print('Error: The server may not be available or the address is incorrect!!!\nPlease check the internet connection!!!')
try:
    jData = data.read()
except NameError:
    print('Error: Due to an error in the previous step we can not continue please check the internet connection!!!')
try:
    rates = json.loads(jData)['rates']
except NameError:
    print('Error: Due to an error in the previous step we can not continue please check the internet connection!!!')

listOfRates=[]
for elem in rates:
   listOfRates.append(elem)

rate=StringVar()
rate.set(listOfRates[0])
optionMenu=OptionMenu(mainWindow,rate,*listOfRates)
optionMenu.place(x=95,y=55)

def click():
    USD=entryText.get()
    convert=float(USD)*rates[rate.get()]
    entryText1.set(str(convert))
button=Button(mainWindow,text='Convert',command=click)
button.place(x=90,y=130)

mainWindow.mainloop()
