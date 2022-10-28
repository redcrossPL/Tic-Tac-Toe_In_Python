import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Kółko i Krzyżyk')
root.resizable(False, False)
root.iconbitmap('krzyz.ico')

licz = True
ruch = 0
c = 0


def wylaczprzyciski():
    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)
    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)
    b6.config(state=tk.DISABLED)
    b7.config(state=tk.DISABLED)
    b8.config(state=tk.DISABLED)
    b9.config(state=tk.DISABLED)


def sprawdzWygrana():
    global c
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b7['text'] == 'X' and b5['text'] == 'X' and b3['text'] == 'X':
        b7.config(bg='red')
        b5.config(bg='red')
        b3.config(bg='red')
        messagebox.showerror('Gracz X Wygrał', 'Gracz X Wygrał!!!')
        wylaczprzyciski()
        c += 1

    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1
    elif b7['text'] == 'O' and b5['text'] == 'O' and b3['text'] == 'O':
        b7.config(bg='red')
        b5.config(bg='red')
        b3.config(bg='red')
        messagebox.showerror('Gracz O Wygrał', 'Gracz O Wygrał!!!')
        wylaczprzyciski()
        c += 1


def b_klik(b):
    global licz
    global c
    global ruch
    if b['text'] == ' ' and licz == True:
        licz = False
        ruch += 1
        b['text'] = 'X'
        tk.Label(root, text='Ruch Gracza: O    ').grid(column=0, row=3)
        sprawdzWygrana()
        if ruch == 9 and c != 1:
            b1.config(bg='red')
            b2.config(bg='red')
            b3.config(bg='red')
            b4.config(bg='red')
            b5.config(bg='red')
            b6.config(bg='red')
            b7.config(bg='red')
            b8.config(bg='red')
            b9.config(bg='red')
            messagebox.showerror('REMIS', 'REMIS!!!')
            wylaczprzyciski()
    elif b['text'] == ' ' and licz == False:
        licz = True
        ruch += 1
        b['text'] = 'O'
        tk.Label(root, text='Ruch Gracza: X    ').grid(column=0, row=3)
        sprawdzWygrana()
        if ruch == 9 and c == 0:
            b1.config(bg='red')
            b2.config(bg='red')
            b3.config(bg='red')
            b4.config(bg='red')
            b5.config(bg='red')
            b6.config(bg='red')
            b7.config(bg='red')
            b8.config(bg='red')
            b9.config(bg='red')
            messagebox.showerror('REMIS', 'REMIS!!!')
            wylaczprzyciski()
    elif ruch == 9 and c == 0:
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        messagebox.showerror('REMIS', 'REMIS!!!')
        wylaczprzyciski()
    else:
        messagebox.showerror('Kółko i Krzyżyk', 'Dane Pole Zostało Już Wybrane. Wybierz Inne!!!')
    c = 0


def reset():
    global root
    root.destroy()


def rest():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, ruch, c
    b1 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b1, ))
    b2 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b2, ))
    b3 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b3, ))

    b4 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b4, ))
    b5 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b5, ))
    b6 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b6, ))

    b7 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b7, ))
    b8 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b8, ))
    b9 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace',
                   command=lambda: b_klik(b9, ))

    b1.grid(column=0, row=0)
    b2.grid(column=0, row=1)
    b3.grid(column=0, row=2)

    b4.grid(column=1, row=0)
    b5.grid(column=1, row=1)
    b6.grid(column=1, row=2)

    b7.grid(column=2, row=0)
    b8.grid(column=2, row=1)
    b9.grid(column=2, row=2)
    ruch = 0
    c = 0


meniu = tk.Menu(root)
root.config(menu=meniu)
opcje_meniu = tk.Menu(meniu, tearoff=False)
meniu.add_cascade(label='Opcje', menu=opcje_meniu)
opcje_meniu.add_command(label='Resetuj', command=rest)
opcje_meniu.add_command(label='Wyjdź', command=reset)

rest()
root.mainloop()
