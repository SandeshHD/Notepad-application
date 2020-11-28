from tkinter import *
from tkinter import filedialog
import wikipedia
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import simpledialog

fileloc = ['no_file']
root = Tk()
root.title("Notepad")


def srch():
    s = simpledialog.askstring('Search', 'Enter your search')
    root.title("Notepad - " + str(s))
    txt.delete(1.0, END)
    if s is None:
        return
    try:
        k = wikipedia.summary(s)
        txt.insert(INSERT, k)
    except:
        txt.insert(INSERT, 'Check your internet connection or Enter proper word')


def new(*args):
    txt.delete(1.0, END)
    root.title("Notepad")
    fileloc[0] = 'no_file'


def strt(*args):
    txt.delete(1.0, END)
    res = filedialog.askopenfile(initialdir='/', title='select',
                                 filetypes=(('text files', '.txt'), ('all files', '*.*')))
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
                                  filetypes=(('text files', '.txt'), ('all files', '*.*')))
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


def changebg():
    clr = colorchooser.askcolor(title='select color')
    txt.config(bg=clr[1])


def changefnt():
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


mainm = Menu(root)
root.config(menu=mainm)
file = Menu(mainm, tearoff=False)
mainm.add_cascade(label='File', menu=file)
file.add_command(label="New", command=new)
file.add_command(label="Open", command=strt)
file.add_command(label="Save", command=save)
file.add_command(label="Save as", command=saveas)
file.add_command(label="Exit", command=exit)
edit_menu = Menu(mainm, tearoff=False)
mainm.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Copy", command=cpy)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)
mainm.add_command(label='Search', command=srch)
tframe = Frame(root)
scroll = Scrollbar(tframe)
scroll.pack(fill=Y, side=RIGHT)
txt = Text(tframe, yscrollcommand=scroll, padx=2, pady=2, wrap=WORD, undo=True)
edit_menu.add_command(label="Undo", command=txt.edit_undo)
edit_menu.add_command(label="Redo", command=txt.edit_redo)
scroll.config(command=txt.yview)
txt.pack(fill=BOTH, expand=1)
tframe.pack()
format_menu = Menu(mainm, tearoff=False)
mainm.add_cascade(label='Format', menu=format_menu)
format_menu.add_command(label='Change Background', command=changebg)
format_menu.add_command(label='Change Font', command=changefnt)
root.bind('<Control-c>', cpy)
root.bind('<Control-v>', paste)
root.bind('<Control-x>', cut)
root.bind('<Control-s>', save)
root.bind('<Control-o>', strt)
root.bind('<Control-n>', new)
root.mainloop()
