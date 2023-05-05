from tkinter import *
from time import strftime
import random


def time():
    string = strftime('%H:%M:%S')
    clock_label.config(text=string)
    clock_label.after(1000, time)


def show_temperature():
    label_show_temp = Label(text=f'Temperature of the engine:  {stock_temp[0]:.1f} °C', font=('calibri', 20, 'bold'), fg="black")
    label_show_temp.place(x=20, y=100)
    label_show_temp.after(500, show_temperature)
    label_show_temp.after(500, change_temp)
    label_show_temp.after(1000, unexpected_item)


def show_speed_of_production():
    label_show_speed = Label(text=f'Speed of the production:  {stock_speed[0]:.1f}x  ', font=('calibri', 20, 'bold'), fg="black")
    label_show_speed.place(x=20, y=140)
    label_show_speed.after(500, show_speed_of_production)


def change_speed(reverse):
    if reverse == 1:
        speed_if[0] = 1
    elif reverse == 2:
        speed_if[0] = 2
    elif reverse == 3:
        speed_if[0] = 3
    elif reverse == 0:
        speed_if[0] = 0


def change_temp():
    if stock_temp[0] >= 50.0:
        is_overheated[0] = 1
        stock_speed[0] = 0
        speed_if[0] = 0
    if stock_temp[0] < 50.0:
        is_overheated[0] = 0

    if speed_if[0] == 1 and is_overheated[0] == 0 and stock_temp[0] >= 35.0:
        stock_temp[0] -= 0.2
        stock_speed[0] = 0.5
    if speed_if[0] == 2 and is_overheated[0] == 0:
        stock_temp[0] += 0.1
        stock_speed[0] = 1
    if speed_if[0] == 3 and is_overheated[0] == 0:
        stock_temp[0] += 0.5
        stock_speed[0] = 2
    if speed_if[0] == 0 and stock_temp[0] >= 35.0:
        stock_temp[0] -= 0.5
        stock_speed[0] = 0

    if time_reaction[0] >= 30:
        speed_if[0] = 0
        stock_speed[0] = 0


def reaction_check():
    if time_did_click[0] == 0:
        time_reaction[0] += 1
    elif time_did_click[0] == 1:
        time_reaction[0] = 0
        time_did_click[0] = 0


def show_reaction_timer():
    label_show_reaction_timer = Label(text=f'Reaction time:  {time_reaction[0]}s  ', font=('calibri', 20, 'bold'), fg="black")
    label_show_reaction_message = Label(text=f'After 30s of no reaction the engine will shut down!!!', font=('calibri', 10, 'bold'), fg="black")
    label_show_reaction_timer.place(x=570, y=140)
    label_show_reaction_message.place(x=500, y=110)
    label_show_reaction_timer.after(1000, reaction_check)
    label_show_reaction_timer.after(1000, show_reaction_timer)


def reaction_clicked():
    time_did_click[0] = 1


def clicked_on_item():
    is_taken_off[0] = 1


def unexpected_text():
    label_unexpected = Label(text=f'There is a hostile item on the production line', font=('calibri', 15, 'bold'), fg="black")
    label_unexpected_1 = Label(text=f'take it down quickly, before it stops the machine!', font=('calibri', 15, 'bold'), fg="black")
    label_unexpected.place(x=100, y=200)
    label_unexpected_1.place(x=100, y=250)


def unexpected_item():
    x = random.random()
    if x <= 0.2 and is_taken_off[0] == 1:
        unexpected_text()
        is_taken_off[0] = 0
        x_0 = random.randint(100, 300)
        y_0 = random.randint(300, 600)
        button_take_item.place(x=x_0, y=y_0)
    elif is_taken_off[0] == 1:
        label_unexpected = Label(text=f'                                                                               ', font=('calibri', 15, 'bold'), fg="black")
        label_unexpected_1 = Label(text=f'                                                                                      ', font=('calibri', 15, 'bold'), fg="black")
        label_unexpected.place(x=100, y=200)
        label_unexpected_1.place(x=100, y=250)
    if is_taken_off[0] == 0:
        time_on_machine[0] += 1
        if time_on_machine[0] >= 10:
            change_speed(0)
    if is_taken_off[0] == 1:
        time_on_machine[0] = 0


# main root
root = Tk()
root.geometry("800x640")

# some variables
is_taken_off = [1]
is_on_machine = [0]
time_on_machine = [0]

# temperature of the machine
stock_temp = [40.0]
stock_speed = [1]
speed_if = [2]
is_overheated = [0]
time_reaction = [0]
time_did_click = [0]

show_reaction_timer()
show_temperature()
show_speed_of_production()

# buttons controlling speed of the production
button_dec_temp = Button(root, width=18, height=3, text="Stop production", command=lambda: change_speed(0))
button_dec_temp.place(x=600, y=390)
button_dec_temp = Button(root, width=18, height=3, text="Less speed (0.5x)", command=lambda: change_speed(1))
button_dec_temp.place(x=600, y=450)
button_dec_temp = Button(root, width=18, height=3, text="Normal speed (1x)", command=lambda: change_speed(2))
button_dec_temp.place(x=600, y=510)
button_dec_temp = Button(root, width=18, height=3, text="More speed (2x)", command=lambda: change_speed(3))
button_dec_temp.place(x=600, y=570)

button_check_reaction = Button(root, width=18, height=3, text="Confirm reaction", command=lambda: reaction_clicked())
button_check_reaction.place(x=600, y=250)

button_take_item = Button(root, width=18, height=3, text="Take the item off",
                          command=lambda: [clicked_on_item(), button_take_item.pack_forget()])


# clock
clock_label = Label(root, font=('calibri', 40, 'bold'), bg="purple")
clock_label.place(x=300, y=10)
time()

root.mainloop()
