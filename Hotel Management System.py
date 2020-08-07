from tkinter import *
import time
from tkinter import ttk
import datetime

msg1 = "Welcome to Hotel Management System..."
msg2 = "Welcome to our Hotel.."
msg3 = "Order your Meal .."
msg4 = "Thank you for your patronage.."
msg5 = "Welcome to Hotel Management System..."
msg6 = "Welcome to Hotel Management System..."
text1 = ""
n = 0

#=========================Calculator Functions=======================

def btn(numbers):
    global  operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def Clear():
    global operator
    operator = ''
    txt_input.set('')
    Display.insert(0,'Start Calculating...')

def Equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

#===================================Total Function=================================
def TotalResult():
    #================Cost of Meal======================
    varme1 = Mealdicator.get()
    varme2 = Meal1.get()
    if varme1 == 'Fried Rice':
       varme3 = (varme2*25)
       Cost.set(varme3)
    elif varme1 == 'Spring Roll':
        varme3 = (varme2*50)
        Cost.set(varme3)
    elif varme1 == 'Pizza':
        varme3 = (varme2*100)
        Cost.set(varme3)
    elif varme1 == 'Chowmein':
        varme3 = (varme2*100)
        Cost.set(varme3)
    elif varme1 == 'Burger':
        varme3 = (varme2*150)
        Cost.set(varme3)
    else:
        varme3 = (varme2 *50)
        Cost.set(varme3)

    # ================Cost of Drink======================
    vardi1 = Drinkdicator.get()
    vardi2 = Drink1.get()
    if vardi1 == 'Bottled Water':
        vardi3 = (vardi1 * 18 )
        Drinks.set(vardi3)
    elif vardi1 == 'Coca Cola':
        vardi3 = (vardi2 * 20)
        Drinks.set(vardi3)
    elif vardi1 == 'Pepsi':
        vardi3 = (vardi2 * 20)
        Drinks.set(vardi3)
    elif vardi1 == 'Frooti':
        vardi3 = (vardi2 * 15)
        Drinks.set(vardi3)
    elif vardi1 == 'Red Wine':
        vardi3 = (vardi2 * 2500)
        Drinks.set(vardi3)
    else:
        vardi3 = (vardi2 * 0.0)
        Drinks.set(vardi3)

    #======================Delivery Cost========================================
    num1 = float(Cost.get())
    num2 = float(Drinks.get())
    Delivery = (num1 + num2) / 5

    #======================Cost of Room==========================================
    room = v.get()
    null = 0.0

    rvip = 10.0 #============Cost of VIP room======================================
    rvip1 = Delivery/(10*2500) #====VIP room with Delivery cost===================

    rnormal = 5.0 #=========Cost of Normal room====================================
    rnormal1 = Delivery/(5*200) #======Normal room with Delivery cost============

    if room == 1:
        if chkb1.get() == 1:
            Service_Charge.set(rvip1)
            RoomCost.set(2000.0)
            DevCost.set(Delivery)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(1500.0)
    elif room == 2:
        if chkb1.get() == 1:
            Service_Charge.set(rnormal)
            RoomCost.set(1200.0)
            DevCost.set(Delivery)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(1000.0)
    elif room == 3:
        if chkb1.get() == 1:
            Service_Charge.set(null)
            RoomCost.set(null)
            DevCost.set(null)
        else:
            Service_Charge.set(null)
            DevCost.set(null)
            RoomCost.set(null)

    #==================Total Result=========================
    num3 = float(DevCost.get())
    num4 = float(RoomCost.get())
    num5 = float(Service_Charge.get())

    MyTotal = num1+num2+num3+num4+num5
    Total.set(MyTotal)
    FinalTotal = "Total = Rs",MyTotal

    num6 = Total.get()
    Display.delete(0,END)
    Display.insert(0,FinalTotal)

    if num6 == '0.0':
        Display.delete(0,END)
        Display.insert(0,'Please,make an order...')


def Convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2 == 'China':
        Display.delete(0,END)
        var4 = ('Yuan',(var3*10.78560))
        Display.insert(0,var4)
    elif var2 == 'France':
        Display.delete(0,END)
        var4 = ('Euro',(var3*88.973779))
        Display.insert(0,var4)
    elif var2 == 'India':
        Display.delete(0,END)
        var4 = ('Rupees',(var3*1))
        Display.insert(0,var4)
    elif var2 == 'Mexico':
        Display.delete(0,END)
        var4 = ('MXN',(var3*3.338197))
        Display.insert(0,var4)
    elif var2 == 'Nigeria':
        Display.delete(0,END)
        var4 = ('Naira',(var3*0.19446))
        Display.insert(0,var4)
    elif var2 == 'USA':
        Display.delete(0,END)
        var4 = ('USD',(var3*74.806616))
        Display.insert(0,var4)
    else:
        Display.delete(0,END)
        Display.insert(0,'Error:Select a country!')

    #============================Reset Button======================

'''def scroll():
    for line in Line:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')'''

def Hotel():
    Display.delete(0,END)
    Display.insert(0,'Hotel Management System.')

def Powered():
    Display.delete(0, END)
    Display.insert(0, 'Powered by Python...')

def Reset():
    Display.delete(0, END)
    Display.insert(0, 'System Resetting...')
    Display.after(2000,Hotel)
    Display.after(4000,Powered)
    Display.after(6000,Rest)

def Rest():
    Clear()
    Display.delete(0,END)
    Display.insert(0,'Hello! Welcome')
    Mealdicator.set(value='Delicious Meal')
    Drinkdicator.set(value='Fresh Drink')
    indicator.set(value='Choose a Country')
    txtQtyofMeal.delete(0,END)
    txtQtyofMeal.insert(0,0)
    txtQtyofDrink.delete(0,END)
    txtQtyofDrink.insert(0,0)
    txtAmount.delete(0,END)
    txtAmount.insert(0,0)
    RoomCost.set(0.0)
    Total.set(0.0)
    Service_Charge.set(0.0)
    Drinks.set(0.0)
    Cost.set(0.0)
    chkb1.set(0)
    v.set(3)
    DevCost.set(0.0)

#==========================Clear Button========================
def ClearScreen():
    Display.delete(0,END)
    RoomCost.set('')
    Total.set('')
    Service_Charge.set('')
    Drinks.set('')
    Cost.set('')
    DevCost.set('')

#===============================Exit===========================
def Stop():
    root.destroy()

def Exit():
    Display.delete(0,END)
    Display.insert(0,'Thanks for patronage...')
    Display.after(3000,Stop)

#============================Time================================
def tick():
    d = datetime.datetime.now()
    Today = '{:%B %d, %Y}'.format(d)

    mytime = time.strftime('%I:%M:%S%p')
    lblInfo.config(text=(mytime+' '+Today))
    lblInfo.after(200,tick)

#=================================Scroll Function===============
def display():
    global text1, n, msg1
    for t in range(len(msg1)):
        for k in range(t):
            text1 += ' '
        for g in range(len(msg1) - t):
            text1 += msg1[g]
        text1 = text1.strip()
        f2.update()
        f2.after(150)
        text1 = text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1 = ''
    scroll_text.set('')
    txtscroll.after(150,display)

root = Tk()
root.geometry('800x400+0+0')
root.title('Hotel Management System')

#================================Window's Partition==============================
Tops = Frame(root, width=800, height=100, bg='blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=200,height=200,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=100, height=200,relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=35, height=200, relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root, width=100, height=200, relief=SUNKEN)
f4.pack(side=LEFT)

#===================================Main Screen==================================
txt_input = StringVar(value = 'Welocme to Our Hotel...')
Display = Entry(Tops, font=('arial',57,'bold'),fg='white',bd=40,bg='blue',justify='right',textvariable=txt_input)
Display.grid(columnspan=4)

#==================================Date and time=================================

lblInfo = Label(f2,font=('arial',15,'bold'),fg='dark blue',bd=5,anchor=W)
lblInfo.grid(row=1,column=0,columnspan=4)
tick()



#================================Choose Meal===================================
Meal1 = IntVar()
Mealdicator = StringVar(value='Delicious Meals')

lblMeal = Label(f1,font=('arial',16,'bold'),text='Choose Meal',bd=10,anchor=W)
lblMeal.grid(row=0,column=0)
txtMeal = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Mealdicator)
txtMeal['values']=('Fried Rice','Spring Rolls','Pizza','Chowmein','Burger')
txtMeal.grid(row=0,column=1)

lblQtofMeal = Label(f1,font=('arial',16,'bold'),text='Qty. of Meal',bd=10,anchor=W)
lblQtofMeal.grid(row=1,column=0)
txtQtyofMeal = Entry(f1,font=('arial',16,'bold'),textvariable=Meal1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtyofMeal.grid(row=1,column=1)

#================================Choose Drinks====================================
Drink1 = IntVar()
Drinkdicator = StringVar(value='Fresh Drinks')

lblDrink = Label(f1,font=('arial',16,'bold'),text='Choose Drink',bd=10,anchor=W)
lblDrink.grid(row=2,column=0)
txtDrink = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Drinkdicator)
txtDrink['values']=('Bottled Water','Coca Cola','Pepsi','Frooti','Red Wine')
txtDrink.grid(row=2,column=1)

lblQtofDrink = Label(f1,font=('arial',16,'bold'),text='Qty. of Drink',bd=10,anchor=W)
lblQtofDrink.grid(row=3,column=0)
txtQtyofDrink = Entry(f1,font=('arial',16,'bold'),textvariable=Drink1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtyofDrink.grid(row=3,column=1)

#==============================Order Delivery=====================================
chkb1 = IntVar()

lblHomeDev = Label(f1,font=('arial',16,'bold'),text='Order Delivery',bd=10,anchor=W)
lblHomeDev.grid(row=4,column=0)
check1 = Checkbutton(f1,text='Yes',variable=chkb1,font=('arial',16,'bold'))
check1.grid(row=4,column=1)

#==========================Book a Room============================================
v = IntVar()
v.set(3)

lblRoom = Label(f1,font=('arial',16,'bold'),text='Book a Room',bd=10, anchor=W)
lblRoom.grid(row=5,column=0)
MyRadios = Radiobutton(f1,text='VIP',font=('arial',16,'bold'),variable=v,value=1)
MyRadios.grid(row=5,column=1,sticky=W)
MyRadios = Radiobutton(f1,text='Normal',font=('arial',16,'bold'),variable=v,value=2)
MyRadios.grid(row=5,column=1)
MyRadios = Radiobutton(f1,text='No',font=('arial',16,'bold'),variable=v,value=3)
MyRadios.grid(row=5,column=1,sticky=E)

#================================Cost Display Screens============================
Cost = StringVar()
lblMeal1 = Label(f1, font=('arial',15,'bold'),text='Cost of Meal',bd=15,anchor=W)
lblMeal1.grid(row=0,column=2)
txtMeal1 = Entry(f1,font=('arial',15,'bold'),textvariable=Cost,fg='white',bd=10,insertwidth=4,bg='blue',
                 justify='right')
txtMeal1.grid(row=0,column=3)

Drinks = StringVar()
lblDrink1 = Label(f1, font=('arial',15,'bold'),text='Cost of Drink',bd=15,anchor=W)
lblDrink1.grid(row=1,column=2)
txtDrink1 = Entry(f1,font=('arial',15,'bold'),textvariable=Drinks,fg='white',bd=10,insertwidth=4,bg='blue',
                  justify='right')
txtDrink1.grid(row=1,column=3)

DevCost = StringVar()
lblDev = Label(f1, font=('arial',15,'bold'),text='Delivery Cost',bd=15,anchor=W)
lblDev.grid(row=2,column=2)
txtDev = Entry(f1,font=('arial',15,'bold'),textvariable=DevCost,fg='white',bd=10,insertwidth=4,bg='blue',
               justify='right')
txtDev.grid(row=2,column=3)

RoomCost = StringVar()
lblRoom = Label(f1, font=('arial',15,'bold'),text='Cost of Room',bd=15,anchor=W)
lblRoom.grid(row=3,column=2)
txtRoom = Entry(f1,font=('arial',15,'bold'),textvariable=RoomCost,fg='white',bd=10,insertwidth=4,bg='blue',
                justify='right')
txtRoom.grid(row=3,column=3)

Service_Charge = StringVar()
lblService = Label(f1, font=('arial',15,'bold'),text='Service Fee',bd=15,anchor=W)
lblService.grid(row=4,column=2)
txtService = Entry(f1,font=('arial',15,'bold'),textvariable=Service_Charge,fg='white',bd=10,insertwidth=4,bg='blue',
                   justify='right')
txtService.grid(row=4,column=3)

Total = StringVar()
lblTotal = Label(f1, font=('arial',15,'bold'),text='Total Cost',bd=15,anchor=W)
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('arial',15,'bold'),textvariable=Total,fg='white',bd=10,insertwidth=4,bg='blue',
                 justify='right')
txtTotal.grid(row=5,column=3)

#====================================Currency Converter===================================
var1 = IntVar()
indicator = StringVar(value='Choose a Country')

lblCunCon = Label(f1,font=('arial',16,'bold italic'),text='-----------------------------------Currency Converter---------------------------------------',
                  bd=20,anchor=W)
lblCunCon.grid(row=6,column=0,columnspan=4)

lblCountry = Label(f1,font=('arial',16,'bold'),text='Nationality',bd=20,anchor=W)
lblCountry.grid(row=7,column=0)
txtCountry = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=indicator)
txtCountry['values'] = ('China','France','India','Mexico','Nigeria','USA')
txtCountry.grid(row=7,column=1)

lblAmount = Label(f1,font=('arial',16,'bold'),text='Amount',bd=20,anchor=W)
lblAmount.grid(row=7,column=2)
txtAmount = Entry(f1,font=('arial',16,'bold'),textvariable=var1,bd=10,insertwidth=4,bg='white',justify='right')
txtAmount.grid(row=7,column=3)

#=======================================Control Buttons=========================================
btnConvert = Button(f1,padx=10,pady=4,bd=16,fg='white',font=('arial',14,'bold'),width=10,text='Convert',bg='orange',
                    command=Convert)
btnConvert.grid(row=8,column=2)

btnTotal = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',14,'bold'),width=10,text='Total',bg='orange',
                  command=TotalResult)
btnTotal.grid(row=0,column=0)

btnScreen = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',14,'bold'),width=10,text='Clear',bg='blue',
                   command=ClearScreen)
btnScreen.grid(row=1,column=0)

btnReset = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',14,'bold'),width=10,text='Reset',bg='green',
                  command=Reset)
btnReset.grid(row=2,column=0)

btnExit = Button(f4,padx=10,pady=8,bd=16,fg='white',font=('arial',14,'bold'),width=10,text='Exit',bg='red',
                 command=Exit)
btnExit.grid(row=3,column=0)

#========================================Logo=======================================================
photo = PhotoImage(file='Icon.png')
myphoto = Label(f1,image=photo)
myphoto.grid(row=8,column=0)

#=====================================Scrollable Text===============================================
scroll_text = StringVar()
txtscroll = Entry(f2, textvariable=scroll_text, font=('arial',16,'bold'), fg='white', bd=10, bg='blue', width=32)
txtscroll.grid(row=0, column=0, columnspan=4)
display()

root.mainloop()
