from tkinter import *
from tkinter import ttk
import itertools

def batton_clic():
    field = Text(root, width=25, height=10, wrap=WORD)
    field.grid(column=0, row=5, columnspan=2)
    text = text_input.get()
    data = data_input.get().split()
    char_data = char_data_input.get()
    if char_data == '':
        char_data = str(len(data))
    char = char_input.get()
    combin = itertools.permutations(data, int(char_data))
    if int(char_data) <= len(data):
        for i in combin:
            field.insert(0.0, '\n')
            for j in i:
                field.insert(0.0, f'{j}' + char)
            field.insert(0.0, f'{text} ')
    else:
        field.insert(0.0, 'Количество знаков не должно превышать количество вводимых данных')

root = Tk()
root.title('ДанИИл')
root.geometry('300x400')

lbl_text = Label(root, text='Текст')
lbl_text.grid(column=0, row=0)
lbl_text = Label(root, text='Данные через пробел')
lbl_text.grid(column=0, row=1)
lbl_text = Label(root, text='Количество знаков')
lbl_text.grid(column=0, row=2)
lbl_text = Label(root, text='Знак разделитель')
lbl_text.grid(column=0, row=3)

text_input = ttk.Entry(root, width=20)
text_input.grid(column=1, row=0)
data_input = ttk.Entry(root, width=20)
data_input.grid(column=1, row=1)
char_data_input = ttk.Entry(root, width=20)
char_data_input.grid(column=1, row=2)
char_input = ttk.Entry(root, width=20)
char_input.grid(column=1, row=3)

btn = ttk.Button(root, text='OK', command=batton_clic)
btn.grid(column=0, row=4, columnspan=2, ipadx=70, ipady=3, padx=5, pady=5)

root.mainloop()