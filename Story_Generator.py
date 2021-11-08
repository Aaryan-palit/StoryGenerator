from tkinter import *
from PIL import ImageTk, Image
import random
import time
import os
from faker import Faker
fake = Faker()
import mysql.connector
root = Tk()
root.title('Story Generator')
root.iconbitmap("C:\\Users\\Aaryan\\Downloads\\StoryIcon1.ico")
root.geometry("800x550")
img=PhotoImage(file="C:\\Users\\Aaryan\\Downloads\\bgBook.png")
#Create canvas
my_canvas=Canvas(root,width= 800, height= 500)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=img, anchor="nw")

mydb= mysql.connector.connect(host= "localhost", user="root", passwd= "7blaze@221B",database="story")

#create cursor
cur=mydb.cursor()
# create database
# cur.execute("CREATE DATABASE story")

#create table
cur.execute("CREATE TABLE IF NOT EXISTS StoryTable (name VARCHAR(255), place VARCHAR(255), time VARCHAR(255), work VARCHAR(255), happend VARCHAR(255), user_id INT AUTO_INCREMENT PRIMARY KEY)")
#Insert table  
sql_cmd=("INSERT INTO StoryTable(name, place, time, work, happend) VALUES(%s, %s, %s, %s, %s)")
hlist=[" found a treasure", " lost 1 million", " got promotion", " won a loterry of 2 million", " got a pet", " got fired from job"," gone bankrupt due to gambling"," found peace in life"]
for _ in range(50):
    n=fake.name()
    p=fake.country()
    t=fake.century()
    w=fake.job()
    h=random.choice(hlist)
    value= (n,p,t,w,h)
    cur.execute(sql_cmd, value)
mydb.commit()

#Show table
# cur.execute("SELECT * FROM StoryTable")
# result=cur.fetchall()
# for x in result:
# 	print(x)

def myClick():
    happlist=[" found a treasure", " lost 1 million", " got promotion", " won a loterry of 2 million", " got a pet", " got fired from job"," gone bankrupt due to gambling"," found peace in life"]
    Starter = ['Long ago', 'At some point', 'Once upon a time', 'In times gone by', 'Once']
    resLabel=Label(top, text=str(random.choice(Starter)+
                    " there was a person named "+nameBox.get()+
                    " who lived in "+placeBox.get()+
                    " during "+timeBox.get()+
                    " century,who was a "+workBox.get()+
                    " by profession. On a certain day their whole family "+random.choice(happlist)),bg="orange",
                     font=("Times",14), wraplength=300, justify="center").grid(row=10,column=6,columnspan=2)

# Update function to update each frames in gif
def update(ind):
    global frames
    global frame
    global label
    global frameCnt
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    top.after(100, update, ind)
#GIF function
def Gif():
    global frames
    global frame
    global label
    global frameCnt
    global ind
    frameCnt = 18
    frames = [PhotoImage(file='C:\\Users\\Aaryan\\Downloads\\cat.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    label = Label(top)
    label.grid(row=1,column=7)
    top.after(0, update, 0)
    top.mainloop()

#Generate Your Story
def Generate():
    global top
    global nameBox
    global placeBox
    global timeBox
    global workBox
    global frames
    global frame
    global label
    global frameCnt
    global ind
    top=Toplevel()
    top.title("Generate Own Story")
    top.iconbitmap("C:\\Users\\Aaryan\\Downloads\\StoryIcon1.ico")
    top.geometry("800x550")
    top.configure(bg="orange")
    lab1=Label(top, text="Generator Your Own Story\n",
                   font=("Comic Sans MS",17,"bold"),bg="orange", wraplength=300, justify="center")
    lab1.grid(row=0,column=6,pady=15)
    nameL=Label(top, text="Enter a Name:",font=("Helvetica",10,'bold'),bg="orange").grid(sticky=W, padx=10,pady=10, row=1,column=0)
    placeL=Label(top, text="Enter a Place:",font=("Helvetica",10,'bold'),bg="orange").grid(sticky=W, padx=10,pady=10,row=2,column=0)
    timeL=Label(top, text="Enter a Time:",font=("Helvetica",10,'bold'),bg="orange").grid(sticky=W, padx=10,pady=10,row=3,column=0)
    workL=Label(top, text="Enter a Job:",font=("Helvetica",10,'bold'),bg="orange").grid(sticky=W, padx=10,pady=10,row=4,column=0)
    nameBox=Entry(top)
    nameBox.grid(row=1,column=1, padx=10,pady=10)
    placeBox=Entry(top)
    placeBox.grid(row=2,column=1, padx=10,pady=10)
    timeBox=Entry(top)
    timeBox.grid(row=3,column=1, padx=10,pady=10)
    workBox=Entry(top)
    workBox.grid(row=4,column=1, padx=10,pady=10)
    btn2= Button(top,text="Show Story",font=("Helvetica",10,'bold'), command=lambda:[myClick(),Gif()]).grid(row=5,column=0,columnspan=2, padx=10, pady=10)
    

#Function to Generate Ramdom Story
def Open():
    global frames
    global frame
    global label
    global frameCnt
    tp=Toplevel()
    tp.title("Random Story")
    tp.iconbitmap("C:\\Users\\Aaryan\\Downloads\\StoryIcon1.ico")
    tp.geometry("800x550")
    tp.configure(bg="orange")  
    cur=mydb.cursor()
    frame1=Frame(tp,bg="orange",width=600,height=600)
    frame1.pack(padx=10,pady=20,ipadx=90,ipady=90)
    labHead=Label(frame1, text="Your Random Story:\n",
                   font=("Comic Sans MS",17,"bold"),bg="orange", wraplength=300, justify="center")
    labHead.pack(pady=10)
    StoryStart = ['Long ago', 'At some point', 'Once upon a time', 'In times gone by', 'Once']
    cur.execute('SELECT * FROM StoryTable WHERE user_id=ROUND((RAND()*199)+1)')
    records=cur.fetchall()
    for rows in records:
        label_=Label(frame1, text=str(random.choice(StoryStart)+
                    " there was a person named "+rows[0]+
                    " who lived in "+rows[1]+
                    " during "+rows[2]+
                    " century,who was a "+rows[3]+
                    " by profession. On a certain day their whole family "+rows[4]),
                    bg='orange', font=("Times",14), wraplength=300, justify="center")
        label_.config(anchor=CENTER)
        label_.pack(padx=10, pady=10)
    btn2= Button(frame1,text="END",font=("Helvetica",10,'bold'), command=tp.destroy).pack(padx=10, pady=10)
    p= PhotoImage(file = "C:\\Users\\Aaryan\\Downloads\\DoneImg.png")
    pLabel= Label(frame1,image= p).pack()
    tp.mainloop()

    mydb.close()

my_canvas.create_text(400,80, text="Welcome to Story Generator\n\n", 
                     font=("Comic Sans MS",17,"bold"),fill="white", justify="center")

my_canvas.create_text(400,180, text="Want to Generate a Random Story!\n\n Click the button",
         font=("Times",13,"bold"),fill="#ffffff", justify="center")
my_canvas.create_text(400,300, text="To Generate Your Own Story!\nClick the button",
         font=("Times",13,"bold"),fill="#343a3a", justify="center")
#Define buttons
btn1= Button(root,text= "Random Story!",font=("Times",11), command=Open, borderwidth=4)
btn1_window=my_canvas.create_window(400,230, window=btn1)
btn2= Button(root,text= "Create Story!",font=("Times",11), command=Generate, borderwidth=4)
btn2_window=my_canvas.create_window(400,350, window=btn2)
root.mainloop()
