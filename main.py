#!/usr/bin/env python
# This is my btc.py script.
import requests
from tkinter import*
from threading import Timer
from datetime import datetime
from datetime import date
import time
import os
from currency_converter import CurrencyConverter

from PIL import ImageTk,Image

window = Tk()
window.geometry("400x430")
window.configure(bg='black')
window.title('Bitcoin Price Watcher')

c = CurrencyConverter()
def printa():

	response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
	data = response.json()
	cad = (data["bpi"]["USD"]["rate_float"])

	real_cad = c.convert(cad, 'USD', 'CAD')
	real_real_cad = round(real_cad,4)
	real_real_real_cad = "{:,}".format(real_real_cad )
	CAD.config(text= "$" + str(real_real_real_cad) + "(CAD)")
	main_string.config(text= "$" + data["bpi"]["USD"]["rate"] + "(USD)")
	pound.config(text= "£" + data["bpi"]["GBP"]["rate"])
	euro.config(text= "€" + data["bpi"]["EUR"]["rate"])

	#print(data["bpi"]["USD"]["rate"])
	Timer(5, printa).start()

def date_time():
	today = date.today()
	d2 = today.strftime("%B %d, %Y")

	current_date.config(text=d2)
	t = time.localtime()
	current_time = time.strftime("%I:%M.%S %p")
	current_time_win.config(text=current_time)
	Timer(1, date_time).start()



watermark = Label(window, text= "Bitcoin Price:", font=("Helvetica", 19), fg =("yellow"), bg=("black"))
watermark.pack()
CAD = Label(window, text= "", font=("Helvetica", 18), fg =("white"), bg=("black"))
CAD.pack()
main_string = Label(window, text= "", font=("Helvetica", 18), fg =("white"), bg=("black"))
main_string.pack()
pound = Label(window, text= "", font=("Helvetica", 18), fg =("white"), bg=("black"))
pound.pack()
euro = Label(window, text= "", font=("Helvetica", 18), fg =("white"), bg=("black"))
euro.pack()


printa()



#button = Button(window, text='press', command=printa)
#button.pack()


	#print("$" + data["bpi"]["USD"]["rate"])
img=PhotoImage(file='logo.gif')
Label(window,image=img, borderwidth=0, highlightthickness=0).pack()
current_date = Label(window, text= "", font=("Helvetica", 18), fg =("white"), bg=("black"))
current_date.pack()
current_time_win = Label(window, text= "", font=("Helvetica", 18), fg =("white"), bg=("black"))
current_time_win.pack()
date_time()
watermark = Label(window, text= "Powered by CoinDesk", font=("Helvetica", 12), fg =("yellow"), bg=("black"))
watermark.pack()
window.mainloop()
