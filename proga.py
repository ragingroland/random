from tkinter import * #импортируются нужные библиотеки
from winsound import *
import webbrowser

def funk2(): #функция которая осуществляет переход по ссылке при нажатии кнопки btnwin2
    webbrowser.open('ссылка', 1)

def funk1(): #функция которая открывает window2 при нажатии на кнопку btn
    window2 = Tk() #создается окно window2 и его параметры
    window2.resizable(width = False, height = False)
    window2.title('название окна')
    window2.geometry('100x100')
    window2['bg'] = 'black'
    tekst1 = Label(window2, text = 'текст', font = ('Comic Sans', 24), fg = 'red', bg = 'black') #текст в window2, расположение и шрифт для примера
    tekst1.place(x = 10, y = 10)
    tekst2 = Label(window2, text = 'текст', font = ('Comic Sans', 24), fg = 'red', bg = 'black') #текст2 в window2, расположение и шрифт для примера
    tekst2.place(x = 10, y = 50)
    btnwin2 = Button(window2, text = 'ссылка или текст', command = funk2, font = ('Comic Sans', 24), fg = 'red', bg = 'black') #кнопка для перехода по ссылке в новом окне, расположение и шрифт для примера
    btnwin2.place(x = 350, y = 50)
    PlaySound("имя аудиофайла в формате WAV", SND_FILENAME) #при нажатии на btn проиграется этот аудиофайл
    window2.mainloop()
    

def funkwin1(): #этот аудиофайл проиграется при нажатии кнопки button в window
    return PlaySound("имя аудиофайла в формате WAV", SND_FILENAME)

window = Tk() #создается окно window и его параметры
window.resizable(width = False, height = False)
window.title('текст')
window.geometry('420x280')
window['bg'] = 'red'
nashtext = Label(window, text = 'текст',fg = 'white', bg = 'red') #текст, который мы увидим в window
nashtext.place(x = 50, y = 70)
btn = Button(window, text = 'текст', command = funk1, width = 40, height = 2,fg = 'white', bg = 'grey') #кнопка, которую можно нажать, после чего будет вызвана функция funk1
btn.place(x = 70, y = 100)
img = PhotoImage(file="название файла с изображением") #изображение будет расположено в окне window
button = Button(window, image=img, command = funkwin1)
button.pack()
button.place(x = 100, y = 100)

window.mainloop() 
