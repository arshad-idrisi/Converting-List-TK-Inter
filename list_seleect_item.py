from tkinter import *


def insert_item():
    list1.insert(END, txtName.get())
    txtName.delete(0, END)


def print_item():
    for i in list2.curselection():
        print(list2.get(i))


def moveto(fromlist, tolist):
    for i in fromlist.curselection():
        indexlist = fromlist.curselection()

        if indexlist:
            index = indexlist[0]
            val = fromlist.get(index)
            fromlist.delete(index)
            tolist.insert(END, val)
        i = i+1


root = Tk()
root.geometry("500x500")
root.title("Listbox!!")

s = Scrollbar(root, jump=True, orient=VERTICAL)
s1 = Scrollbar(root, jump=True, orient=VERTICAL)

bottom = Label(root, text="✨✨...Star Code with Arshad...👑👑", bg="aqua", fg="red", font="comicsansms, 15 bold", bd="4", relief="raised")
bottom.pack()

list1 = Listbox(root, width=25, height=10, fg="red", font=("Agency fb", 20),
                selectmode='multiple', background="light grey", bd=10, yscrollcommand=s.set)
list1.insert(1, "Data Structure")
list1.insert(2, "Dta Science")

list2 = Listbox(root, width=25, height=10, fg="red", font=("Agency fb", 20),
                selectmode='multiple', background="light grey", bd=10, yscrollcommand=s.set)

list2.insert(1, "Python")
list2.insert(2, "Java")

txtName = Entry(bd=5, fg="blue", font="arial 10 bold")

insert_btn = Button(root, text="INSERT", fg="green", bd=5, command=insert_item)
print_btn = Button(root, text="PRINT BUTTON", fg="green", bd=5, command=print_item)

right_btn = Button(root, text="---->", fg="red", bd=5, background="grey", command=lambda :moveto(list1, list2))
left_btn = Button(root, text="<----", fg="red", bd=5, background="grey", command=lambda :moveto(list2, list1))

list1.place(x=120, y=50)
list2.place(x=925, y=50)
txtName.place(x=180, y=430)
insert_btn.place(x=220, y=480)
print_btn.place(x=1030, y=420)
right_btn.place(x=650, y=100)
left_btn.place(x=650, y=150)


s.config(command=list1.yview)
s1.config(command=list2.yview)
s.pack(side=RIGHT, fill=Y)
s1.pack(side=RIGHT, fill=Y)

root.mainloop()
