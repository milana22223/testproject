from tkinter import*
from tkinter import messagebox


def set_value(formula):
    if formula=='':
        lbl['text']='0'
    else:
        try:
            lbl['text'] = str(eval(formula))
        except ZeroDivisionError:
            messagebox.showerror('Ошибка', 'Деление на 0')
            lbl['text'] = '0'

def logicalc(operation):
    if operation =='C':
        set_value('')
    elif operation =='DEL':
         lbl['text'] = lbl['text'][0:-1]
    elif operation == 'x^2':
        set_value(str((eval(lbl['text']))**2))
    elif operation == '=':
        set_value(lbl['text'])
    else:
        if lbl['text'] == '0':
            lbl['text']= ''
        lbl['text']= lbl['text']+operation

root=Tk()
root['bg']='black'
root.geometry('485x550+200+200')
root.title('Калькулятор')
root.resizable(False,False)
lbl= Label(text='0', font=('Consolas', 21 ,'bold'), bg='black', fg='white')
lbl.place(x=11, y=50)

btns=[
    'C', 'DEL', '*', "=",
    "1", '2', '3', '/',
    '4', '5', '6', '+',
    '7', '8', '9', '-',
    '(','0', ')', 'x^2'
]

x=10
y=140
for bt in btns:
    com = lambda x=bt: logicalc(x)
    Button(text=bt, bg='white', font=('consolas', 15), command=com).place(x=x, y=y, width=115, height=79)
    x+=117
    if x>400:
        x=10
        y+=81

root.mainloop()

