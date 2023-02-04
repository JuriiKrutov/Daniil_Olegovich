from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import itertools

def batton_clic():
    field = Text(root, width=25, height=10, wrap=WORD)
    field.grid(column=0, row=4)
    text = text_input.get()
    data = data_input.get().split()
    combin = itertools.permutations(data)
    for i in combin:
        field.insert(0.0, '\n')
        for j in i:
            field.insert(0.0, f'{j}')
        field.insert(0.0, f'{text} ')

root = Tk()
root.title('Специально для ДанИИла')
root.geometry('600x400')

lbl_text = Label(root, text='Текст')
lbl_text.grid(column=0, row=0)
lbl_text = Label(root, text='Данные через пробел')
lbl_text.grid(column=0, row=1)

text_input = Entry(root, width=10)
text_input.grid(column=1, row=0)
data_input = Entry(root, width=10)
data_input.grid(column=1, row=1)

btn = Button(root, text='OK', command=batton_clic)
btn.grid(column=1, row=2)

root.mainloop()