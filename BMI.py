


import matplotlib.pyplot as plt
from datetime import datetime
import time
from tkinter import *






root=Tk()
root.geometry("1550x650+0+0")
root.resizable(0,0)
root.title("BMI")






BMI=0
def BMI_Cal():
    global BMI
    Bhieght=float(var2.get())
    Bweight=float(var1.get())
    if Bhieght !=0 or Bweight!=0:
        Age=float(var3.get())
        BMI=str("%.2f" %(Bweight/(Bhieght**2)))
        lblBMIResult.config(text=BMI)
        f=open("bmi.txt","a+")
        s=str(BMI)+","+str(Age)
        f.write(s)
        f.write("\n")
    else:
        lblBMIResult.config(text="Enter Valid Data")


def plot():
    f=open("bmi.txt","r")
    r=f.read()
    t=r.split("\n")
    print(t)
    bmi=[]
    age=[]
    z=0
    for i in t:
        z=z+1
        if z==len(t):
            break
        o=i.split(",")
        print(o)
        bmi.append(o[0])
        age.append(o[1])
    lenb=len(bmi)
    lena=len(age)   
    groupb=[]
    for i in bmi:
        groupb.append(i)
    groupa=[]
    for j in age:
        groupa.append(j)
    
    
    plt.bar(groupb,groupa,color="blue")
    plt.xlabel("BMI_Val-->")
    plt.ylabel("Age_Val-->")
    plt.title("BMI x AGE")
    plt.show()     





var1=DoubleVar()
var2=DoubleVar()
var3=DoubleVar()
date1=StringVar()
time1=StringVar()
date1.set(time.strftime("%d/%m/%y"))
time1.set(time.strftime("%H:%M"))






Tops=Frame(root,width=1350,height=50,bd=8,relief="raise")
Tops.pack(side=TOP)
f2=Frame(root,width=200,height=700,bd=8,relief="raise")
f2.pack(side=RIGHT)
f1a=Frame(root,width=600,height=200,bd=20,relief="raise")
f1a.pack(side=TOP)
f1b=Frame(root,width=600,height=600,bd=20,relief="raise")
f1b.pack(side=TOP)
f1c=Frame(root,width=600,height=600,bd=20,relief="raise")
f1c.pack(side=TOP)





lblTitle=Label(Tops,textvariable=date1,font=("cambria",32,"bold"),
                  pady=15,padx=50,bd=15,bg="sky blue",fg="#000000").grid(row=0,column=0)
lblTitle=Label(Tops,text="\tBODY MASS INDEX\t\t",font=("cambria",32,"bold"),
                  pady=15,padx=50,bd=15,bg="sky blue",fg="#000000").grid(row=0,column=1)
lblTitle=Label(Tops,textvariable=time1,font=("cambria",32,"bold"),
                  pady=15,padx=50,bd=15,bg="sky blue",fg="#000000").grid(row=0,column=2)




lblheight=Label(f1a,text="Select Age ",font=("arial",20,"bold"),bd=20).grid(row=0,column=0)
Age= Scale(f1a,variable=var3,from_=1,to=100,length=880,tickinterval=10,orient=HORIZONTAL)
Age.grid(row=1,column=0)

lblheight=Label(f1b,text="Enter height in metre",font=("arial",20,"bold"),bd=20).grid(row=0,column=0)
txtheight=Entry(f1b, textvariable=var2, font=("arial",16,'bold'),bd=16,width=34,justify='center')
txtheight.grid(row=1,column=0)

lblheight=Label(f1b,text="Enter weight in kilograms",font=("arial",20,"bold"),bd=20).grid(row=0,column=1)
Bodyweight=Entry(f1b, textvariable=var1, font=("arial",16,'bold'),bd=16,width=34,justify='center')
Bodyweight.grid(row=1,column=1)




lblBMIResult=Label(f1c,padx=16,pady=16,bd=16,
                   fg="#000000",font=("arial",30,"bold"),
                   bg="sky blue",relief="sunk",width=35,height=1)



lblBMIResult.grid(row=2,column=0)




lblBMITable=Label(f2,font=("arial",22,"bold"),text="BMI Table").grid(row=0,column=1)
txtlblBMITable=Text(f2,height=15,width=55,bd=16,font=("arial",12,"bold"))
txtlblBMITable.grid(row=1,column=0, columnspan=3)




txtlblBMITable.insert(END,"Meaning \t\t"+"BMI\n\n")
txtlblBMITable.insert(END,"Normal weight\t\t"+"19-24,9\n\n")
txtlblBMITable.insert(END,"Overweight \t\t"+"25-29,9\n\n")
txtlblBMITable.insert(END,"Obesity level I \t\t"+"30-34,9\n\n")
txtlblBMITable.insert(END,"Obesity level II \t\t"+"35-39,9\n\n")
txtlblBMITable.insert(END,"Obesity level III \t\t"+">=40\n\n")

def ext():
    root.destroy()

btnBMI1= Button(f2, text="Click to \n Check your \n BMI",padx=8,pady=8,bd=12,width=9,
                              font=('arial',20,'bold'),height=2,
                              justify="center",
                              command=BMI_Cal)


btnBMI2= Button(f2, text="Click to\nView Graph",padx=8,pady=8,bd=12,width=9,
                              font=('arial',20,'bold'),height=2,
                              justify="center",
                              command=plot)


btnBMI3= Button(f2, text="Click to\nExit",padx=8,pady=8,bd=12,width=9,
                              font=('arial',20,'bold'),height=2,justify="center",command=ext)






btnBMI1.grid(row=2 ,column=0)
btnBMI2.grid(row=2 ,column=1)
btnBMI3.grid(row=2,column=2)
root.mainloop()

                                                      






































