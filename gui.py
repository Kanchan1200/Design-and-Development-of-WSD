from tkinter import *
from tkinter import messagebox
from util.modelling import getSense




def show_window():
    root= Tk()
    root.geometry('1000x626+100+100')
    root.title('Correct sense')
    #root.resizable(0,0)
    bgimage=PhotoImage(file='bg.png')
    bgLabel=Label(root,image=bgimage)
    bgLabel.place(x=0,y=0)

    #FOR OUTPUT
    correctlabel=Label(root,text='Correct Sense:',font=('castellar',15,'bold'),fg='#4d1537', bg='whitesmoke')
    correctlabel.place(x=510,y=205)
    label_meaning=Label(root, text='', wrap=True, wraplength=200, justify='left',font=('castellar',12,'bold'),fg='#4d1537', bg='whitesmoke')
    label_meaning.place(x=510, y=260)

    exitButton = Button(root,text='exit') #image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                        #command=search)
    exitButton.place(x=650, y=435)

    # For INPUT
    enterwordlabel=Label(root,text='Enter The Sentence:',font=('castellar',15,'bold'),fg='#4d1537', bg='whitesmoke')
    enterwordlabel.place(x=520,y=20)

    enterwordentry = Entry(root, font=('arial', 20, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
    enterwordentry.place(x=510, y=60)
    enterwordentry.focus_set()

    #searchimage = PhotoImage(file='search.png')

    def clear():
        enterwordentry.delete(0, END)
        label_meaning.config(text='')
    # Clear button
    clearButton = Button(root,text='clear', command=clear) #image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                        #command=search)
    clearButton.place(x=610, y=130) 
    
    def make_prediction():
        label_meaning.config(text='')
        # input data
        ip_data = enterwordentry.get() 
        if ip_data != '':
            meaning = getSense(ip_data)
            label_meaning.config(text=meaning)

        else:
            messagebox.warning("Please Type some Text into the Sentence Field!")

        
    predictButton = Button(root,text='Predict', command=make_prediction) #image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                        #command=search)
    predictButton.place(x=690, y=130)



    
    root.mainloop()

