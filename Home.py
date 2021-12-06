from tkinter import *
import tkinter.messagebox as tm
import tkinter.font as font
import ast

def displaylot(l):#returns a 2d matrix type of string to display as the parking area
    design=""
    for i in l:
        for j in i:
            design+=j+"   "
        design+="\n---------------------------------\n"
    return design[0:(len(design)-1)]

def displayhome():#displays the home tkinter window
    home.geometry("1300x800")
    home.configure(bg="black")
    home.title("Python Parking Management System")
    title=Frame(home,width=1300,height=50,bg="black")
    # fontstyle=font.Font(family="Atlas",size=40)
    Label(home,text="Python Parking Management System",font=("Times New Roman",40),bg="black",fg="white").pack(side=TOP)
    title.pack(side=TOP)
    img=PhotoImage(file="carback.png")
    c=Canvas(home,height=300,width=400)
    c.create_image(170,100,image=img)
    c.pack()
    services=Frame(home,width=1300,height=400,bg="black")
    Button(services,text="Park Vehicle",width=15,height=5,font=("Times New Roman",20,font.BOLD),bg="lawn green",bd=4,relief="ridge",command=displayparking).pack(side=LEFT,padx=10)
    Button(services,text="Search Vehicle",width=15,height=5,font=("Times New Roman",20,font.BOLD),bg="dodger blue",bd=4,relief="ridge",command=searchvehicle).pack(side=LEFT,padx=10)
    Button(services,text="Parking Prices",width=15,height=5,font=("Times New Roman",20,font.BOLD),bg="orange",bd=4,relief="ridge",command=prices).pack(side=LEFT,padx=10)
    Button(services,text="Exit the lot",width=15,height=5,font=("Times New Roman",20,font.BOLD),bg="violet red",bd=4,relief="ridge",command=exitlot).pack(side=LEFT,padx=10)
    services.pack(pady=100)
    home.mainloop()     

def displayparking():#displays a new tkinter window with a form to get details and the parking area to park vehicles
    mess.set("Please fill the form and press Park")
    name.set("")
    vehnum.set("")
    phn.set("")
    r.set("")
    c.set("")
    park=Toplevel(home)
    park.title("Parking Area")
    park.geometry("1300x800")
    park.configure(bg="black")
    head=Frame(park,height="40",width=1300)
    Label(head,text="Welcome To The Online Parking Area",font=("Times New Roman",40,font.BOLD),bg="black",fg="white").pack()
    head.pack()

    details=Frame(park,height=400,width=1300,bd=4,relief="ridge",bg="black")
    details.pack(padx=10,pady=100)

    form=Frame(details,width=400,height=400,bd=4,relief="sunken",bg="seashell3")
    Label(form,text="Enter the details",font=("Times New Roman",20,font.BOLD),bg="seashell3").grid(row=0,column=0,columnspan=2)
    Label(form,text='',bg="seashell3").grid(row=1,column=1)
    Label(form,text="             Your name:",font=("Times New Roman",15,font.BOLD),bg="seashell3").grid(row=2,column=0)
    global nameval
    nameval=Entry(form,textvariable=name,font=("Times New Roman",13,font.BOLD))
    nameval.grid(row=2,column=1)
    Label(form,text="Your phone number:",font=("Times New Roman",15,font.BOLD),bg="seashell3").grid(row=3,column=0)
    global phnval
    phnval=Entry(form,textvariable=phn,font=("Times New Roman",13,font.BOLD))
    phnval.grid(row=3,column=1)
    Label(form,text="Your vehicle number:",font=("Times New Roman",15,font.BOLD),bg="seashell3").grid(row=4,column=0)
    global vehnumval
    vehnumval=Entry(form,textvariable=vehnum,font=("Times New Roman",13,font.BOLD))
    vehnumval.grid(row=4,column=1)
    Label(form,text="    Choose row:",font=("Times New Roman",15,font.BOLD),bg="seashell3").grid(row=5,column=0)
    global rval
    rval=Entry(form,textvariable=r,font=("Times New Roman",13,font.BOLD))
    rval.grid(row=5,column=1)
    Label(form,text="    Choose column:",font=("Times New Roman",15,font.BOLD),bg="seashell3").grid(row=6,column=0)
    global cval
    cval=Entry(form,textvariable=c,font=("Times New Roman",13,font.BOLD))
    cval.grid(row=6,column=1)
    form.pack(padx=20,pady=20,side=LEFT,anchor=NW)
    global vehtypeval
    Label(form,text="Choose vehicle type:",font=("Times New Roman",15,font.BOLD),bg="seashell3").grid(row=7,column=0)
    Radiobutton(form,text="Bike",font=("Times New Roman",13,font.BOLD),variable=vehtype,value="B",bg="seashell3").grid(row=7,column=1)
    Radiobutton(form,text="Car",font=("Times New Roman",13,font.BOLD),variable=vehtype,value="C",bg="seashell3").grid(row=8,column=1)
    Radiobutton(form,text="Truck",font=("Times New Roman",13,font.BOLD),variable=vehtype,value="T",bg="seashell3").grid(row=9,column=1)
    form.pack(padx=10,pady=20,side=LEFT,anchor=NW)

    global messagebox
    messagebox=Frame(details,height=100,width=400,relief="sunken",bd=4,bg="slate blue")
    Label(messagebox,textvariable=mess,font="lucida 12 bold",bg="slate blue",fg="lawn green").pack()
    messagebox.pack(side=LEFT,padx=1,pady=20,anchor=CENTER)

    global parkarea
    parkarea=Frame(details,height=400,width=400,relief="sunken",bd=4)
    Label(parkarea,textvariable=area,font=("Times New Roman",20,font.BOLD),bg="lemon chiffon").pack()
    parkarea.pack(side=RIGHT,padx=10,pady=20,anchor=NW)

    Button(park,text="Park",font=("Times New Roman",13,font.BOLD),height=1,width=30,bg="lawn green",command=updateinfo).pack()
    Button(park,text="Help",font=("Times New Roman",13,font.BOLD),height=1,width=10,bg="dodger blue",command=help).pack(side=RIGHT,padx=10)
    park.grab_set()
def help():
    tm.showinfo("Help","The 'B','C','T' in the parking area represent parked Bikes, Cars, Trucks respectively and these are filled parking spots.You have to choose an empty parking spot which are represented by their respective row and column number.\nHope that helps.")
def updateinfo():#to change the parking area to the one which has the customers vehicle and display it
    if(nameval.get()=='' or phnval.get()=='' or rval.get()=='' or cval.get()=='' or vehnumval.get()==''):
        tm.showerror("Missing Information","Please fill all the information before pressing the key")
        return
    if(int(rval.get())>3 or int(cval.get())>3):
        tm.showerror("Invalid row or column","Please choose a valid row or column from the given parking lot")
        return
    if vehnumval.get() not in database.keys():#customer not already in parking area
        if lot[int(rval.get())][int(cval.get())]==f"[ {int(rval.get())}{int(cval.get())} ]":#customer chose an empty spot
            data=[nameval.get(),phnval.get(),rval.get(),cval.get(),vehnumval.get(),vehtype.get()]
            database[vehnumval.get()]=data
            lot[int(rval.get())][int(cval.get())]=f"[ {vehtype.get()} ]"
            design=displaylot(lot)
            area.set(design)
            parkarea.update()
            print(database)
            # tm.showinfo("Success",f"{nameval.get()} your vehicle was successfully parked at spot [{rval.get()}][{cval.get()}]")
            mess.set(f"{nameval.get()} your vehicle was \nsuccessfully parked at spot [{rval.get()}][{cval.get()}]")
        else:
            # tm.showerror("Oops!","That spot is already filled...Please choose an empty spot")
            mess.set("That spot is already \nfilled...Please choose an \nempty spot")
    else:
        # tm.showerror("Error","Your vehicle is alredy parked in the parking lot...!")
        mess.set("Your vehicle is alredy \nparked in the parking lot...!")
    messagebox.update()
def searchvehicle():
    search=Toplevel(home)
    search.grab_set()
    search.geometry("400x200")
    search.configure(bg="black")
    vehicle=StringVar()
    Label(search,text="Enter your vehicle number:",font=("Times New Roman",15,font.BOLD),bg="black",fg="white").pack(pady=10)
    global vehicleval
    vehicleval=Entry(search,textvariable=vehicle,font=("Times New Roman",15,font.BOLD))
    vehicleval.pack(pady=30)
    Button(search,text="Search",font=("Times New Roman",10,font.BOLD),width=30,bg="lawn green",command=searchresult).pack(pady=10)
def searchresult():#to show if the vehicle is found or not
    if(vehicleval.get()==""):
        tm.showerror("Missing Information","Please fill  the information before pressing the key")
        return
    if vehicleval.get() in database.keys():
        tm.showinfo("Found",f"Hello {database[vehicleval.get()][0]}, Your vehicle {database[vehicleval.get()][4]} is parked at spot [{database[vehicleval.get()][2]}][{database[vehicleval.get()][3]}]")
    else:
        tm.showerror("Not Found","Your vehicle is not parked here or you must have entered wrong information")
def exitlot():
    vehicle=Toplevel(home)
    vehicle.grab_set()
    vehicle.geometry("400x200")
    vehicle.configure(bg="black")
    veh=StringVar()
    Label(vehicle,text="Enter your vehicle number:",font=("Times New Roman",15,font.BOLD),bg="black",fg="white").pack(pady=10)
    global vehicleval
    vehicleval=Entry(vehicle,textvariable=veh,font=("Times New Roman",15,font.BOLD))
    vehicleval.pack(pady=30)
    Button(vehicle,text="Remove",font=("Times New Roman",10,font.BOLD),width=30,bg="lawn green",command=removevehicle).pack(pady=10)
def removevehicle():#again updates the parking lot and removes the customer from the database
    if(vehicleval.get()==""):
        tm.showerror("Missing Information","Please fill  the information before pressing the key")
        return
    if vehicleval.get() in database.keys():
        r=int(database[vehicleval.get()][2])
        c=int(database[vehicleval.get()][3])
        n=database[vehicleval.get()][0]
        database.pop(vehicleval.get())
        lot[r][c]=f"[ {r}{c} ]"
        design=displaylot(lot)
        area.set(design)
        tm.showinfo("Thanks",f"Hey {n} \nYour vehicle was successfully removed...\nThanks for visiting")
    else:
        tm.showerror("Not Found","Your vehicle is not parked here or you must have entered wrong information")
def prices():
    info=Toplevel(home)
    info.grab_set()
    info.geometry("400x200")
    info.configure(bg="black")
    txt="Bike - 20 Rupees per hour\nCar - 30 Rupees per hour\nTruck - 50 Rupees per hour"
    Label(info,text="Price Table",font=("Times New Roman",20,font.BOLD),bg="black",fg="white").pack(side=TOP,pady=20)
    Label(info,text=txt,font=("Times New Roman",12,font.BOLD),bg="black",fg="white",bd=4,relief="ridge").pack(pady=30)
    
if __name__=="__main__":
    home=Tk()
    name=StringVar()
    phn=StringVar()
    vehnum=StringVar()
    vehtype=StringVar()
    r=StringVar()
    c=StringVar()
    area=StringVar()
    mess=StringVar()
    mess.set("Please fill the form and press Park")
    vehtype.set("B")
    rval=cval=""
    with open("record.txt",'r')as f:
        database=ast.literal_eval(f.read())
    with open("lot.txt",'r')as f:
        lot=ast.literal_eval(f.read())
    design=displaylot(lot)
    area.set(design)
    displayhome()
    with open('record.txt','w') as f:
        f.write(str(database))
    with open('lot.txt','w') as f:
        f.write(str(lot))    
