from tkinter import *
import back_bookstore as back

window=Tk()
window.wm_title("Biblio")

# Initialize database if it doesn't exist
back.init_table()

# Functions
def get_selected_row(event):
    global selected_tuple
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass



def view_command():
    list1.delete(0,END)
    for row in back.print_data():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for r in back.search(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()):
        list1.insert(END,r)

def add_command():
    back.insert_data(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())
    list1.delete(0,END)
    list1.insert(END,(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()))

def delete_command():
    back.delete_data(selected_tuple[0])
    list1.delete(0,END)
    for row in back.print_data():
        list1.insert(END,row)

def update_command():
    back.update_data(selected_tuple[0],e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())
    list1.delete(0,END)
    for row in back.print_data():
        list1.insert(END,row)


# Labels
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

# Entries
e1_title = StringVar()
e1 = Entry(window,textvariable=e1_title)
e1.grid(row=0,column=1)

e2_author = StringVar()
e2 = Entry(window,textvariable=e2_author)
e2.grid(row=0,column=3)

e3_year = StringVar()
e3 = Entry(window,textvariable=e3_year)
e3.grid(row=1,column=1)

e4_isbn = StringVar()
e4 = Entry(window,textvariable=e4_isbn)
e4.grid(row=1,column=3)

# List box, scroll KeyboardInterrupt and bind method
## listbox
list1 = Listbox(window,heigh=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

## Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=3,column=2)

## configure both
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

## bind method (return a list object when you select it with the mouse)
list1.bind('<<ListboxSelect>>',get_selected_row)


# Bottons
b_view_all = Button(window,text="View All",width=12,command=view_command)
b_view_all.grid(row=2,column=3)

b_search = Button(window,text="Search",width=12,command=search_command)
b_search.grid(row=3,column=3)

b_add = Button(window,text="Add",width=12,command=add_command)
b_add.grid(row=4,column=3)

b_update = Button(window,text="Update",width=12,command=update_command)
b_update.grid(row=5,column=3)

b_delete = Button(window,text="Delete",width=12,command=delete_command)
b_delete.grid(row=6,column=3)

b_close = Button(window,text="Close",width=12,command=window.destroy)
b_close.grid(row=7,column=3)

# t1 = Text(window,height=1,width=20)
# t1.grid(row=0,column=2)


window.mainloop()
