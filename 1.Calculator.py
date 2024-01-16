from tkinter import *
import string


def click(event):
    global user_value
    argument = event.widget.cget("text")
    if argument == "C":
        user_value.set("")
        screen.update()
    elif argument == "=":
        if user_value.get().isdigit():
            value = int(user_value)
        else:
            try:
                value = int(eval(user_value.get()))
            except Exception as e:
                value = "Error"
        user_value.set(value)
        screen.update()
    else:
        user_value.set(user_value.get() + argument)
        screen.update()


root = Tk()
root.geometry("400x700")
root.wm_title("Calculator By Arbaz")
root.config(bg="#606075")
if __name__ == '__main__':
    user_value = StringVar()
    user_value.set("")
    screen = Entry(root, textvariable=user_value, font="timesnewroman 30 bold")
    screen.pack(fill=X, pady=10, padx=6, ipady=10, ipadx=8)
    buttons = list(string.digits)[::-1]
    buttons.extend(["00", ".", "/", "*", "+", "-", "="])
    buttons.insert(0, "C")
    bframe = Frame(root, bg="#405357")
    r = 0
    c = 0
    for i in range(len(buttons)):
        all_btns = Button(bframe, text=buttons[i], height=2, width=5, font="timesnewroman 19 bold", relief=GROOVE,
                          overrelief=FLAT, bg="#1B2C33", fg="white")
        all_btns.grid(row=r, column=c, padx=10, pady=8)
        all_btns.bind("<Button-1>", click)
        if i % 3 == 2:
            c = -1
            r += 1
        c += 1
    bframe.pack(anchor=CENTER)
    root.mainloop()
