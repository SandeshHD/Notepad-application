from tkinter import *
from tkinter import filedialog, colorchooser, messagebox, simpledialog
import wikipedia
import tkinter.font


fileloc = ['no_file']
root = Tk()
root.title("Notepad")


def search(*args):
    s = simpledialog.askstring('Search', 'Enter your search')
    root.title("Notepad - " + str(s))
    txt.delete(1.0, END)
    if s is None:
        return
    try:
        k = wikipedia.summary(s)
        txt.insert(INSERT, k)
    except:
        messagebox.showerror("Error","Check your internet connection or Enter proper word")


def new(*args):
    txt.delete(1.0, END)
    root.title("Notepad")
    fileloc[0] = 'no_file'


def strt(*args):
    txt.delete(1.0, END)
    res = filedialog.askopenfile(initialdir='/', title='select',
                                 filetypes=(('text files', '.txt'), ('all files', '.')))
    root.title("Notepad - " + str(res.name))
    if res is None:
        return
    fileloc[0] = res.name
    for c in res:
        txt.insert(INSERT, c)


def exit():
    ans = messagebox.askquestion('Exit', 'Do you really want to exit')
    if ans == 'yes':
        root.destroy()


def saveas():
    sv = filedialog.asksaveasfile(mode='w', defaultextension='.txt', initialdir='/',
                                  filetypes=(('text files', '.txt'), ('all files', '.')))
    root.title("Notepad - " + str(sv.name))
    if sv is None:
        return
    sv.write(txt.get(1.0, END))
    fileloc[0] = sv.name
    sv.close()
    messagebox.showinfo('Info', 'File saved successfully.')


def save(*args):
    if fileloc[0] == 'no_file':
        saveas()
    else:
        f = open(fileloc[0], 'w+')
        f.write(txt.get(1.0, END))
        f.close()


def changeBg(*args):
    clr = colorchooser.askcolor(title='select color')
    txt.config(bg=clr[1])


def changeFont(*args):
    clr = colorchooser.askcolor(title='select color')
    txt.config(fg=clr[1])


def cpy(event=''):
    try:
        txt.clipboard_clear()
        txt.clipboard_append(txt.selection_get())
    except:
        pass


def paste(event=''):
    txt.insert(INSERT, txt.clipboard_get())


def cut(event=''):
    try:
        cpy()
        txt.delete('sel.first', 'sel.last')
    except:
        pass


def changeFntFam(font):
    Desired_font = tkinter.font.Font(family=font)
    print(font)
    print("txt===",txt)
    txt.config(font=Desired_font)

tframe = Frame(root)
tframe.pack()

scroll = Scrollbar(tframe)
scroll.pack(fill=Y, side=RIGHT)

txt = Text(tframe,yscrollcommand=scroll, padx=2, pady=2, wrap=WORD, undo=True)
txt.pack(fill=BOTH, expand=True)
scroll.config(command=txt.yview)

mainm = Menu(root)
root.config(menu=mainm)

file = Menu(mainm, tearoff=False)
mainm.add_cascade(label='File', menu=file)

file_menu_labels = ["New", "Open", "Save", "Save as", "Exit"]
file_menu_commands = [new, strt, save, saveas, exit]

for item in zip(file_menu_labels, file_menu_commands):
    file.add_command(label=item[0], command=item[1])

edit_menu = Menu(mainm, tearoff=False)
mainm.add_cascade(label='Edit', menu=edit_menu)

edit_menu_labels = ["Copy", "Cut", "Paste", "Undo", "Redo"]
edit_menu_functions = [cpy, cut, paste, txt.edit_undo, txt.edit_redo]

for item in zip(edit_menu_labels, edit_menu_functions):
    edit_menu.add_command(label=item[0], command=item[1])

fontFam = Menu(mainm, tearoff=False)
mainm.add_cascade(label='Font Family', menu=fontFam)

font_labels = ["Adobe Garamond Pro",
               "Comic Sans MS",
               "Consolas",
               "Courier",
               "Courier New",
               "Courier New Greek",
               "Microsoft Himalaya",
               "Modern",
               "MS Sans Serif",
               "Roman",
               "System",
               "Terminal",
               "Times New Roman"
]

for font in font_labels:
    fontFam.add_command(label=font, command=lambda font=font: changeFntFam(font))

format_menu = Menu(mainm, tearoff=False)
mainm.add_cascade(label='Format', menu=format_menu)
format_menu.add_command(label='Change Background', command=changeBg)
format_menu.add_command(label='Change Font', command=changeFont)

root.bind('<Control-c>', cpy)
root.bind('<Control-v>', paste)
root.bind('<Control-x>', cut)
root.bind('<Control-s>', save)
root.bind('<Control-o>', strt)
root.bind('<Control-n>', new)

#added 3 shortcuts
root.bind('<Control-w>', search)
root.bind('<Control-b>', changeBg)
root.bind('<Control-f>', changeFont)

#changed font family
Desired_font = tkinter.font.Font( family = "Comic Sans MS", size = 12
                                  )
txt.configure(font= Desired_font)
root.mainloop()
