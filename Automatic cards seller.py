from tkinter import *
import customtkinter
import pyautogui
import asyncio
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

#Title, icon and dimension of the program
root.title('Automatic cards seller')
root.iconbitmap('images/gachapon.ico')
root.geometry('700x400')

#some varibles i writed here because i was getting errors, so doing this it got fixed, and probably dont needed but i leave it there just in case
numbers = ''
l = ''
tiempo = ''
tipo = ''
w=5

#function to delete all in the textbox
def delete():
    my_text.delete(0.0, 'end')

#function to sort all numbers in descending form
def sort():
    global numbers
    global l
    l= []
    numbers = my_text.get(0.0, 'end')
    numbers = numbers.split(',')
    numbers = [int(x) for x in numbers]
    numbers = sorted(numbers)
    z = len(numbers)
    z = z - 1
    for y in numbers:
        l.append(numbers[z])
        z =  z - 1
    my_text.delete(0.0, 'end')
    i = 0
    for x in l:
        my_text.insert('end'," " + str(l[i]))
        i = i + 1

#main function process to get things done
def start():
    for x in l:
        loc = pyautogui.locateOnScreen('images/text.png', confidence=0.95) #here it fetch for the image to look where to write
        poi = pyautogui.center(loc)
        pyautogui.click(poi.x,poi.y,duration=.57)
        pyautogui.typewrite('gsell ')
        pyautogui.typewrite(str(x))
        pyautogui.hotkey('enter')
        my_text.delete(0.0, 'end')
        my_text.insert('end', "In process card number: " + str(x))
        root.update()
        root.after(2000) #delay needed to wait the bot
        t = 0
        while bool(t) == False:
            try:
                loc1 = pyautogui.locateOnScreen('images/confirm.png', confidence=0.95) #here it fetch for the image to click on it
                poi1 = pyautogui.center(loc1)
                t = 1
            except:
                pass
        pyautogui.click(poi1.x,poi1.y,duration=.57)
        t1 = 0
        while bool(t1) == False:
            try:
                loc3 = pyautogui.locateOnScreen('images/value.png', confidence=0.95) #here it fetch for the image to click on it
                poi3 = pyautogui.center(loc3)
                t1 = 1
            except:
                pass
        pyautogui.hotkey('tab')
        pyautogui.typewrite(valor)
        pyautogui.hotkey('tab')
        pyautogui.typewrite(tiempo)
        pyautogui.hotkey('tab')
        pyautogui.typewrite(tipo)
        pyautogui.hotkey('enter')
        t2 = 0
        while bool(t2) == False:
            try:
                loc2 = pyautogui.locateOnScreen('images/yes.png', confidence=0.95) #here it fetch for the image to click on it
                poi2 = pyautogui.center(loc2)
                t2 = 1
            except:
                pass
        pyautogui.click(poi2.x,poi2.y,duration=.57)
        my_text.delete(0.0, 'end')
        my_text.insert('end', "Finished card number: " + str(x)) #here finished the process to sell 1 card
        root.update()
    my_text.delete(0.0, 'end')
    my_text.insert('end', "All cards have been put on sell")
    root.update()
    
#variable of candy
def candy_event():
    global tipo
    tip = candy_var.get()
    if tip == "yes candy":
        tipo = "candy"
    else:
        tipo = ''

#variable of heart
def heart_event():
    global tipo
    tip = heart_var.get()
    if tip == "yes heart":
        tipo = "heart"
    else:
        tipo = ''

#variable of coins
def coins_event():
    global tipo
    tip = coins_var.get()
    if tip == "yes coins":
        tipo = "coins"
    else:
        tipo = ''

#variable of time
def button_tiempo():
    global tiempo
    dialog = customtkinter.CTkInputDialog(text="Input the time it gonne be on sell", title="Time of the cards")
    tiempo = dialog.get_input()

#variable of value for each card
def button_valor():
    global valor
    dialog = customtkinter.CTkInputDialog(text="Input the value of the card", title="Value of the cards")
    valor = dialog.get_input()

label = customtkinter.CTkLabel(root, text="Input all numbers of the cards you want to sell", fg_color="transparent")
label.pack(pady=2)

my_text = customtkinter.CTkTextbox(root)
my_text.pack(pady=10)

my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=20)

##values and configuration of the buttons
delete_button = customtkinter.CTkButton(my_frame, text="Delete", command=delete)
ordenar_button = customtkinter.CTkButton(my_frame, text="Sort", command=sort)
vender_button = customtkinter.CTkButton(my_frame, text="Start", command=start)
Tiempo = customtkinter.CTkButton(my_frame, text="Time", command=button_tiempo)
Cantidad = customtkinter.CTkButton(my_frame, text="Value", command=button_valor)

#values and configuration of the switches
candy_var = customtkinter.StringVar(value="no candy")
switch_candy = customtkinter.CTkSwitch(my_frame, text="candy", command=candy_event,
                                 variable=candy_var, onvalue="yes candy", offvalue="no candy")

heart_var = customtkinter.StringVar(value="no heart")
switch_heart = customtkinter.CTkSwitch(my_frame, text="heart", command=heart_event,
                                 variable=heart_var, onvalue="yes heart", offvalue="no heart")

coins_var = customtkinter.StringVar(value="no coins")
switch_coins = customtkinter.CTkSwitch(my_frame, text="coins", command=coins_event,
                                 variable=coins_var, onvalue="yes coins", offvalue="no coins")

#grid of all functions displayed to the user
delete_button.grid(row=0, column=0)
ordenar_button.grid(row=0, column=1, padx=10)
vender_button.grid(row=0, column=2)
switch_candy.grid(row=1, column=0)
switch_heart.grid(row=1, column=1, padx=10)
switch_coins.grid(row=1, column=2)
Tiempo.grid(row=2, column=0)
Cantidad.grid(row=2, column=2)

root.mainloop()