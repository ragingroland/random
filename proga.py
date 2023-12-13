from tkinter import *
from winsound import *
import webbrowser

def perehod():
    webbrowser.open('https://ru.wikipedia.org/wiki/Интернет-мошенничество', 1)

def udalenie():
    window2 = Tk()
    window2.resizable(width = False, height = False)
    window2.title('ДЕНЬГИ')
    window2.geometry('1500x100')
    window2['bg'] = 'black'
    moneycycl = Label(window2, text = 'ви стали жертвою дистанційного шахрайства, всі ваші гроші були переведені на безпечний рахунок', font = ('Comic Sans', 24), fg = 'red', bg = 'black')
    moneycycl.place(x = 10, y = 10)
    moneycycl2 = Label(window2, text = 'більше інформації тут', font = ('Comic Sans', 24), fg = 'red', bg = 'black')
    moneycycl2.place(x = 10, y = 50)
    moneycycl3 = Button(window2, text = 'https://ru.wikipedia.org/wiki/Интернет-мошенничество', command = perehod, font = ('Comic Sans', 24), fg = 'red', bg = 'black')
    moneycycl3.place(x = 350, y = 50)
    PlaySound("nihya.wav", SND_FILENAME)
    window2.mainloop()
    

def moan():
    return PlaySound("moan1.wav", SND_FILENAME)

window = Tk()
window.resizable(width = False, height = False)
window.title('КрИтИнИчЕсКаЯ АШШШШИПКА')
window.geometry('420x280')
window['bg'] = 'red'
idea = Label(window, text = 'Удалить Оперативную Систему Windos штоб розбоготет?',fg = 'white', bg = 'red')
idea.place(x = 50, y = 70)
btn = Button(window, text = 'Ну разумеется', command = udalenie, width = 40, height = 2,fg = 'white', bg = 'grey')
btn.place(x = 70, y = 100)
img = PhotoImage(file="1690677.jpg")
button = Button(window, image=img, command = moan)
button.pack()
button.place(x = 160, y = 150)
window.mainloop()