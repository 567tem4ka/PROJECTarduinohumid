from tkinter import *
from bs4 import BeautifulSoup
import mainprogramm

hivemqurl = 'https://www.hivemq.com/demos/websocket-client/'
DATA = 'data'

def change():
    text.delete('1.0', END)
    text.insert(1.0, DATA)

root = Tk()
root.title("дачик вепав")
root.geometry("300x250")
text = Text(width=25, height=5)
text.pack()
b1 = Button(text="обновить",
            width=15, height=3)
b1.config(command=change)
b1.pack()
root.mainloop()
